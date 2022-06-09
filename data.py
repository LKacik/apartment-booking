import datetime


def print_rental_date(rental_date: list):
    data_from = rental_date[0]
    data_to = rental_date[1]
    new_data_from = data_from.replace(' ', '').split(',')
    new_data_to = data_to.replace(' ', '').split(',')
    data1 = datetime.date(int(new_data_from[0]), int(new_data_from[1]), int(new_data_from[2]))
    data2 = datetime.date(int(new_data_to[0]), int(new_data_to[1]), int(new_data_to[2]))
    result = f"{data1} -> {data2}"
    return result
