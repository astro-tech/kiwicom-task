from datetime import datetime, timedelta

empty_time = None
my_now = datetime.now()
print(my_now)
max_allowed = timedelta(hours=0)

print(max_allowed)


# time_1 = '2021-09-01T11:00:00'
# time_2 = '2021-09-01T15:00:00'
#
# my_list = [{'origin': 'WIW', 'destination': 'ECV', 'departure': '2021-09-01T07:25:00', 'arrival': '2021-09-01T11:00:00'},
#            {'origin': 'ECV', 'destination': 'RFZ', 'departure': '2021-09-01T12:10:00', 'arrival': '2021-09-01T14:40:00'},
#            {'origin': 'RFZ', 'destination': 'BUD', 'departure': '2021-09-01T16:10:00', 'arrival': '2021-09-01T18:40:00'},
#            {'origin': 'BUD', 'destination': 'LTN', 'departure': '2021-09-01T20:10:00', 'arrival': '2021-09-01T23:40:00'}]


def check_within_timeframe(reference, compare):
    try:
        reference_time = datetime.strptime(reference, '%Y-%m-%dT%H:%M:%S')
        compare_time = datetime.strptime(compare, '%Y-%m-%dT%H:%M:%S')
    except TypeError:
        return False
    except ValueError:
        return False
    min_allowed = reference_time + timedelta(hours=1)
    max_allowed = reference_time + timedelta(hours=6)
    if min_allowed <= compare_time <= max_allowed:
        return True
    return False


# print(check_within_timeframe(time_1, time_2))

def check_consecutive_flights(list_to_check):
    times_list = []
    for line in list_to_check:
        time_d, time_a = line['departure'], line['arrival']
        times_list.extend([time_d, time_a])
    # print(times_list)
    for i in range(1, len(times_list) - 1, 2):
        # print(i, i + 1)
        if not check_within_timeframe(times_list[i], times_list[i + 1]):
            break
    else:
        return True     # only executed if for loop didn't break
    return False    # only executed if for loop broke


# print(check_consecutive_flights(my_list))
