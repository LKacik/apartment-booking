import json
import os.path


'''a function that allows you to book a room, saves the date, date in json'''


def room_reservation():

    counter = 0
    if os.path.exists('room.json'):
        with open('room.json', 'r', encoding='utf-8') as read_file:
            room_reservation_dict_temp = json.load(read_file)
            counter = list(room_reservation_dict_temp.keys())[-1]
    room_reservation_dict = dict()
    while True:
        print('Proszę podać: ')
        temp_dict = dict()
        first_name = input('Imię wynajmującego: ')
        last_name = input('Nazwisko wynajmującego: ')
        date_from = input('Datę rozpoczęcia wynajmu(RRRR, MM, DD): ')
        date_to = input('Datę zakończenia wynajmu(RRRR, MM, DD): ')
        phone_number = input('Nr telefonu wynajmującego: ')
        number_beds = input('Ilość łóżek: ')
        notes = input('Uwagi: ')
        temp_dict['imie'] = first_name
        temp_dict['nazwisko'] = last_name
        temp_dict['data wynajmu'] = [date_from, date_to]
        temp_dict['nr telefonu'] = phone_number
        temp_dict['ilosc lozek'] = number_beds
        temp_dict['uwagi'] = notes
        counter = int(counter)
        counter += 1
        room_reservation_dict[str(counter)] = temp_dict
        print(room_reservation_dict)
        end = input("Kontynuujesz czy koniec -> 'q': ")
        if end == 'q':
            if os.path.exists('room.json'):
                data = json.load(open('room.json', encoding='utf-8'))
                data.update(room_reservation_dict)
                with open('room.json', 'w', encoding='utf-8') as outfile:
                    json.dump(data, outfile, ensure_ascii=False)
                break
            else:
                with open('room.json', 'w', encoding='utf-8') as save_file:
                    json.dump(room_reservation_dict, save_file, ensure_ascii=False)
                break
        else:
            continue
