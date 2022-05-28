from datetime import date, timedelta


def date_in_future(days_number):
    result = date.today()

    if isinstance(days_number, int):
        result = date.today() + timedelta(days=days_number)

    result = result.strftime('%d-%m-%Y %H:%M:%S')

    print("input days number: " + str(days_number) + " | result: " + str(result))

    return result


date_in_future([])
date_in_future(2)
