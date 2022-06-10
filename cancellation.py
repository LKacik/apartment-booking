import json


'''function that allows you to delete a reservation, in the key value 'imie', 'nazwisko', 'data wynajmu 'insert None'''


def cancellation_room_reservation():
    print('Proszę podać dane anulowanej rezerwacji: ')
    first_name = input('Imię wynajmującego: ')
    last_name = input('Nazwisko wynajmującego: ')
    date_from = input('Datę rozpoczęcia wynajmu(RRRR, MM, DD): ')

    with open('room.json', 'r', encoding='utf-8') as read_file:
        room_reservation_dict = json.load(read_file)
        for index_number in range(1, len(room_reservation_dict) + 1):
            condition_fulfillment_counter = 0
            if first_name == room_reservation_dict.get(str(index_number))['imie'] and last_name == room_reservation_dict.get(str(index_number))['nazwisko'] and date_from == room_reservation_dict.get(str(index_number))['data wynajmu'][0]:
                condition_fulfillment_counter += 1
                keys_reservation = ['imie', 'nazwisko', 'data wynajmu']
                for key_reservation in keys_reservation:
                    room_reservation_dict[str(index_number)][key_reservation] = None
                print('Rezerwacja, anulowana pomyślnie.')
                print(room_reservation_dict)
                with open('room.json', 'w', encoding='utf-8') as save_file:
                    json.dump(room_reservation_dict, save_file, ensure_ascii=False)
            if condition_fulfillment_counter == 0:
                print('Błąd, brak rezerwacji o takich danych.')
