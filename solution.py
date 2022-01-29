import csv
from collections import namedtuple
from datetime import datetime, timedelta
from operator import itemgetter
import sys
import os
# custom imports
from graph_traverse import get_all_possibilities_between_origin_destination
from journey_filter import discover_all_combinations
from progress_bar import print_progress_bar


def command_line_arguments():
    def index_containing_substring(the_list, substring):
        for idx, s in enumerate(the_list):
            if substring in s:
                return idx
        return False

    def search_and_validate_number_argument(search_string, warning_text, default_value):
        argument_indexes[search_string] = index_containing_substring(sys.argv, search_string)
        if argument_indexes[search_string]:
            try:
                argument = sys.argv[argument_indexes[search_string]].split('=')[1]
                argument = int(argument)
            except ValueError:      # in case not a number is entered
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
    # print("\nArguments passed: " + str(argument_numbers))
    # print(sys.argv)
    if argument_numbers < 4:    # validate if mandatory arguments are given
        print('Mandatory arguments are missing! Required: CSV file location, origin airport, destination airport.')
        print('Example: python -m solution example/example0.csv WIW RFZ')
        input("Press any key to exit.")
        sys.exit(0)
    arguments['input_file'] = sys.argv[1]
    if not os.path.isfile('./' + arguments['input_file']):
        print("Input CSV file does not exist.")
        input("Press any key to exit.")
        sys.exit(0)
    arguments['origin'] = sys.argv[2]   # validated later
    arguments['destination'] = sys.argv[3]   # validated later
    arguments['requested_bags'] = search_and_validate_number_argument('--bags=', 'requested bags', 0)
    arguments['max_transfer'] = search_and_validate_number_argument('--transfer=', 'maximum transfers', None)
    arguments['return_requested'] = search_boolean_argument('--return')
    arguments['print_progress'] = search_boolean_argument('--progress')
    return arguments


def scan_csv_file_to_memory(file):
    flights_list_out = []
    correct_fieldnames = ['flight_no', 'origin', 'destination', 'departure', 'arrival',
                          'base_price', 'bag_price', 'bags_allowed']
    with open(file, newline='') as csv_file:
        flights = csv.DictReader(csv_file)
        if flights.fieldnames == correct_fieldnames:
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
                # print(row)
                flights_list_out.append(row)
        else:
            print('The CSV file fieldnames shall be: ' + str(correct_fieldnames))
            input("Press any key to exit.")
            sys.exit(0)
    return flights_list_out


def generate_flights_network_graph(input_data):
    airports = []   # these are the graph vertices
    routes = []   # these are the graph edges
    for row in input_data:
        if row['origin'] not in airports:
            airports.append(row['origin'])
        if row['destination'] not in airports:
            airports.append(row['destination'])
        if (row['origin'], row['destination']) not in routes:
            routes.append((row['origin'], row['destination']))
    network_out = Graph(airports, routes)   # initialize graph object
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
        if vertex_1 != end and vertex_2 != start:   # filter out return flights to make directed graph
            output_dictionary[vertex_1].append(vertex_2)
    return output_dictionary


def generate_travel_plans():    # handles one-way only and return trips as well
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
        intermediate_step = discover_all_combinations(return_trip, True, a['destination'])
        # print(intermediate_step)
        travel_plans_return = []
        for i in intermediate_step:
            current_list = []
            for j in i:
                for k in j:
                    current_list.append(k)
            travel_plans_return.append(current_list[:])
        return travel_plans_return
    return travel_plans_out


def fetch_flights_within_travel_plan(travel_plan, min_bags):
    possible_journeys = {}
    leg_counter = 0
    for leg in travel_plan:
        possible_journeys[leg_counter] = []
        current_origin, current_destination = leg[0], leg[1]
        for row in flights_list:
            if row['origin'] == current_origin and row['destination'] == current_destination and \
                    row['bags_allowed'] >= min_bags:
                possible_journeys[leg_counter].append(row)
        leg_counter += 1
    # print(possible_journeys)
    return discover_all_combinations(possible_journeys, False, a['destination'])


def convert_to_output_format(plans, min_bags):
    output_list = []
    plans_length = len(plans)
    i = 0
    for current_travel_plan in plans:
        # print(current_travel_plan)
        i += 1
        if a['print_progress']:
            print_progress_bar(i, plans_length, prefix='Currently evaluating: ' + str(current_travel_plan), length=50)
        fetched_flights = fetch_flights_within_travel_plan(current_travel_plan, min_bags)
        for flights_found in fetched_flights:
            bags_allowed = []
            total_price = 0.0
            travel_time = timedelta(hours=0)
            for flight_leg in flights_found:
                # print(flight_leg)
                bags_allowed.append(flight_leg['bags_allowed'])
                total_price += flight_leg['base_price'] + flight_leg['bag_price']   # not sure if bag_price * bag_nbr
                current_flight_time = datetime.strptime(flight_leg['arrival'], '%Y-%m-%dT%H:%M:%S') - \
                    datetime.strptime(flight_leg['departure'], '%Y-%m-%dT%H:%M:%S')
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


if __name__ == '__main__':
    # development arguments
    # a = {'input_file': 'example/example1.csv', 'origin': 'DHE', 'destination': 'NIZ',
    #      'requested_bags': 0, 'return_requested': True, 'max_transfer': 1, 'print_progress': True}
    Graph = namedtuple('Graph', ['vertices', 'edges'])          # create graph namedtuple

    a = command_line_arguments()
    print(a)
    flights_list = scan_csv_file_to_memory(a['input_file'])
    # print(flights_list)
    network = generate_flights_network_graph(flights_list)
    # print(network)
    validate_origin_destination_input()
    travel_plans = generate_travel_plans()
    # print(travel_plans)
    output = convert_to_output_format(travel_plans, a['requested_bags'])
    # print(output)
    ordered_output = sorted(output, key=itemgetter('total_price'), reverse=False)   # ascending
    print()     # print new line before output
    print(ordered_output)
    # for line in ordered_output:
    #     print(line)
