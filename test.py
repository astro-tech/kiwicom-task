# note01: https://stackoverflow.com/questions/5280799/list-append-changing-all-elements-to-the-appended-item
adjacency_list_3 = {'WIW': ['XXX', 'ECV', 'RFZ'], 'ECV': ['RFZ', 'XXX'], 'RFZ': [], 'XXX': []}
origin_3 = 'WIW'
destination_3 = 'RFZ'
adjacency_list_4 = {'DHE': ['NIZ', 'NRX', 'SML'], 'NIZ': [], 'NRX': ['NIZ', 'SML', 'XXX'], 'SML': ['NRX', 'NIZ'], 'XXX': []}
origin_4 = 'DHE'
destination_4 = 'NIZ'


def get_all_possibilities_between_origin_destination(adj, start, end):
    possibilities = []
    current_search = []
    visited = {key: False for key in adj}
    # counter = 0

    def dfs(vertex):    # performing a depth first search, this is more representative for a journey than bfs
        # nonlocal counter
        # counter += 1
        # print('dfs_called#' + str(counter))
        nonlocal current_search     # to access outer namespace
        visited[vertex] = True
        if vertex == end:   # searching reached end on current branch
            # print('reached end')
            possibilities.append(current_search[:])   # current_search is copied not just referenced, see note01
            if current_search:      # to avoid pop on empty list error
                current_search.pop()
            visited[vertex] = False     # destination can be visited again in another branch
            # return
        else:
            # print('current_vertex: ' + vertex)
            children = adj[vertex]
            # print(children)
            for child in children:
                # print('current_child: ' + child)
                if not visited[child]:      # to avoid visiting vertex in same branch
                    # print('appendeles')
                    current_search.append((vertex, child))  # register current dfs leg
                    dfs(child)  # recursive
            if current_search:      # to avoid pop on empty list error
                current_search.pop()     # avoid register dead end tree as solution
            visited[vertex] = False     # current vertex can be visited again in another branch

    dfs(start)

    return possibilities


# print(get_all_possibilities_between_origin_destination(adjacency_list_3, origin_3, destination_3))
print(get_all_possibilities_between_origin_destination(adjacency_list_4, origin_4, destination_4))

