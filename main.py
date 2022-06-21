from next import next_reservation
from reservation import room_reservation
from preview import preview_the_booking
from cancellation import cancellation_room_reservation

menu_options = {
    1: 'Rezerwacja mieszkania',
    2: 'Najbliższa rezerwacja',
    3: 'Anulowanie rezerwacji',
    4: 'Podgląd rezerwacji',
    5: 'Wyjście',
}


def print_menu():
    for key in menu_options.keys():
        print(key, '->', menu_options[key])


if __name__ == '__main__':
    while True:
        print_menu()
        option = ''
        try:
            option = int(input('Proszę dokonać wyboru: '))
        except:
            print('Nie poprawne dane. Proszę wprowadzić cyfrę ...')
        if option == 1:
            room_reservation()
        elif option == 2:
            next_reservation()
        elif option == 3:
            cancellation_room_reservation()
        elif option == 4:
            preview_the_booking()
        elif option == 5:
            print('Wyłączenie programu.')
        else:
            print('Błędny wybór. Proszę wybrać cyfry z przedziału 1 - 5.')