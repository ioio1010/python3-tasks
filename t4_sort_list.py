def sort_list(input_list):
    result = []

    if len(input_list) != 0:
        min = input_list[0]
        max = input_list[0]

        for n in input_list:
            if n < min:
                min = n
            elif n > max:
                max = n

        for n in input_list:
            if n == min:
                result.append(max)
            elif n == max:
                result.append(min)
            else:
                result.append(n)

        result.append(min)

    print("input list: " + str(input_list) + " | result: " + str(result))

    return result


sort_list([])
sort_list([2, 4, 6, 8])
sort_list([1])
sort_list([1, 2, 1, 3])
