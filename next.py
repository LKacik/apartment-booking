from datetime import date, datetime
import json
import os.path
from data import print_rental_date


def next_reservation():
    date_today = date.today()
    with open('room.json', 'r', encoding='utf-8') as read_file:
        room_reservation_dict = json.load(read_file)
    date_temp = room_reservation_dict.get(str('1'))['data wynajmu'][0]
    date_temp = datetime.strptime(date_temp, "%Y, %m, %d").date()
    condition_fulfillment_counter = 0
    temp_index_value = None
    for index_number in range(1, len(room_reservation_dict) + 1):
        condition_fulfillment_counter += 1
        index_values = room_reservation_dict.get(str(index_number))
        date_for = index_values['data wynajmu'][0]
        date_for = datetime.strptime(date_for, "%Y, %m, %d").date()
        if  date_for >= date_today and date_for <= date_temp:
            date_temp = date_for
            temp_index_value = index_values
            phone_number = temp_index_value['nr telefonu']

    print(f"imie: {temp_index_value['imie']} \nnazwisko: {temp_index_value['nazwisko']} \ndata wynajmu:"
          f" {print_rental_date(temp_index_value['data wynajmu'][:])} \nnumer telefonu:"
          f" {'-'.join(phone_number[i:i + 3] for i in range(0, len(phone_number), 3))} \nilość łózek: {temp_index_value['ilosc lozek']}\nuwagi:"
          f" {temp_index_value['uwagi']} \n")



next_reservation()
