import csv
from collections import namedtuple
from datetime import datetime, timedelta
from operator import itemgetter
import argparse
import sys
import json
# custom imports
from airports_traverse import get_all_possibilities_between_origin_destination
from journey_traverse import transfer_lists_traverse
from progress_bar import print_progress_bar
from time_check import check_within_timeframe
from merge_return import merge_outbound_with_inbound


def command_line_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('input_file', type=argparse.FileType('r'), help='input CSV file location')
    parser.add_argument('origin', help='origin airport code')
    parser.add_argument('destination', help='destination  airport code')
    parser.add_argument('--bags', dest='requested_bags', type=int, default=0, help='number of requested bags')
    parser.add_argument('--transfer', dest='max_transfer', type=int, default=None, help='maximum number of transfers')
    parser.add_argument('--return', dest='return_requested', action='store_true', help='Is it a return flight?')
    parser.add_argument('--progress', dest='print_progress', action='store_true', help='Display progress bar?')
    parser.add_argument('--raw', dest='raw_format_requested', action='store_true', help='Get output as raw dictionary?')
    # 'requested_bags': 0, 'return_requested': False, 'max_transfer': None,
    # 'print_progress': False, 'raw_format_requested': False
    # bugfix: 'example/example3.csv', 'ZRW', 'BPZ', '--progress'
    args = parser.parse_args(['example/example3.csv', 'ZRW', 'BPZ', '--progress', '--return', '--transfer=3'])
    # args = parser.parse_args()
    return args


def scan_csv_file_to_memory(file):
    flights_list_out = []
    correct_fieldnames = ['flight_no', 'origin', 'destination', 'departure', 'arrival',
                          'base_price', 'bag_price', 'bags_allowed']
    with file as csv_file:
        flights = csv.DictReader(csv_file)
        if flights.fieldnames == correct_fieldnames:
            idn = 0
            for row in flights:
                try:
                    datetime.strptime(row['departure'], '%Y-%m-%dT%H:%M:%S')
                    datetime.strptime(row['arrival'], '%Y-%m-%dT%H:%M:%S')
                except ValueError:
                    print(f'Incorrect time format given in CSV departure or arrival column. '
                          f'(format YYYY-MM-DDTHH:MM:SS)')
                    input("Press any key to exit.")
                    sys.exit(0)
                try:
                    row['base_price'] = float(row['base_price'])
                    row['bag_price'] = float(row['bag_price'])
                    row['bags_allowed'] = int(row['bags_allowed'])
                except ValueError:
                    print('Enter valid number for base_price, bag_price, bags_allowed')
                    input("Press any key to exit.")
                    sys.exit(0)
                row['idn'] = idn    # unique id number is added to each row for later use
                idn += 1
                # print(row)
                flights_list_out.append(row)
        else:
            print('The CSV file fieldnames shall be: ' + str(correct_fieldnames))
            input("Press any key to exit.")
            sys.exit(0)
    return flights_list_out


def generate_flights_network_graph(input_data):
    airports = []  # graph vertices
    routes = []  # graph edges
    for row in input_data:
        if row['origin'] not in airports:
            airports.append(row['origin'])
        if row['destination'] not in airports:
            airports.append(row['destination'])
        if (row['origin'], row['destination']) not in routes:
            routes.append((row['origin'], row['destination']))
    network_out = Graph(airports, routes)  # graph object
    return network_out


def validate_origin_destination_input():
    if a.origin not in network.vertices or a.destination not in network.vertices:
        print('Either origin or destination airport codes are not present in database! (Case sensitive!)')
        input("Press any key to exit.")
        sys.exit(0)


def convert_to_adjacency_list(graph, start, end):
    output_dictionary = {vertex: [] for vertex in graph.vertices}
    for edge in graph.edges:
        vertex_1, vertex_2 = edge[0], edge[1]
        if vertex_1 != end and vertex_2 != start:  # filter out return flights to make directed graph
            output_dictionary[vertex_1].append(vertex_2)
    return output_dictionary


def generate_travel_plans():
    if a.print_progress:
        print('Discovering possible combinations...')
    travel_plans_all = []
    outbound_adj = convert_to_adjacency_list(network, a.origin, a.destination)
    # print(outbound_adj)
    travel_plans_out = get_all_possibilities_between_origin_destination(
        outbound_adj, a.origin, a.destination, a.max_transfer)
    travel_plans_all.append(travel_plans_out)
    if a.return_requested:
        inbound_adj = convert_to_adjacency_list(network, a.destination, a.origin)
        # print(inbound_adj)
        travel_plans_back = get_all_possibilities_between_origin_destination(
            inbound_adj, a.destination, a.origin, a.max_transfer)
        travel_plans_all.append(travel_plans_back)
    if a.print_progress:
        print('Done!')
    return travel_plans_all


def assign_flights_to_travel_plans(plans, min_bags):
    fetched_flight_ids = {'out': [], 'in': []}

    def outbound_or_inbound_loop(plans_number, dictionary_key):
        i = 0
        for current_travel_plan in plans[plans_number]:    # 0 is outbound travel plans
            i += 1
            if a.print_progress:
                plans_length = len(plans[plans_number])
                print_progress_bar(
                    i, plans_length, prefix='Currently evaluating: ' + str(current_travel_plan), length=50)
            ids_list = fetch_flight_ids_within_travel_plan(current_travel_plan, min_bags)
            for item in ids_list:   # to extract inner list
                fetched_flight_ids[dictionary_key].append(item)

    outbound_or_inbound_loop(0, 'out')      # outbound case, this is always used
    if not a.return_requested:
        # print(fetched_flight_ids['out'])
        fetched_flights = convert_flight_ids_to_flights(fetched_flight_ids['out'])
        return fetched_flights
    else:
        outbound_or_inbound_loop(1, 'in')   # in case of return the outbound cases are amended with inbound cases
        if a.print_progress:
            print('Merging outbound and inbound solutions...')
        return_adjacency_list = check_return_flight_compatibility()
        # print(return_adjacency_list)
        merged_fetched_flight_ids = merge_outbound_with_inbound(fetched_flight_ids, return_adjacency_list)
        # print(merged_fetched_flight_ids)
        merged_fetched_flights = convert_flight_ids_to_flights(merged_fetched_flight_ids)
        # print(merged_fetched_flights)
        if a.print_progress:
            print('Done!')
        return merged_fetched_flights


