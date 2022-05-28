import re


def is_palindrome(input_value):
    input_string = str(input_value)
    prepared_string = re.sub(r'\W|\s', '', input_string).lower()
    result = prepared_string == prepared_string[::-1]

    print("input string: " + input_string + " | result: " + str(result))

    return result


is_palindrome("A man, a plan, a canal -- Panama")
is_palindrome("Madam, I'm Adam!")
is_palindrome(333)
is_palindrome(None)
is_palindrome("Abracadabra")
