import math


def multiply_numbers(numbers=None):
    result = None
    numbers_for_multiply = []

    if isinstance(numbers, list):
        numbers_for_multiply = numbers
    elif isinstance(numbers, str):
        numbers_for_multiply = [int(ch) for ch in list(numbers) if ch.isdigit()]
    elif isinstance(numbers, float):
        numbers_for_multiply = [int(ch) for ch in str(numbers) if ch.isdigit()]

    if len(numbers_for_multiply) > 0:
        result = math.prod(numbers_for_multiply)

    print("input list: " + str(numbers) + " | result: " + str(result))

    return result


multiply_numbers()
multiply_numbers('ss')
multiply_numbers('1234')
multiply_numbers('sssdd34')
multiply_numbers(2.3)
multiply_numbers([5, 6, 4])
