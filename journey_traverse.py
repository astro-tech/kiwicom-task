travel_plan = [('DHE', 'SML'), ('SML', 'NRX'), ('NRX', 'NIZ'), ('NIZ', 'DHE')]
transfer_lists_3 = {'6DHESML': ['11SMLNRX'],
                    '8DHESML': ['11SMLNRX'],
                    '30DHESML': ['35SMLNRX'],
                    '31DHESML': ['35SMLNRX'],
                    '11SMLNRX': ['15NRXNIZ'],
                    '23SMLNRX': [],
                    '35SMLNRX': [],
                    '1NRXNIZ': ['24NIZDHE', '39NIZDHE'],
                    '15NRXNIZ': ['24NIZDHE', '39NIZDHE'],
                    '22NRXNIZ': ['24NIZDHE', '39NIZDHE']}
transfer_lists_2 = {'6DHESML': ['11SMLNRX', '23SMLNRX'],
                  '8DHESML': ['11SMLNRX'],
                  '30DHESML': ['35SMLNRX'],
                  '31DHESML': ['35SMLNRX'],
                  '11SMLNRX': ['15NRXNIZ', '1NRXNIZ'],
                  '23SMLNRX': ['1NRXNIZ'],
                  '35SMLNRX': [],
                  '1NRXNIZ': ['24NIZDHE', '39NIZDHE'],
                  '15NRXNIZ': ['24NIZDHE', '39NIZDHE'],
                  '22NRXNIZ': ['24NIZDHE', '39NIZDHE']}
graph_starts = ['6DHESML', '8DHESML', '30DHESML', '31DHESML']
travel_plan_length_2 = 4
transfer_lists_1 = {'6DHESML': [], '8DHESML': [], '30DHESML': [], '31DHESML': []}
travel_plan_length_1 = 1
# graph_starts = [128]
# transfer_lists = {128: [163], 163: [195], 195: [222], 222: []}
# travel_plan_length = 5


def transfer_lists_traverse(start_list, adj, desired_length):
    final_id_list = []

    def dfs(vertex):
        nonlocal final_id_list, current_search
        current_search.append(vertex)
        if len(current_search) == desired_length:   # we completed the full path
            final_id_list.append(current_search[:])
            if current_search:      # to avoid pop on empty list error
                current_search.pop()
        else:
            children = adj[vertex]
            for child in children:
                dfs(child)
            if current_search:
                current_search.pop()

    for start in start_list:
        current_search = []  # empty every for loop
        dfs(start)
    return final_id_list


# print(transfer_lists_traverse(graph_starts, transfer_lists, travel_plan_length))
