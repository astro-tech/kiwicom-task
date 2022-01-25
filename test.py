my_adjacency_list = {'WIW': ['ECV', 'RFZ'], 'ECV': ['RFZ'], 'RFZ': []}
origin = 'WIW'
destination = 'RFZ'


def get_all_possibilities_between_origin_destination(adj, start, end):
    global current_search
    possibilities = []
    current_search = []
    visited = {key: False for key in my_adjacency_list}

    def dfs(vertex, parent):    # performing a depth first search
        global current_search
        if vertex == end:
            possibilities.append(current_search)
            current_search = []
            visited[vertex] = False
            return
        else:
            children = adj[vertex]
            for child in children:
                if not visited[child]:
                    visited[child] = True
                    current_search.append((vertex, child))
                    dfs(child, vertex)  # recursive
            visited[vertex] = False

    visited[start] = True
    dfs(start, start)

    return possibilities


print(get_all_possibilities_between_origin_destination(my_adjacency_list, origin, destination))

