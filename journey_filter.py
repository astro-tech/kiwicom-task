from time_check import check_consecutive_flights

a = {0: [
{'flight_no': 'CC742', 'origin': 'ZRW', 'destination': 'WTN', 'departure': '2021-09-01T06:55:00', 'arrival': '2021-09-01T10:35:00', 'base_price': 95.0, 'bag_price': 9.0, 'bags_allowed': 2},
{'flight_no': 'JT106', 'origin': 'ZRW', 'destination': 'WTN', 'departure': '2021-09-15T13:20:00', 'arrival': '2021-09-15T17:00:00', 'base_price': 98.0, 'bag_price': 11.0, 'bags_allowed': 2}],
1: [
{'flight_no': 'CC118', 'origin': 'WTN', 'destination': 'VVH', 'departure': '2021-09-01T13:25:00', 'arrival': '2021-09-01T18:10:00', 'base_price': 193.0, 'bag_price': 9.0, 'bags_allowed': 2},
{'flight_no': 'YL244', 'origin': 'WTN', 'destination': 'VVH', 'departure': '2021-09-16T04:05:00', 'arrival': '2021-09-16T08:50:00', 'base_price': 189.0, 'bag_price': 10.0, 'bags_allowed': 2}],
2: [
{'flight_no': 'JT512', 'origin': 'VVH', 'destination': 'NNB', 'departure': '2021-09-01T12:45:00', 'arrival': '2021-09-01T14:35:00', 'base_price': 27.0, 'bag_price': 11.0, 'bags_allowed': 1},
{'flight_no': 'YL591', 'origin': 'VVH', 'destination': 'NNB', 'departure': '2021-09-18T14:45:00', 'arrival': '2021-09-18T16:35:00', 'base_price': 30.0, 'bag_price': 10.0, 'bags_allowed': 1}],
3: [
{'flight_no': 'JT459', 'origin': 'NNB', 'destination': 'JBN', 'departure': '2021-09-01T04:00:00', 'arrival': '2021-09-01T06:05:00', 'base_price': 33.0, 'bag_price': 11.0, 'bags_allowed': 1},
{'flight_no': 'JT459', 'origin': 'NNB', 'destination': 'JBN', 'departure': '2021-09-02T04:00:00', 'arrival': '2021-09-02T06:05:00', 'base_price': 33.0, 'bag_price': 11.0, 'bags_allowed': 1},
{'flight_no': 'YL596', 'origin': 'NNB', 'destination': 'JBN', 'departure': '2021-09-02T06:35:00', 'arrival': '2021-09-02T08:40:00', 'base_price': 16.0, 'bag_price': 10.0, 'bags_allowed': 2},
{'flight_no': 'CC753', 'origin': 'NNB', 'destination': 'JBN', 'departure': '2021-09-02T14:10:00', 'arrival': '2021-09-02T16:15:00', 'base_price': 53.0, 'bag_price': 9.0, 'bags_allowed': 2},
{'flight_no': 'JT459', 'origin': 'NNB', 'destination': 'JBN', 'departure': '2021-09-05T04:00:00', 'arrival': '2021-09-05T06:05:00', 'base_price': 33.0, 'bag_price': 11.0, 'bags_allowed': 1},
{'flight_no': 'YL596', 'origin': 'NNB', 'destination': 'JBN', 'departure': '2021-09-05T06:35:00', 'arrival': '2021-09-05T08:40:00', 'base_price': 16.0, 'bag_price': 10.0, 'bags_allowed': 2},
{'flight_no': 'CC753', 'origin': 'NNB', 'destination': 'JBN', 'departure': '2021-09-05T14:10:00', 'arrival': '2021-09-05T16:15:00', 'base_price': 53.0, 'bag_price': 9.0, 'bags_allowed': 2},
{'flight_no': 'JT459', 'origin': 'NNB', 'destination': 'JBN', 'departure': '2021-09-09T04:00:00', 'arrival': '2021-09-09T06:05:00', 'base_price': 33.0, 'bag_price': 11.0, 'bags_allowed': 1},
{'flight_no': 'YL596', 'origin': 'NNB', 'destination': 'JBN', 'departure': '2021-09-10T06:35:00', 'arrival': '2021-09-10T08:40:00', 'base_price': 16.0, 'bag_price': 10.0, 'bags_allowed': 2},
{'flight_no': 'CC753', 'origin': 'NNB', 'destination': 'JBN', 'departure': '2021-09-10T14:10:00', 'arrival': '2021-09-10T16:15:00', 'base_price': 53.0, 'bag_price': 9.0, 'bags_allowed': 2},
{'flight_no': 'JT459', 'origin': 'NNB', 'destination': 'JBN', 'departure': '2021-09-15T04:00:00', 'arrival': '2021-09-15T06:05:00', 'base_price': 33.0, 'bag_price': 11.0, 'bags_allowed': 1}],
4: [
{'flight_no': 'CC515', 'origin': 'JBN', 'destination': 'WUE', 'departure': '2021-09-01T03:55:00', 'arrival': '2021-09-01T05:05:00', 'base_price': 18.0, 'bag_price': 9.0, 'bags_allowed': 2},
{'flight_no': 'JT808', 'origin': 'JBN', 'destination': 'WUE', 'departure': '2021-09-01T06:15:00', 'arrival': '2021-09-01T07:25:00', 'base_price': 36.0, 'bag_price': 11.0, 'bags_allowed': 2},
{'flight_no': 'CC515', 'origin': 'JBN', 'destination': 'WUE', 'departure': '2021-09-02T03:55:00', 'arrival': '2021-09-02T05:05:00', 'base_price': 18.0, 'bag_price': 9.0, 'bags_allowed': 2},
{'flight_no': 'YL320', 'origin': 'JBN', 'destination': 'WUE', 'departure': '2021-09-02T16:30:00', 'arrival': '2021-09-02T17:40:00', 'base_price': 2.0, 'bag_price': 10.0, 'bags_allowed': 2},
{'flight_no': 'JT808', 'origin': 'JBN', 'destination': 'WUE', 'departure': '2021-09-03T06:15:00', 'arrival': '2021-09-03T07:25:00', 'base_price': 36.0, 'bag_price': 11.0, 'bags_allowed': 2},
{'flight_no': 'CC515', 'origin': 'JBN', 'destination': 'WUE', 'departure': '2021-09-05T03:55:00', 'arrival': '2021-09-05T05:05:00', 'base_price': 18.0, 'bag_price': 9.0, 'bags_allowed': 2},
{'flight_no': 'YL320', 'origin': 'JBN', 'destination': 'WUE', 'departure': '2021-09-05T16:30:00', 'arrival': '2021-09-05T17:40:00', 'base_price': 2.0, 'bag_price': 10.0, 'bags_allowed': 2},
{'flight_no': 'JT808', 'origin': 'JBN', 'destination': 'WUE', 'departure': '2021-09-07T06:15:00', 'arrival': '2021-09-07T07:25:00', 'base_price': 36.0, 'bag_price': 11.0, 'bags_allowed': 2},
{'flight_no': 'CC515', 'origin': 'JBN', 'destination': 'WUE', 'departure': '2021-09-09T03:55:00', 'arrival': '2021-09-09T05:05:00', 'base_price': 18.0, 'bag_price': 9.0, 'bags_allowed': 2},
{'flight_no': 'YL320', 'origin': 'JBN', 'destination': 'WUE', 'departure': '2021-09-10T16:30:00', 'arrival': '2021-09-10T17:40:00', 'base_price': 2.0, 'bag_price': 10.0, 'bags_allowed': 2},
{'flight_no': 'JT808', 'origin': 'JBN', 'destination': 'WUE', 'departure': '2021-09-13T06:15:00', 'arrival': '2021-09-13T07:25:00', 'base_price': 36.0, 'bag_price': 11.0, 'bags_allowed': 2},
{'flight_no': 'CC515', 'origin': 'JBN', 'destination': 'WUE', 'departure': '2021-09-15T03:55:00', 'arrival': '2021-09-15T05:05:00', 'base_price': 18.0, 'bag_price': 9.0, 'bags_allowed': 2}],
5: [
{'flight_no': 'JT755', 'origin': 'WUE', 'destination': 'EZO', 'departure': '2021-09-01T02:55:00', 'arrival': '2021-09-01T06:10:00', 'base_price': 76.0, 'bag_price': 11.0, 'bags_allowed': 1},
{'flight_no': 'CC156', 'origin': 'WUE', 'destination': 'EZO', 'departure': '2021-09-01T03:30:00', 'arrival': '2021-09-01T06:45:00', 'base_price': 64.0, 'bag_price': 9.0, 'bags_allowed': 2},
{'flight_no': 'YL839', 'origin': 'WUE', 'destination': 'EZO', 'departure': '2021-09-01T21:25:00', 'arrival': '2021-09-02T00:40:00', 'base_price': 91.0, 'bag_price': 10.0, 'bags_allowed': 1},
{'flight_no': 'JT755', 'origin': 'WUE', 'destination': 'EZO', 'departure': '2021-09-02T02:55:00', 'arrival': '2021-09-02T06:10:00', 'base_price': 76.0, 'bag_price': 11.0, 'bags_allowed': 1},
{'flight_no': 'CC156', 'origin': 'WUE', 'destination': 'EZO', 'departure': '2021-09-03T03:30:00', 'arrival': '2021-09-03T06:45:00', 'base_price': 64.0, 'bag_price': 9.0, 'bags_allowed': 2},
{'flight_no': 'YL839', 'origin': 'WUE', 'destination': 'EZO', 'departure': '2021-09-03T21:25:00', 'arrival': '2021-09-04T00:40:00', 'base_price': 91.0, 'bag_price': 10.0, 'bags_allowed': 1},
{'flight_no': 'JT755', 'origin': 'WUE', 'destination': 'EZO', 'departure': '2021-09-05T02:55:00', 'arrival': '2021-09-05T06:10:00', 'base_price': 76.0, 'bag_price': 11.0, 'bags_allowed': 1},
{'flight_no': 'CC156', 'origin': 'WUE', 'destination': 'EZO', 'departure': '2021-09-07T03:30:00', 'arrival': '2021-09-07T06:45:00', 'base_price': 64.0, 'bag_price': 9.0, 'bags_allowed': 2},
{'flight_no': 'YL839', 'origin': 'WUE', 'destination': 'EZO', 'departure': '2021-09-07T21:25:00', 'arrival': '2021-09-08T00:40:00', 'base_price': 91.0, 'bag_price': 10.0, 'bags_allowed': 1},
{'flight_no': 'JT755', 'origin': 'WUE', 'destination': 'EZO', 'departure': '2021-09-09T02:55:00', 'arrival': '2021-09-09T06:10:00', 'base_price': 76.0, 'bag_price': 11.0, 'bags_allowed': 1},
{'flight_no': 'CC156', 'origin': 'WUE', 'destination': 'EZO', 'departure': '2021-09-13T03:30:00', 'arrival': '2021-09-13T06:45:00', 'base_price': 64.0, 'bag_price': 9.0, 'bags_allowed': 2},
{'flight_no': 'YL839', 'origin': 'WUE', 'destination': 'EZO', 'departure': '2021-09-13T21:25:00', 'arrival': '2021-09-14T00:40:00', 'base_price': 91.0, 'bag_price': 10.0, 'bags_allowed': 1},
{'flight_no': 'JT755', 'origin': 'WUE', 'destination': 'EZO', 'departure': '2021-09-15T02:55:00', 'arrival': '2021-09-15T06:10:00', 'base_price': 76.0, 'bag_price': 11.0, 'bags_allowed': 1}],
6: [
{'flight_no': 'JT547', 'origin': 'EZO', 'destination': 'BPZ', 'departure': '2021-09-01T20:55:00', 'arrival': '2021-09-02T00:25:00', 'base_price': 92.0, 'bag_price': 11.0, 'bags_allowed': 2},
{'flight_no': 'CC813', 'origin': 'EZO', 'destination': 'BPZ', 'departure': '2021-09-02T03:00:00', 'arrival': '2021-09-02T06:30:00', 'base_price': 76.0, 'bag_price': 9.0, 'bags_allowed': 2},
{'flight_no': 'YL193', 'origin': 'EZO', 'destination': 'BPZ', 'departure': '2021-09-02T23:35:00', 'arrival': '2021-09-03T03:05:00', 'base_price': 114.0, 'bag_price': 10.0, 'bags_allowed': 2},
{'flight_no': 'JT547', 'origin': 'EZO', 'destination': 'BPZ', 'departure': '2021-09-03T20:55:00', 'arrival': '2021-09-04T00:25:00', 'base_price': 92.0, 'bag_price': 11.0, 'bags_allowed': 2},
{'flight_no': 'CC813', 'origin': 'EZO', 'destination': 'BPZ', 'departure': '2021-09-04T03:00:00', 'arrival': '2021-09-04T06:30:00', 'base_price': 76.0, 'bag_price': 9.0, 'bags_allowed': 2},
{'flight_no': 'YL193', 'origin': 'EZO', 'destination': 'BPZ', 'departure': '2021-09-05T23:35:00', 'arrival': '2021-09-06T03:05:00', 'base_price': 114.0, 'bag_price': 10.0, 'bags_allowed': 2},
{'flight_no': 'JT547', 'origin': 'EZO', 'destination': 'BPZ', 'departure': '2021-09-07T20:55:00', 'arrival': '2021-09-08T00:25:00', 'base_price': 92.0, 'bag_price': 11.0, 'bags_allowed': 2},
{'flight_no': 'CC813', 'origin': 'EZO', 'destination': 'BPZ', 'departure': '2021-09-08T03:00:00', 'arrival': '2021-09-08T06:30:00', 'base_price': 76.0, 'bag_price': 9.0, 'bags_allowed': 2},
{'flight_no': 'YL193', 'origin': 'EZO', 'destination': 'BPZ', 'departure': '2021-09-10T23:35:00', 'arrival': '2021-09-11T03:05:00', 'base_price': 114.0, 'bag_price': 10.0, 'bags_allowed': 2},
{'flight_no': 'JT547', 'origin': 'EZO', 'destination': 'BPZ', 'departure': '2021-09-12T20:55:00', 'arrival': '2021-09-13T00:25:00', 'base_price': 92.0, 'bag_price': 11.0, 'bags_allowed': 2},
{'flight_no': 'CC813', 'origin': 'EZO', 'destination': 'BPZ', 'departure': '2021-09-13T03:00:00', 'arrival': '2021-09-13T06:30:00', 'base_price': 76.0, 'bag_price': 9.0, 'bags_allowed': 2}]}


