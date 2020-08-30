#Task 4
#BOOK COLLECTION
import pprint

def get_book(books: list) -> list:
    return books

def print_result(*args) -> None:
    for element in args:
        pprint.pprint(element, width=1)
        input('Press to continue...')

def add_book(author: str, book_name: str, genre: str, year_of_release: int, number_of_pages: int, publishing_house: str) -> dict:
    global BOOKS
    book = {
        "Author": author,
        "Book name": book_name,
        "Genre": genre,
        "Year of release": year_of_release,
        "Number of pages": number_of_pages,
        "Publishing house": publishing_house
    }
    
    BOOKS.append(book)
    return book

def del_book(book_name: str) -> dict:
    global BOOKS
    deleted_book = {}
    for index, book in enumerate(BOOKS):
        if book['Book name'] == book_name:
            deleted_book = book
            del(BOOKS[index])
            return deleted_book

def update_book(book_name: str) -> dict:
    global BOOKS
    for index, book in enumerate(BOOKS):
        if book['Book name'] == book_name:
            author = book["Author"]
            book_name = book["Book name"]
            genre = book["Genre"]
            year_of_release = book["Year of release"]
            number_of_pages = book['Number of pages']
            publishing_house = book['Publishing house']

            new_author = input(f'Enter author of the book ({author} - default): ')
            new_book_name = input(f'Enter name of the book ({book_name} - default): ')
            new_genre = input(f'Enter genre of the book ({genre} - default): ')
            new_year_of_release = input(f'Enter the year of book release ({year_of_release} - default): ')
            new_number_of_pages = input(f'Enter the number of book pages ({number_of_pages} - default): ')
            new_publishing_house = input(f'Enter the publishing house ({publishing_house} - default): ')
            
            if new_author:
                book['Author'] = new_author
            if new_book_name:
                book['Book name'] = new_book_name
            if new_genre:
                book['Genre'] = new_genre
            if new_year_of_release:
                book['Year of release'] = new_year_of_release
            if new_number_of_pages:
                book["Number of pages"] = new_number_of_pages
            if new_publishing_house:
                book["Publishing house"] = new_publishing_house
                
            return book

def search_book(book_name: str) -> dict:
    global BOOKS
    for book in BOOKS:
        if book['Book name'] == book_name:
            return book
    return f"Book {book_name} does not exist\n"


if __name__ == "__main__":
    BOOKS_LIST = 'list'
    ADD_BOOK = 'add'
    DEL_BOOK = 'delete'
    SEARCH_BOOK = 'search'
    UPDATE_BOOK = 'update'
    EXIT = 'quit'
    BOOKS = []
    while True:
        print(f'''
        Choices:
        BOOKS_LIST -> {BOOKS_LIST}
        ADD_BOOK -> {ADD_BOOK}
        DEL_BOOK -> {DEL_BOOK}
        SEARCH_BOOK -> {SEARCH_BOOK}
        UPDATE_BOOK -> {UPDATE_BOOK}
        EXIT -> {EXIT}
        ---------------------''')
        choice = input('Enter choice: ')
        if choice == EXIT:
            break

        elif choice == BOOKS_LIST:
            books = get_book(BOOKS)
            print_result(books)
            
        elif choice == ADD_BOOK:
            author = input('Enter author of the book: ')
            book_name = input('Enter name of the book: ')
            genre = input('Enter genre of the book: ')
            year_of_release = input('Enter the year of book release: ')
            number_of_pages = input('Enter the number of book pages: ')
            publishing_house = input('Enter the publishing house: ')
            book = add_book(
                author = author,
                book_name = book_name,
                genre = genre,
                year_of_release = year_of_release,
                number_of_pages = number_of_pages,
                publishing_house = publishing_house,
            )
            print_result(book)

        elif choice == DEL_BOOK:
            book_name = input("Enter book name: ")
            deleted_book = del_book(book_name=book_name)
            print_result(deleted_book)

        elif choice == SEARCH_BOOK:
            book_name = input("Enter book name: ")
            book = search_book(book_name=book_name)
            print_result(book)

        elif choice == UPDATE_BOOK:
            book_name = input("Enter book name: ")
            updated_book = update_book(book_name=book_name)
            print_result(updated_book)

