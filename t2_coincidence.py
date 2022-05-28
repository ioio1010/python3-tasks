def coincidence(input_list=None, input_range=None):
    result = []

    if None not in (input_list, input_range):
        range_list = []
        for i, n in enumerate(input_range):
            range_list.append(n * 1.0)
            range_list.append(n + 0.5)

        for list_element in input_list:
            if list_element in range_list:
                result.append(list_element)

    print("input list: " + str(input_list) + " | input range: " + str(input_range) + " | result: " + str(result))

    return result


coincidence([1, 2, 3, 4, 5], range(3, 6))
coincidence()
coincidence([None, 1, 'foo', 4, 2, 2.5], range(1, 4))
