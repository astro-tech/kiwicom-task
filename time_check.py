from datetime import datetime, timedelta


def check_within_timeframe(reference, compare, layover):
    reference_time = datetime.strptime(reference, '%Y-%m-%dT%H:%M:%S')
    compare_time = datetime.strptime(compare, '%Y-%m-%dT%H:%M:%S')
    min_allowed = reference_time + timedelta(hours=1)
    max_allowed = reference_time + timedelta(hours=6)
    if layover:
        if min_allowed < compare_time:       # in case of layover the only limit is flight2 is after flight1 + 1hour
            return True
    else:
        if min_allowed <= compare_time <= max_allowed:
            return True
    return False


def check_consecutive_flights(list_to_check, destination):  # destination used for return flight check
    times_list = []
    for line in list_to_check:
        time_d, time_a = line['departure'], line['arrival']
        times_list.extend([time_d, time_a])
    # print(times_list)
    for i in range(1, len(times_list) - 1, 2):
        # print(i, i + 1)
        previous_sector = int(i / 2 - 0.5)
        if list_to_check[previous_sector]['destination'] == destination:    # to prevent the 1-6hours limit for layover
            layover = True
        else:
            layover = False
        if not check_within_timeframe(times_list[i], times_list[i + 1], layover):
            break
    else:
        return True     # only executed if for loop didn't break
    return False    # only executed if for loop broke
