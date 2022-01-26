import csv
from collections import namedtuple

# mandatory arguments
origin = 'DHE'
destination = 'NIZ'

# initialize output
output = []

# create graph namedtuple
Graph = namedtuple('Graph', ['vertices', 'edges'])

airports = []   # these are the graph vertices
routes = []   # these are the graph edges

with open('example/example1.csv', newline='') as csv_file:
    flights = csv.DictReader(csv_file)
    for row in flights:
        if row['origin'] not in airports:
            airports.append(row['origin'])
        if row['destination'] not in airports:
            airports.append(row['destination'])
        if (row['origin'], row['destination']) not in routes:
            routes.append((row['origin'], row['destination']))

# initialize graph object
flights = Graph(airports, routes)
print(flights)


def convert_to_adjacency_list(graph):
    output_dictionary = {vertex: [] for vertex in graph.vertices}
    for edge in graph.edges:
        vertex_1, vertex_2 = edge[0], edge[1]
        if vertex_1 != destination and vertex_2 != origin:  # filter out return flights, swap dest and orig for return
            output_dictionary[vertex_1].append(vertex_2)
    return output_dictionary


outbound_adj = convert_to_adjacency_list(flights)
print(outbound_adj)



