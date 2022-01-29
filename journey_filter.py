from time_check import check_consecutive_flights


def discover_all_combinations(flights_dict, destination, searching_return=False):
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
