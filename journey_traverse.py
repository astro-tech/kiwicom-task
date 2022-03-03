def transfer_lists_traverse(start_list, adj, desired_length):
    final_id_list = []
    max_depth = 0

    def dfs(vertex):
        nonlocal final_id_list, current_search, max_depth
        current_search.append(vertex)
        if len(current_search) == desired_length:  # we completed the full path
            max_depth = desired_length
            final_id_list.append(current_search[:])
            if current_search:  # to avoid pop on empty list error
                current_search.pop()
        else:
            children = adj[vertex]
            if children == [] and max_depth < len(current_search) < desired_length:
                max_depth = len(current_search)
            for child in children:
                dfs(child)
            if current_search:
                current_search.pop()

    for start in start_list:
        current_search = []  # empty every for loop
        dfs(start)
    return final_id_list, max_depth