b = {0: [
{'flight_no': 'CC742', 'origin': 'ZRW', 'destination': 'WTN', 'departure': '2021-09-01T06:55:00', 'arrival': '2021-09-01T10:35:00', 'base_price': 95.0, 'bag_price': 9.0, 'bags_allowed': 2},
{'flight_no': 'YL336', 'origin': 'ZRW', 'destination': 'WTN', 'departure': '2021-09-01T08:55:00', 'arrival': '2021-09-01T12:35:00', 'base_price': 115.0, 'bag_price': 10.0, 'bags_allowed': 2},
{'flight_no': 'JT106', 'origin': 'ZRW', 'destination': 'WTN', 'departure': '2021-09-01T13:20:00', 'arrival': '2021-09-01T17:00:00', 'base_price': 98.0, 'bag_price': 11.0, 'bags_allowed': 2},
{'flight_no': 'CC742', 'origin': 'ZRW', 'destination': 'WTN', 'departure': '2021-09-02T06:55:00', 'arrival': '2021-09-02T10:35:00', 'base_price': 95.0, 'bag_price': 9.0, 'bags_allowed': 2},
{'flight_no': 'YL336', 'origin': 'ZRW', 'destination': 'WTN', 'departure': '2021-09-02T08:55:00', 'arrival': '2021-09-02T12:35:00', 'base_price': 115.0, 'bag_price': 10.0, 'bags_allowed': 2},
{'flight_no': 'JT106', 'origin': 'ZRW', 'destination': 'WTN', 'departure': '2021-09-02T13:20:00', 'arrival': '2021-09-02T17:00:00', 'base_price': 98.0, 'bag_price': 11.0, 'bags_allowed': 2},
{'flight_no': 'JT106', 'origin': 'ZRW', 'destination': 'WTN', 'departure': '2021-09-05T13:20:00', 'arrival': '2021-09-05T17:00:00', 'base_price': 98.0, 'bag_price': 11.0, 'bags_allowed': 2},
{'flight_no': 'CC742', 'origin': 'ZRW', 'destination': 'WTN', 'departure': '2021-09-06T06:55:00', 'arrival': '2021-09-06T10:35:00', 'base_price': 95.0, 'bag_price': 9.0, 'bags_allowed': 2},
{'flight_no': 'YL336', 'origin': 'ZRW', 'destination': 'WTN', 'departure': '2021-09-06T08:55:00', 'arrival': '2021-09-06T12:35:00', 'base_price': 115.0, 'bag_price': 10.0, 'bags_allowed': 2},
{'flight_no': 'JT106', 'origin': 'ZRW', 'destination': 'WTN', 'departure': '2021-09-09T13:20:00', 'arrival': '2021-09-09T17:00:00', 'base_price': 98.0, 'bag_price': 11.0, 'bags_allowed': 2},
{'flight_no': 'CC742', 'origin': 'ZRW', 'destination': 'WTN', 'departure': '2021-09-11T06:55:00', 'arrival': '2021-09-11T10:35:00', 'base_price': 95.0, 'bag_price': 9.0, 'bags_allowed': 2},
{'flight_no': 'YL336', 'origin': 'ZRW', 'destination': 'WTN', 'departure': '2021-09-11T08:55:00', 'arrival': '2021-09-11T12:35:00', 'base_price': 115.0, 'bag_price': 10.0, 'bags_allowed': 2},
{'flight_no': 'JT106', 'origin': 'ZRW', 'destination': 'WTN', 'departure': '2021-09-15T13:20:00', 'arrival': '2021-09-15T17:00:00', 'base_price': 98.0, 'bag_price': 11.0, 'bags_allowed': 2}],
1: [
{'flight_no': 'CC118', 'origin': 'WTN', 'destination': 'VVH', 'departure': '2021-09-01T13:25:00', 'arrival': '2021-09-01T18:10:00', 'base_price': 193.0, 'bag_price': 9.0, 'bags_allowed': 2},
{'flight_no': 'YL244', 'origin': 'WTN', 'destination': 'VVH', 'departure': '2021-09-02T04:05:00', 'arrival': '2021-09-02T08:50:00', 'base_price': 189.0, 'bag_price': 10.0, 'bags_allowed': 2},
{'flight_no': 'CC118', 'origin': 'WTN', 'destination': 'VVH', 'departure': '2021-09-02T13:25:00', 'arrival': '2021-09-02T18:10:00', 'base_price': 193.0, 'bag_price': 9.0, 'bags_allowed': 2},
{'flight_no': 'JT226', 'origin': 'WTN', 'destination': 'VVH', 'departure': '2021-09-03T00:45:00', 'arrival': '2021-09-03T05:30:00', 'base_price': 188.0, 'bag_price': 11.0, 'bags_allowed': 2},
{'flight_no': 'YL244', 'origin': 'WTN', 'destination': 'VVH', 'departure': '2021-09-03T04:05:00', 'arrival': '2021-09-03T08:50:00', 'base_price': 189.0, 'bag_price': 10.0, 'bags_allowed': 2},
{'flight_no': 'CC118', 'origin': 'WTN', 'destination': 'VVH', 'departure': '2021-09-05T13:25:00', 'arrival': '2021-09-05T18:10:00', 'base_price': 193.0, 'bag_price': 9.0, 'bags_allowed': 2},
{'flight_no': 'JT226', 'origin': 'WTN', 'destination': 'VVH', 'departure': '2021-09-06T00:45:00', 'arrival': '2021-09-06T05:30:00', 'base_price': 188.0, 'bag_price': 11.0, 'bags_allowed': 2},
{'flight_no': 'YL244', 'origin': 'WTN', 'destination': 'VVH', 'departure': '2021-09-06T04:05:00', 'arrival': '2021-09-06T08:50:00', 'base_price': 189.0, 'bag_price': 10.0, 'bags_allowed': 2},
{'flight_no': 'CC118', 'origin': 'WTN', 'destination': 'VVH', 'departure': '2021-09-09T13:25:00', 'arrival': '2021-09-09T18:10:00', 'base_price': 193.0, 'bag_price': 9.0, 'bags_allowed': 2},
{'flight_no': 'YL244', 'origin': 'WTN', 'destination': 'VVH', 'departure': '2021-09-10T04:05:00', 'arrival': '2021-09-10T08:50:00', 'base_price': 189.0, 'bag_price': 10.0, 'bags_allowed': 2},
{'flight_no': 'JT226', 'origin': 'WTN', 'destination': 'VVH', 'departure': '2021-09-11T00:45:00', 'arrival': '2021-09-11T05:30:00', 'base_price': 188.0, 'bag_price': 11.0, 'bags_allowed': 2},
{'flight_no': 'CC118', 'origin': 'WTN', 'destination': 'VVH', 'departure': '2021-09-15T13:25:00', 'arrival': '2021-09-15T18:10:00', 'base_price': 193.0, 'bag_price': 9.0, 'bags_allowed': 2},
{'flight_no': 'YL244', 'origin': 'WTN', 'destination': 'VVH', 'departure': '2021-09-16T04:05:00', 'arrival': '2021-09-16T08:50:00', 'base_price': 189.0, 'bag_price': 10.0, 'bags_allowed': 2}],
2: [
{'flight_no': 'CC229', 'origin': 'VVH', 'destination': 'BPZ', 'departure': '2021-09-01T10:15:00', 'arrival': '2021-09-01T14:30:00', 'base_price': 126.0, 'bag_price': 9.0, 'bags_allowed': 2},
{'flight_no': 'YL311', 'origin': 'VVH', 'destination': 'BPZ', 'departure': '2021-09-01T17:30:00', 'arrival': '2021-09-01T21:45:00', 'base_price': 147.0, 'bag_price': 10.0, 'bags_allowed': 2},
{'flight_no': 'CC229', 'origin': 'VVH', 'destination': 'BPZ', 'departure': '2021-09-02T10:15:00', 'arrival': '2021-09-02T14:30:00', 'base_price': 126.0, 'bag_price': 9.0, 'bags_allowed': 2},
{'flight_no': 'YL311', 'origin': 'VVH', 'destination': 'BPZ', 'departure': '2021-09-02T17:30:00', 'arrival': '2021-09-02T21:45:00', 'base_price': 147.0, 'bag_price': 10.0, 'bags_allowed': 2},
{'flight_no': 'JT107', 'origin': 'VVH', 'destination': 'BPZ', 'departure': '2021-09-02T19:10:00', 'arrival': '2021-09-02T23:25:00', 'base_price': 156.0, 'bag_price': 11.0, 'bags_allowed': 2},
{'flight_no': 'JT107', 'origin': 'VVH', 'destination': 'BPZ', 'departure': '2021-09-04T19:10:00', 'arrival': '2021-09-04T23:25:00', 'base_price': 156.0, 'bag_price': 11.0, 'bags_allowed': 2},
{'flight_no': 'CC229', 'origin': 'VVH', 'destination': 'BPZ', 'departure': '2021-09-05T10:15:00', 'arrival': '2021-09-05T14:30:00', 'base_price': 126.0, 'bag_price': 9.0, 'bags_allowed': 2},
{'flight_no': 'YL311', 'origin': 'VVH', 'destination': 'BPZ', 'departure': '2021-09-06T17:30:00', 'arrival': '2021-09-06T21:45:00', 'base_price': 147.0, 'bag_price': 10.0, 'bags_allowed': 2},
{'flight_no': 'JT107', 'origin': 'VVH', 'destination': 'BPZ', 'departure': '2021-09-07T19:10:00', 'arrival': '2021-09-07T23:25:00', 'base_price': 156.0, 'bag_price': 11.0, 'bags_allowed': 2},
{'flight_no': 'CC229', 'origin': 'VVH', 'destination': 'BPZ', 'departure': '2021-09-09T10:15:00', 'arrival': '2021-09-09T14:30:00', 'base_price': 126.0, 'bag_price': 9.0, 'bags_allowed': 2},
{'flight_no': 'YL311', 'origin': 'VVH', 'destination': 'BPZ', 'departure': '2021-09-11T17:30:00', 'arrival': '2021-09-11T21:45:00', 'base_price': 147.0, 'bag_price': 10.0, 'bags_allowed': 2},
{'flight_no': 'JT107', 'origin': 'VVH', 'destination': 'BPZ', 'departure': '2021-09-12T19:10:00', 'arrival': '2021-09-12T23:25:00', 'base_price': 156.0, 'bag_price': 11.0, 'bags_allowed': 2},
{'flight_no': 'CC229', 'origin': 'VVH', 'destination': 'BPZ', 'departure': '2021-09-15T10:15:00', 'arrival': '2021-09-15T14:30:00', 'base_price': 126.0, 'bag_price': 9.0, 'bags_allowed': 2},
{'flight_no': 'JT107', 'origin': 'VVH', 'destination': 'BPZ', 'departure': '2021-09-18T19:10:00', 'arrival': '2021-09-18T23:25:00', 'base_price': 156.0, 'bag_price': 11.0, 'bags_allowed': 2}]}

