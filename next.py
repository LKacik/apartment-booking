from datetime import date, datetime
import json
from data import print_rental_date


def next_reservation():
    date_today = date.today()
    try:
        with open('room.json', 'r', encoding='utf-8') as read_file:
            room_reservation_dict = json.load(read_file)
        condition_fulfillment_counter = 0
        temp_index_value = None
        date_temp = date.today()
        counter = 0
        for index_number in range(1, len(room_reservation_dict) + 1):
            condition_fulfillment_counter += 1
            index_values = room_reservation_dict.get(str(index_number))
            try:
                date_for = index_values['data wynajmu'][0]
            except TypeError:
                continue
            date_for = datetime.strptime(date_for, "%Y, %m, %d").date()
            condition_fulfillment_counter += 1
            if counter == 0:
                date_temp = date_for
                temp_index_value = index_values
                phone_number = temp_index_value['nr telefonu']
            if date_for >= date_today and date_temp >= date_for and counter > 0:
                date_temp = date_for
                temp_index_value = index_values
                phone_number = temp_index_value['nr telefonu']
            counter += 1
        if condition_fulfillment_counter == 0:
            print('Brak rezerwacji.')
        print(f"imie: {temp_index_value['imie']} \nnazwisko: {temp_index_value['nazwisko']} \ndata wynajmu:"
            f" {print_rental_date(temp_index_value['data wynajmu'][:])} \nnumer telefonu:"
            f" {'-'.join(phone_number[i:i + 3] for i in range(0, len(phone_number), 3))} \nilość łózek: {temp_index_value['ilosc lozek']}\nuwagi:"
            f" {temp_index_value['uwagi']} \n")
    except FileNotFoundError:
        print(f"Brak najbliżej rezerwacji.\n")
