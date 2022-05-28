import re
from collections import Counter


def count_words(input_string):
    prepared_string = re.findall(r'\w+', input_string.lower())
    result = Counter(prepared_string)

    print("input string: " + input_string + " | result: " + str(result))

    return result


count_words("A man, a plan, a canal -- Panama")
count_words("Doo bee doo bee doo")
