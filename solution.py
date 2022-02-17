import csv
from collections import namedtuple
from datetime import datetime, timedelta
from operator import itemgetter
import sys
import os
import json
# custom imports
from graph_traverse import get_all_possibilities_between_origin_destination
from journey_filter import discover_all_combinations
from progress_bar import print_progress_bar
from time_check import check_total_trip_time, check_within_timeframe


def command_line_arguments():
    def index_containing_substring(input_list, substring):
        for idx, s in enumerate(input_list):
            if substring in s:
                return idx
        return False

    def search_and_validate_number_argument(search_string, warning_text, default_value):
        argument_indexes[search_string] = index_containing_substring(sys.argv, search_string)
        if argument_indexes[search_string]:
            try:
                argument = sys.argv[argument_indexes[search_string]].split('=')[1]
                argument = int(argument)
            except ValueError:
                print(f'Enter valid number for {warning_text} (format {search_string}1)')
                input("Press any key to exit.")
                sys.exit(0)
        else:
            argument = default_value
        return argument

    def search_boolean_argument(search_string):
        if search_string in sys.argv:
            argument = True
        else:
            argument = False
        return argument

    arguments = {}
    argument_indexes = {}
    argument_numbers = len(sys.argv)
    # print(sys.argv)
    if argument_numbers < 4:
        print('Mandatory arguments are missing! Required: CSV file location, origin airport, destination airport.')
        print('Example: python -m solution example/example0.csv WIW RFZ')
        input("Press any key to exit.")
        sys.exit(0)
    arguments['input_file'] = sys.argv[1]
    if not os.path.isfile('./' + arguments['input_file']):
        print("Input CSV file does not exist.")
        input("Press any key to exit.")
        sys.exit(0)
    arguments['origin'] = sys.argv[2]  # validated later
    arguments['destination'] = sys.argv[3]  # validated later
    arguments['requested_bags'] = search_and_validate_number_argument('--bags=', 'requested bags', 0)
    arguments['max_transfer'] = search_and_validate_number_argument('--transfer=', 'maximum transfers', None)
    arguments['return_requested'] = search_boolean_argument('--return')
    arguments['print_progress'] = search_boolean_argument('--progress')
    arguments['raw_format_requested'] = search_boolean_argument('--raw')
    return arguments


def scan_csv_file_to_memory(file):
    flights_list_out = []
    correct_fieldnames = ['flight_no', 'origin', 'destination', 'departure', 'arrival',
                          'base_price', 'bag_price', 'bags_allowed']
    with open(file, newline='') as csv_file:
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
                print(row)
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
    if a['origin'] not in network.vertices or a['destination'] not in network.vertices:
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
    outbound_adj = convert_to_adjacency_list(network, a['origin'], a['destination'])
    # print(outbound_adj)
    travel_plans_out = get_all_possibilities_between_origin_destination(
        outbound_adj, a['origin'], a['destination'], a['max_transfer'])
    # print(travel_plans_out)
    if a['return_requested']:
        inbound_adj = convert_to_adjacency_list(network, a['destination'], a['origin'])
        # print(inbound_adj)
        travel_plans_back = get_all_possibilities_between_origin_destination(
            inbound_adj, a['destination'], a['origin'], a['max_transfer'])
        # print(travel_plans_back)
        return_trip = {0: travel_plans_out, 1: travel_plans_back}
        intermediate_step = [[outbound, inbound] for outbound in return_trip[0] for inbound in return_trip[1]]
        # print(intermediate_step)
        travel_plans_return = []  # merging outbound and inbound solutions
        for i in intermediate_step:
            current_list = []
            for j in i:
                for k in j:
                    current_list.append(k)
            travel_plans_return.append(current_list[:])
        return travel_plans_return
    return travel_plans_out

"""
def fetch_flights_within_travel_plan(min_bags):    # (travel_plan, min_bags)
    travel_plan = [('DHE', 'SML'), ('SML', 'NRX'), ('NRX', 'NIZ')]
    first_trip_origin, first_trip_destination = travel_plan[0][0], travel_plan[0][1]
    possible_journeys = []
    dictionary_counter = 0
    for row_1 in flights_list:      # outer loop for iterating first leg flights
        if row_1['origin'] == first_trip_origin and row_1['destination'] == first_trip_destination and \
                row_1['bags_allowed'] >= min_bags:
            possible_journeys.append({0: [row_1]})
            if len(travel_plan) > 1:
                first_trip_arrival = row_1['arrival']
                travel_plan_slice = travel_plan[1:]
                leg_counter = 1
                for leg in travel_plan_slice:   # inner loop for iterating other sectors
                    possible_journeys[dictionary_counter][leg_counter] = []
                    current_origin, current_destination = leg[0], leg[1]
                    for row_2 in flights_list:
                        if row_2['origin'] == current_origin and row_2['destination'] == current_destination and \
                                row_2['bags_allowed'] >= min_bags and \
                                check_total_trip_time(first_trip_arrival, row_2['departure']):
                            possible_journeys[dictionary_counter][leg_counter].append(row_2)
                    leg_counter += 1
            dictionary_counter += 1
    print(possible_journeys)
    return #discover_all_combinations(possible_journeys, a['destination'])
"""


