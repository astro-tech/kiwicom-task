from time_check import check_consecutive_flights

# flights search examples within current itinerary
# possible_journeys = \
#     {0: [{'origin': 'WIW', 'destination': 'ECV', 'departure': '2021-09-01T07:25:00', 'arrival': '2021-09-01T11:00:00'},
#         {'origin': 'WIW', 'destination': 'ECV', 'departure': '2021-09-02T07:25:00', 'arrival': '2021-09-02T11:00:00'}],
#      1: [{'origin': 'ECV', 'destination': 'RFZ', 'departure': '2021-09-01T12:10:00', 'arrival': '2021-09-01T14:40:00'},
#          {'origin': 'ECV', 'destination': 'RFZ', 'departure': '2021-09-01T12:20:00', 'arrival': '2021-09-01T14:50:00'}],
#      2: [{'origin': 'RFZ', 'destination': 'BUD', 'departure': '2021-09-01T19:10:00', 'arrival': '2021-09-01T18:40:00'},
#          {'origin': 'RFZ', 'destination': 'BUD', 'departure': '2021-09-01T20:10:00', 'arrival': '2021-09-01T18:40:00'}]
#      }

# return journey search examples
# possible_journeys = {0: [[('WIW', 'ECV'), ('ECV', 'RFZ')], [('WIW', 'RFZ')]],
#                      1: [[('RFZ', 'ECV'), ('ECV', 'WIW')], [('RFZ', 'WIW')]]}
# possible_journeys = \
#     {0: [[('DHE', 'NIZ')],
#          [('DHE', 'NRX'), ('NRX', 'NIZ')],
#          [('DHE', 'NRX'), ('NRX', 'SML'), ('SML', 'NIZ')],
#          [('DHE', 'SML'), ('SML', 'NRX'), ('NRX', 'NIZ')],
#          [('DHE', 'SML'), ('SML', 'NIZ')]],
#      1: [[('NIZ', 'DHE')],
#          [('NIZ', 'NRX'), ('NRX', 'SML'), ('SML', 'DHE')],
#          [('NIZ', 'NRX'), ('NRX', 'DHE')],
#          [('NIZ', 'SML'), ('SML', 'NRX'), ('NRX', 'DHE')],
#          [('NIZ', 'SML'), ('SML', 'DHE')]]}


def discover_all_combinations(flights_dict, searching_return, destination):
    legs_count = len(flights_dict) - 1
    present_solution = []
    solutions = []
    counter = 0

    def inner_loop(ways):
        nonlocal counter, present_solution
        for row in ways:
            present_solution.append(row)
            if counter == legs_count:   # reached bottom level
                if searching_return:    # this part to reuse code for return search as well
                    solutions.append(present_solution[:])
                else:
                    if check_consecutive_flights(present_solution, destination):   # original part without return search
                        solutions.append(present_solution[:])
                if present_solution:
                    present_solution.pop()
            if counter < legs_count:
                counter += 1
                inner_loop(flights_dict[counter])
        counter -= 1
        if present_solution:
            present_solution.pop()

    inner_loop(flights_dict[counter])
    return solutions


# result = discover_all_combinations(possible_journeys, True, 'NIZ')
# # for i in result:
# #     print(i)
# print(result)
