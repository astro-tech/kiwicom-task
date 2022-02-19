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
