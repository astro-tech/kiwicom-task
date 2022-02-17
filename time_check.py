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