def fetch_flights_within_travel_plan_2(min_bags):
    transfer_lists = {}
    graph_starts = []
    travel_plan = [('DHE', 'SML')]
    travel_plan_length = len(travel_plan)
    if travel_plan_length == 1:
        sectors_to_check = [0]
    else:
        sectors_to_check = [i for i in range(len(travel_plan) - 1)]
    for i in sectors_to_check:
        first_trip_origin, first_trip_destination = travel_plan[i][0], travel_plan[i][1]
        for row_1 in flights_list:
            if row_1['origin'] == first_trip_origin and row_1['destination'] == first_trip_destination and \
                    row_1['bags_allowed'] >= min_bags:
                transfer_lists[str(row_1['idn'])+row_1['origin']+row_1['destination']] = []
                if i == 0:      # to collect the first leg id's as starting points for the graph traversal
                    graph_starts.append(str(row_1['idn'])+row_1['origin']+row_1['destination'])
                if travel_plan_length > 1:
                    second_trip_origin, second_trip_destination = travel_plan[i + 1][0], travel_plan[i + 1][1]
                    for row_2 in flights_list:
                        if row_2['origin'] == a['destination']:
                            layover = True      # this does not necessarily mean that it's layover, but the next if
                        else:                   # statement makes it clear
                            layover = False
                        if row_2['origin'] == second_trip_origin and row_2['destination'] == second_trip_destination and \
                                row_2['bags_allowed'] >= min_bags and check_within_timeframe(row_1['arrival'], row_2['departure'], layover):
                            transfer_lists[str(row_1['idn'])+row_1['origin']+row_1['destination']].append(str(row_2['idn'])+row_2['origin']+row_2['destination'])
    print(travel_plan_length)
    print(transfer_lists)
    print(graph_starts)


def generate_output_list(plans, min_bags):
    output_list = []
    i = 0
    for current_travel_plan in plans:
        # print(current_travel_plan)
        i += 1
        if a['print_progress']:
            plans_length = len(plans)
            print_progress_bar(i, plans_length, prefix='Currently evaluating: ' + str(current_travel_plan), length=50)
        fetched_flights = fetch_flights_within_travel_plan_2(current_travel_plan, min_bags)
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
                                  'origin': a['origin'],
                                  'destination': a['destination'],
                                  'bags_allowed': min(bags_allowed),
                                  'bags_count': min_bags,
                                  'total_price': total_price,
                                  'travel_time': str(travel_time)}
            output_list.append(current_dictionary)
    return output_list


def convert_to_json_format(input_list):
    stringed_list = str(input_list)
    stringed_list = stringed_list.replace("\'", "\"")
    # print(stringed_list)
    parsed = json.loads(stringed_list)
    converted = json.dumps(parsed, indent=4, sort_keys=False)
    return converted


if __name__ == '__main__':
    # development arguments
    a = {'input_file': 'example/example1l.csv', 'origin': 'DHE', 'destination': 'NIZ', 'requested_bags': 0,
         'return_requested': False, 'max_transfer': None, 'print_progress': True, 'raw_format_requested': True}
    Graph = namedtuple('Graph', ['vertices', 'edges'])  # create graph namedtuple

    #a = command_line_arguments()
    # print(a)
    flights_list = scan_csv_file_to_memory(a['input_file'])
    # print(flights_list)
    network = generate_flights_network_graph(flights_list)
    # print(network)
    validate_origin_destination_input()
    travel_plans = generate_travel_plans()
    fetch_flights_within_travel_plan_2(0)
    # print(len(travel_plans))
    # for i in travel_plans:
    #     print(i)
    # # print(travel_plans)
    """output = generate_output_list(travel_plans, a['requested_bags'])
    # print(output)
    ordered_output = sorted(output, key=itemgetter('total_price'), reverse=False)  # ascending
    if a['raw_format_requested']:
        print(ordered_output)
    else:
        json_output = convert_to_json_format(ordered_output)
        print(json_output)"""
