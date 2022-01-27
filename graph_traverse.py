# note01: https://stackoverflow.com/questions/5280799/list-append-changing-all-elements-to-the-appended-item
# adjacency_list_3 = {'WIW': ['XXX', 'ECV', 'RFZ'], 'ECV': ['RFZ', 'XXX'], 'RFZ': [], 'XXX': []}
# origin_3 = 'WIW'
# destination_3 = 'RFZ'
# adjacency_list_4 = {'DHE': ['NIZ', 'NRX', 'SML'], 'NIZ': [], 'NRX': ['NIZ', 'SML', 'XXX'], 'SML': ['NRX', 'NIZ'], 'XXX': []}
# origin_4 = 'DHE'
# destination_4 = 'NIZ'
# adjacency_list_5 = {'YOT': ['IUQ', 'IUT', 'LOM', 'GXV'], 'IUQ': [], 'GXV': ['IUQ', 'IUT', 'LOM', 'XXX'], 'IUT': ['GXV', 'IUQ', 'LOM'], 'LOM': ['IUT', 'GXV'], 'XXX': []}
# origin_5 = 'YOT'
# destination_5 = 'IUQ'
# adjacency_list_4r = {'DHE': [], 'NIZ': ['DHE', 'NRX', 'SML'], 'NRX': ['SML', 'DHE'], 'SML': ['NRX', 'DHE']}
# origin_4r = 'NIZ'
# destination_4r = 'DHE'


def get_all_possibilities_between_origin_destination(adj, start, end, max_transfer):
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
            if len(current_search) < max_transfer + 2:      # e.g: 4 legs are 3 transfers
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


# result1 = get_all_possibilities_between_origin_destination(adjacency_list_3, origin_3, destination_3)
# result2 = get_all_possibilities_between_origin_destination(adjacency_list_4, origin_4, destination_4)
# result3 = get_all_possibilities_between_origin_destination(adjacency_list_4r, origin_4r, destination_4r)
# result4 = get_all_possibilities_between_origin_destination(adjacency_list_5, origin_5, destination_5, 1)
# count = 1
# for i in result4:
#     print(count, end=': ')
#     print(i)
#     count += 1

