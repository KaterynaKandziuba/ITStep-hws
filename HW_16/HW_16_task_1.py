#Task 1
#GREAT BASKETBALL PLAYERS
import pprint

def get_basketballers(basketballers: list) -> list:
    return basketballers

def print_result(*args) -> None:
    for element in args:
        pprint.pprint(element, width=1)
        input('Press to continue...')

def add_basketballer(first_name: str, surname: str, middle_name: str, heigth: float) -> dict:
    global BASKETBALLERS
    basketballer = {
        "First name": first_name,
        "Surname": surname,
        "Middle name": middle_name,
        "Heigth": heigth
    }
    
    BASKETBALLERS.append(basketballer)
    return basketballer

def del_basketballer(surname: str) -> dict:
    global BASKETBALLERS
    deleted_basketballer = {}
    for index, basketballer in enumerate(BASKETBALLERS):
        if basketballer['Surname'] == surname:
            deleted_basketballer = basketballer
            del(BASKETBALLERS[index])
            return deleted_basketballer

def update_basketballer(surname: str) -> dict:
    global BASKETBALLERS
    for index, basketballer in enumerate(BASKETBALLERS):
        if basketballer['Surname'] == surname:
            first_name = basketballer["First name"]
            surname = basketballer["Surname"]
            middle_name = basketballer["Middle name"]
            heigth = basketballer["Heigth"]
            new_first_name = input(f"Enter first name ({first_name} - default): ")
            new_surname = input(f"Enter surname ({surname} - default): ")
            new_middle_name = input(f"Enter middle name ({middle_name} - default): ")
            new_height = input(f"Enter height ({heigth} - default): ")
            if new_first_name:
                basketballer['First name'] = new_first_name
            if new_surname:
                basketballer['Surname'] = new_surname
            if new_middle_name:
                basketballer['Middle name'] = new_middle_name
            if heigth:
                basketballer['Heigth'] = heigth
            return basketballer

def search_basketballer(surname: str) -> dict:
    global BASKETBALLERS
    for basketballer in BASKETBALLERS:
        if basketballer['Surname'] == surname:
            return basketballer
    return f"Basketballer {surname} does not exist\n"


if __name__ == "__main__":
    BASKETBALLERS_LIST = 'list'
    ADD_BASKETBALLER = 'add'
    DEL_BASKETBALLER = 'delete'
    SEARCH_BASKETBALLER = 'search'
    UPDATE_BASKETBALLER = 'update'
    EXIT = 'quit'
    BASKETBALLERS = []
    while True:
        print(f'''
        Choices:
        BASKETBALLERS_LIST -> {BASKETBALLERS_LIST}
        ADD_BASKETBALLER -> {ADD_BASKETBALLER}
        DEL_BASKETBALLER -> {DEL_BASKETBALLER}
        SEARCH_BASKETBALLER -> {SEARCH_BASKETBALLER}
        UPDATE_BASKETBALLER -> {UPDATE_BASKETBALLER}
        EXIT -> {EXIT}
        ---------------------''')
        choice = input('Enter choice: ')
        if choice == EXIT:
            break

        elif choice == BASKETBALLERS_LIST:
            basketballers = get_basketballers(BASKETBALLERS)
            print_result(basketballers)
            
        elif choice == ADD_BASKETBALLER:
            first_name = input('Enter first name: ')
            surname = input('Enter surname: ')
            middle_name = input('Enter middle name: ')
            heigth = input('Enter heigth in santimeters: ')
            basketballer = add_basketballer(
                first_name=first_name,
                surname=surname,
                middle_name=middle_name,
                heigth = heigth
            )
            print_result(basketballer)

        elif choice == DEL_BASKETBALLER:
            surname = input("Enter basketballer's surname: ")
            basketballer = del_basketballer(surname=surname)
            print_result(basketballer)

        elif choice == SEARCH_BASKETBALLER:
            surname = input("Enter surname: ")
            basketballer = search_basketballer(surname=surname)
            print_result(basketballer)

        elif choice == UPDATE_BASKETBALLER:
            surname = input("Enter surname: ")
            basketballer = update_basketballer(surname=surname)
            print_result(basketballer)
