import json
from data import print_rental_date


'''function that allows you to preview the booking, displays the first name, last name, date of rental'''
def preview_the_booking():
    with open('room.json', 'r', encoding='utf-8') as read_file:
        room_reservation_dict = json.load(read_file)
    search_name = input("Proszę podać nazwisko wynajmującego: ")
    for index_number in range(1, len(room_reservation_dict) + 1):
        if search_name == room_reservation_dict.get(str(index_number))['nazwisko']:
            index_values = room_reservation_dict.get(str(index_number))
            print(f"imie: {index_values['imie']} \nnazwisko: {index_values['nazwisko']} \ndata wynajmu:"
                  f" {print_rental_date(index_values['data wynajmu'][:])}")
        else:
            print("Brak nazwiska w bazie wynajmujących.")