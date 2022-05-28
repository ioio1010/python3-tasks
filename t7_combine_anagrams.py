def combine_anagrams(words_list):
    result = {}

    for word in words_list:
        group_key = ''.join(sorted(word))
        result[group_key] = []
        sorted_word = sorted(word)

        for anagram in words_list:
            if sorted_word == sorted(anagram):
                result[group_key].append(anagram)

    result = list(result.values())

    print("words list: " + str(words_list) + " | result: " + str(result))

    return result


combine_anagrams(["cars", "for", "potatoes", "racs", "four", "scar", "creams", "scream"])