def fetch_flight_ids_within_travel_plan(travel_plan, min_bags):
    transfer_lists = {}     # adjacency list
    graph_starts = []
    travel_plan_length = len(travel_plan)
    if travel_plan_length == 1:
        sectors_to_check = [0]
    else:
        sectors_to_check = [i for i in range(travel_plan_length - 1)]
    for i in sectors_to_check:
        first_trip_origin, first_trip_destination = travel_plan[i][0], travel_plan[i][1]
        for row_1 in flights_list:
            if row_1['origin'] == first_trip_origin and row_1['destination'] == first_trip_destination and \
                    row_1['bags_allowed'] >= min_bags:
                transfer_lists[row_1['idn']] = []
                if i == 0:      # to collect the first leg id's as starting points for the graph traversal
                    graph_starts.append(row_1['idn'])
                if travel_plan_length > 1:
                    second_trip_origin, second_trip_destination = travel_plan[i + 1][0], travel_plan[i + 1][1]
                    for row_2 in flights_list:
                        if row_2['origin'] == second_trip_origin and row_2['destination'] == second_trip_destination \
                                and row_2['bags_allowed'] >= min_bags \
                                and check_within_timeframe(row_1['arrival'], row_2['departure'], False):  # layover=F
                            transfer_lists[row_1['idn']].append(row_2['idn'])
    # print(transfer_lists)
    # print(graph_starts)
    # print(travel_plan_length)
    list_of_flights_ids = transfer_lists_traverse(graph_starts, transfer_lists, travel_plan_length)
    return list_of_flights_ids


def convert_flight_ids_to_flights(input_list):
    list_of_flights = []
    for current_list in input_list:
        current_list_of_flights = []
        for current_id in current_list:
            for row in flights_list:
                if row['idn'] == current_id:
                    current_list_of_flights.append(row)
        list_of_flights.append(current_list_of_flights[:])
    return list_of_flights


def check_return_flight_compatibility():
    transfer_lists = {}  # adjacency list
    for row_1 in flights_list:
        if row_1['destination'] == a.destination:
            transfer_lists[row_1['idn']] = []
            for row_2 in flights_list:
                if row_2['origin'] == a.destination \
                        and check_within_timeframe(row_1['arrival'], row_2['departure'], True):  # layover=T
                    transfer_lists[row_1['idn']].append(row_2['idn'])
    return transfer_lists


def generate_output_list(fetched_flights, min_bags):
    output_list = []
    for flights_found in fetched_flights:
        bags_allowed = []
        total_price = 0.0
        travel_time = timedelta(hours=0)
        for flight_leg in flights_found:
            # print(flight_leg)
            bags_allowed.append(flight_leg['bags_allowed'])
            total_price += flight_leg['base_price'] + flight_leg['bag_price']  # not sure if bag_price * bag_nbr
            current_flight_time = datetime.strptime(flight_leg['arrival'], '%Y-%m-%dT%H:%M:%S') \
                - datetime.strptime(flight_leg['departure'], '%Y-%m-%dT%H:%M:%S')
            travel_time += current_flight_time
        # print(flights_found)
        current_dictionary = {'flights': flights_found,
                              'origin': a.origin,
                              'destination': a.destination,
                              'bags_allowed': min(bags_allowed),
                              'bags_count': min_bags,
                              'total_price': total_price,
                              'travel_time': str(travel_time)}
        output_list.append(current_dictionary)
    return output_list


def remove_id_numbers(input_list):
    for i in input_list:
        for j in i:
            if j == 'flights':
                for k in i['flights']:
                    k.pop('idn', None)


def convert_to_json_format(input_list):
    stringed_list = str(input_list)
    stringed_list = stringed_list.replace("\'", "\"")
    # print(stringed_list)
    parsed = json.loads(stringed_list)
    converted = json.dumps(parsed, indent=4, sort_keys=False)
    return converted


if __name__ == '__main__':
    Graph = namedtuple('Graph', ['vertices', 'edges'])  # create graph namedtuple
    a = command_line_arguments()
    # print(a)
    flights_list = scan_csv_file_to_memory(a.input_file)
    # print(flights_list)
    network = generate_flights_network_graph(flights_list)
    # print(network)
    validate_origin_destination_input()
    travel_plans = generate_travel_plans()
    if a.print_progress:
        if not a.return_requested:
            print(f'Found {str(len(travel_plans))} possible combinations.')
        else:
            print(f'Found {str(len(travel_plans[0]))} possible outbound combinations.')
            print(f'Found {str(len(travel_plans[1]))} possible inbound combinations.')
    # print(travel_plans)
    journey_list = assign_flights_to_travel_plans(travel_plans, a.requested_bags)
    # print(journey_list)
    output = generate_output_list(journey_list, a.requested_bags)
    # print(output)
    remove_id_numbers(output)
    ordered_output = sorted(output, key=itemgetter('total_price'), reverse=False)  # ascending
    if a.raw_format_requested:
        print(ordered_output)
    else:
        json_output = convert_to_json_format(ordered_output)
        print(json_output)
