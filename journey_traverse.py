# my_adj = {
#     96: [136, 58],
#     196: [],
#     206: [],
#     207: [],
#     291: [],
#     294: [318],
#     379: [],
#     431: [],
#     443: [],
#     541: [],
#     577: [],
#     585: [],
#     671: [],
#     674: [],
#     58: [101],
#     108: [],
#     136: [],
#     171: [],
#     263: [],
#     318: [],
#     334: [],
#     384: [],
#     483: [],
#     499: [],
#     545: [],
#     642: [],
#     653: [],
#     101: [152],
#     111: [152],
#     193: [],
#     215: [],
#     259: [],
#     289: [],
#     354: [367],
#     429: [],
#     445: [],
#     493: [],
#     575: [],
#     588: [],
#     650: [],
#     670: [],
#     42: [],
#     152: [184, 186],
#     185: [],
#     197: [],
#     285: [],
#     345: [],
#     367: [],
#     421: [],
#     512: [],
#     529: [],
#     569: [],
#     666: [],
#     55: [],
#     170: [194, 146],
#     184: [],
#     186: [],
#     284: [],
#     286: [],
#     370: [],
#     420: [],
#     423: [],
#     532: [],
#     568: [],
#     571: [],
#     665: [],
#     667: [],
#     37: [],
#     146: [168],
#     158: [],
#     194: [],
#     321: [333],
#     324: [],
#     344: [],
#     474: [],
#     501: [],
#     511: [],
#     634: []}
# my_start_list = [96, 196, 206, 207, 291, 294, 379, 431, 443, 541, 577, 585, 671, 674]
# my_desired_length = 7
my_adj = {4: [], 17: [22], 28: [], 40: [44], 52: [], 64: [68], 78: []}
my_start_list = [4, 17, 28, 40, 52, 64, 78]
my_desired_length = 2


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


# print(transfer_lists_traverse(my_start_list, my_adj, my_desired_length))
