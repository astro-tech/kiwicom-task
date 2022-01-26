import csv
from collections import namedtuple
from graph_traverse import get_all_possibilities_between_origin_destination

# mandatory arguments
origin = 'WIW'
destination = 'RFZ'

# initialize output
output = []

# create graph namedtuple
Graph = namedtuple('Graph', ['vertices', 'edges'])


def convert_to_adjacency_list(graph, start, end):
    output_dictionary = {vertex: [] for vertex in graph.vertices}
    for edge in graph.edges:
        vertex_1, vertex_2 = edge[0], edge[1]
        if vertex_1 != end and vertex_2 != start:   # filter out return flights
            output_dictionary[vertex_1].append(vertex_2)
    return output_dictionary


airports = []   # these are the graph vertices
routes = []   # these are the graph edges
flights_list = []

with open('example/example0.csv', newline='') as csv_file:
    flights = csv.DictReader(csv_file)
    for row in flights:
        flights_list.append(row)
# print(flights_list)

for row in flights_list:
    if row['origin'] not in airports:
        airports.append(row['origin'])
    if row['destination'] not in airports:
        airports.append(row['destination'])
    if (row['origin'], row['destination']) not in routes:
        routes.append((row['origin'], row['destination']))
network = Graph(airports, routes)   # initialize graph object
# print(network)
outbound_adj = convert_to_adjacency_list(network, origin, destination)  # inbound: (flights, destination, origin)
# print(outbound_adj)
travel_plans = get_all_possibilities_between_origin_destination(outbound_adj, origin, destination)
print(travel_plans)

travel_plan0 = travel_plans[0]      # to be iterated
print(travel_plan0)

possible_journeys = {}
leg_counter = 0
for leg in travel_plan0:
    possible_journeys[leg_counter] = []
    current_origin, current_destination = leg[0], leg[1]
    for row in flights_list:
        if row['origin'] == current_origin and row['destination'] == current_destination:
            possible_journeys[leg_counter].append(row)
    leg_counter += 1

print(possible_journeys)


