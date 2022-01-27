import csv
from collections import namedtuple
from graph_traverse import get_all_possibilities_between_origin_destination
from journey_filter import search_for_connective_flights


def scan_csv_file_to_memory(file):
    flights_list_out = []
    with open(file, newline='') as csv_file:
        flights = csv.DictReader(csv_file)
        for row in flights:
            flights_list_out.append(row)
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


def convert_to_adjacency_list(graph, start, end):
    output_dictionary = {vertex: [] for vertex in graph.vertices}
    for edge in graph.edges:
        vertex_1, vertex_2 = edge[0], edge[1]
        if vertex_1 != end and vertex_2 != start:   # filter out return flights to make directed graph
            output_dictionary[vertex_1].append(vertex_2)
    return output_dictionary


def fetch_flights_within_travel_plan(travel_plan):
    possible_journeys = {}
    leg_counter = 0
    for leg in travel_plan:
        possible_journeys[leg_counter] = []
        current_origin, current_destination = leg[0], leg[1]
        for row in flights_list:
            if row['origin'] == current_origin and row['destination'] == current_destination:
                possible_journeys[leg_counter].append(row)
        leg_counter += 1
    # print(possible_journeys)
    return search_for_connective_flights(possible_journeys)


if __name__ == '__main__':
    # mandatory arguments
    origin = 'WIW'
    destination = 'RFZ'
    input_file = 'example/example0.csv'

    # create graph namedtuple
    Graph = namedtuple('Graph', ['vertices', 'edges'])

    flights_list = scan_csv_file_to_memory(input_file)
    # print(flights_list)
    network = generate_flights_network_graph(flights_list)
    # print(network)
    outbound_adj = convert_to_adjacency_list(network, origin, destination)  # inbound: (flights, destination, origin)
    # print(outbound_adj)
    travel_plans = get_all_possibilities_between_origin_destination(outbound_adj, origin, destination)
    # print(travel_plans)
    for current_travel_plan in travel_plans:
        # print(current_travel_plan)
        fetched_flights = fetch_flights_within_travel_plan(current_travel_plan)
        for flight_found in fetched_flights:
            print(flight_found)
