from datetime import datetime, timedelta

time_1 = '2021-09-01T11:00:00'
time_2 = '2021-09-01T15:00:00'


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
