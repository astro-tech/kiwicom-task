# note01: https://stackoverflow.com/questions/5280799/list-append-changing-all-elements-to-the-appended-item

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
            if max_transfer or max_transfer == 0:    # max transfer might not be limited and have None or 0 value
                if len(current_search) < max_transfer + 2:      # e.g: 4 legs are 3 transfers
                    possibilities.append(current_search[:])   # current_search is copied not just referenced, see note01
            else:
                possibilities.append(current_search[:])
            if current_search:      # to avoid pop on empty list error
                current_search.pop()
            visited[vertex] = False     # destination can be visited again in another branch
        else:
            # print('current_vertex: ' + vertex)
            children = adj[vertex]
            # print(children)
            for child in children:
                # print('current_child: ' + child)
                if not visited[child]:      # to avoid visiting vertex in same branch
                    # print('appending')
                    current_search.append((vertex, child))  # register current dfs leg
                    dfs(child)  # recursive
            if current_search:      # to avoid pop on empty list error
                current_search.pop()     # avoid register dead end tree as solution
            visited[vertex] = False     # current vertex can be visited again in another branch

    dfs(start)

    return possibilities
