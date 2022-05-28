def connect_dicts(dict1, dict2):
    sum_dict1 = sum(dict1.values())
    sum_dict2 = sum(dict2.values())

    sort_dict1 = {key: value for key, value in dict1.items() if value >= 10}
    sort_dict2 = {key: value for key, value in dict2.items() if value >= 10}

    priorities = {"low": sort_dict1, "high": sort_dict2}

    if sum_dict1 > sum_dict2:
        priorities["low"] = sort_dict2
        priorities["high"] = sort_dict1

    result = dict(sorted({**priorities["low"], **priorities["high"]}.items(), reverse=True))

    print("dict1: " + str(dict1) + " | dict2: " + str(dict2) + " | result: " + str(result))

    return result


connect_dicts({"a": 2, "b": 12}, {"c": 11, "e": 5})
connect_dicts({"a": 13, "b": 9, "d": 11}, {"c": 12, "a": 15})
connect_dicts({"a": 14, "b": 12}, {"c": 11, "a": 15})
