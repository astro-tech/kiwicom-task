return_adjacency_list = {1: [3, 5, 9, 11, 13, 17, 19, 23], 4: [5, 9, 11, 13, 17, 19, 23], 7: [9, 11, 13, 17, 19, 23], 10: [11, 13, 17, 19, 23], 12: [13, 17, 19, 23], 16: [17, 19, 23], 18: [19, 23], 22: [23]}
fetched_flight_ids = {'out': [[0, 1], [6, 7], [4], [10], [18]], 'in': [[5], [11], [19]]}


def merge_outbound_with_inbound(id_list, adj):
    output_list = []
    for outbound in id_list['out']:
        for inbound in id_list['in']:
            current_list = []
            last_sector_of_current_outbound = outbound[-1]
            first_sector_of_current_inbound = inbound[0]
            if first_sector_of_current_inbound in adj[last_sector_of_current_outbound]:
                for number_1 in outbound:
                    current_list.append(number_1)
                for number_2 in inbound:
                    current_list.append(number_2)
                output_list.append(current_list[:])
    return output_list


# print(merge_outbound_with_inbound(fetched_flight_ids, return_adjacency_list))