c = {0: [
{'origin': 'ZRW', 'destination': 'WTN', 'departure': '2021-09-01T06:55:00', 'arrival': '2021-09-01T10:35:00'},
{'origin': 'ZRW', 'destination': 'WTN', 'departure': '2021-09-15T13:20:00', 'arrival': '2021-09-15T17:00:00'}],
1: [
{'origin': 'WTN', 'destination': 'VVH', 'departure': '2021-09-01T13:25:00', 'arrival': '2021-09-01T18:10:00'},
{'origin': 'WTN', 'destination': 'VVH', 'departure': '2021-09-16T04:05:00', 'arrival': '2021-09-16T08:50:00'}],
2: [
{'origin': 'VVH', 'destination': 'BPZ', 'departure': '2021-09-01T10:15:00', 'arrival': '2021-09-01T14:30:00'},
{'origin': 'VVH', 'destination': 'BPZ', 'departure': '2021-09-18T19:10:00', 'arrival': '2021-09-18T23:25:00'}]}


def discover_all_combinations(flights_dict, destination):
    legs_count = len(flights_dict) - 1
    present_solution = []
    solutions = []
    counter = 0
    counter_spec = 1

    def inner_loop(ways):
        nonlocal counter, present_solution, counter_spec
        for row in ways:
            present_solution.append(row)
            # print(present_solution)
            if counter == legs_count:   # reached bottom level
                # print(counter_spec)
                counter_spec += 1
                print(present_solution)
                if check_consecutive_flights(present_solution, destination):   # original part without return search
                    solutions.append(present_solution[:])
                if present_solution:
                    present_solution.pop()
            elif counter < legs_count:    # this could be elif?
                counter += 1
                inner_loop(flights_dict[counter])
        counter -= 1
        if present_solution:
            present_solution.pop()

    inner_loop(flights_dict[counter])
    # print(counter_spec)
    return solutions


# paths = discover_all_combinations(c, 'BPZ')
# for i in range(7):
#     print(len(a[i]))
"""
def discover_roundtrip_combinations(flights_dict):
    present_solution = []
    solutions = []
    counter = 0

    def inner_loop(ways):
        nonlocal counter, present_solution
        for row in ways:
            present_solution.append(row)
            if counter == 1:   # trip back home
                solutions.append(present_solution[:])
                if present_solution:
                    present_solution.pop()
            elif counter == 0:    # this could be elif?
                counter += 1
                inner_loop(flights_dict[counter])
        counter -= 1
        if present_solution:
            present_solution.pop()

    inner_loop(flights_dict[counter])
    return solutions"""