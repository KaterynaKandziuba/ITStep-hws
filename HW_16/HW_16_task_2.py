#Task 2
#ENGLISH-FRENCH DICTIONARY
import pprint

def get_dictionary(dictionary: list) -> list:
    return dictionary

def print_result(*args) -> None:
    for element in args:
        pprint.pprint(element, width=1)
        input('Press to continue...')

def add_word(inEnglish: str, inFrench: str) -> dict:
    global DICTIONARY
    word = {
        "In English": inEnglish,
        "In French": inFrench,
    }
    DICTIONARY.append(word)
    return word

def del_word(inEnglish: str) -> dict:
    global DICTIONARY
    deleted_word = {}
    for index, word in enumerate(DICTIONARY):
        if word["In English"] == inEnglish:
            deleted_word = word
            del(DICTIONARY[index])
            return deleted_word

def change_word(inEnglish: str) -> dict:
    global DICTIONARY
    for word in DICTIONARY:
        if word['In English'] == inEnglish:
            inEnglish = word["In English"]
            inFrench = word["In French"]
            new_inEnglish = input(f"Enter word in English ({inEnglish} - default): ")
            new_inFrench = input(f"Enter word in French ({inFrench} - default): ")
            if new_inEnglish:
                word['In English'] = new_inEnglish
            if new_inFrench:
                word['In French'] = new_inFrench
        return word


def search_word(inEnglish: str) -> dict:
    global DICTIONARY
    for word in DICTIONARY:
        if word['In English'] == inEnglish:
            return word
    return f"Word {inEnglish} does not exist\n"


if __name__ == "__main__":
    WORDS_LIST = 'list'
    ADD_WORD = 'add'
    DEL_WORD = 'delete'
    SEARCH_WORD = 'search'
    CHANGE_WORD = 'change'
    EXIT = 'quit'
    DICTIONARY = []
    while True:
        print(f'''
        Choices:
        WORDS_LIST -> {WORDS_LIST}
        ADD_WORD -> {ADD_WORD}
        DEL_WORD -> {DEL_WORD}
        SEARCH_WORD -> {SEARCH_WORD}
        CHANGE_WORD -> {CHANGE_WORD}
        EXIT -> {EXIT}
        ---------------------''')
        choice = input('Enter choice: ')
        if choice == EXIT:
            break

        elif choice == WORDS_LIST:
            dictionary = get_dictionary(DICTIONARY)
            print_result(DICTIONARY)
            
        elif choice == ADD_WORD:
            inEnglish = input('Enter word in English: ')
            inFrench = input('Enter word in French: ')
            word = add_word(
                inEnglish=inEnglish,
                inFrench=inFrench,
            )
            print_result(word)

        elif choice == DEL_WORD:
            inEnglish = input("Enter word in English: ")
            word = del_word(inEnglish = inEnglish)
            print_result(word)

        elif choice == SEARCH_WORD:
            inEnglish = input("Enter word in English: ")
            word = search_word(inEnglish=inEnglish)
            print_result(word)

        elif choice == CHANGE_WORD:
            inEnglish = input("Enter word in English: ")
            word = change_word(inEnglish=inEnglish)
            print_result(word)
