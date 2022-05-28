import numbers


def max_odd(input_list):
    result = None

    for element in input_list:
        if (isinstance(element, numbers.Number)) and (element % 2 != 0):
            if (result is None) or (element > result):
                result = element

    print("input list: " + str(input_list) + " | result: " + str(result))

    return result


max_odd([1, 2, 3, 4, 4])
max_odd([21.0, 2, 3, 4, 4])
max_odd(['ololo', 2, 3, 4, [1, 2], None])
max_odd(['ololo', 'fufufu'])
max_odd([2, 2, 4])
