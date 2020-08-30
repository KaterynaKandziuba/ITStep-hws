#Task 3
#FIRM
import pprint

def get_employees(employees: list) -> list:
    return employees

def print_result(*args) -> None:
    for element in args:
        pprint.pprint(element, width=1)
        input('Press to continue...')

def add_employee(
    first_name: str, 
    surname: str, 
    middle_name: str, 
    mobile_number: str, 
    email: str, 
    job_title: str, 
    office_number: int, 
    skype: str) -> dict:

    global FIRM
    employee = {
        "First name": first_name,
        "Surname": surname,
        "Middle name": middle_name,
        "Mobile number": mobile_number,
        "E-mail": email,
        "Job title": job_title,
        "Office number": office_number,
        "Skype": skype
    }    
    FIRM.append(employee)
    return employee

def del_employee(surname: str) -> dict:
    global FIRM
    deleted_employee = {}
    for index, employee in enumerate(FIRM):
        if employee['Surname'] == surname:
            deleted_employee = employee
            del(FIRM[index])
            return deleted_employee

def search_employee(surname: str) -> dict:
    global FIRM
    for employee in FIRM:
        if employee['Surname'] == surname:
            return employee
    return f"Employee {surname} does not exist\n"

def update_employee(surname: str) -> dict:
    global FIRM
    for index, employee in enumerate(FIRM):
        if employee['Surname'] == surname:
            first_name = employee["First name"]
            surname = employee["Surname"]
            middle_name = employee["Middle name"]
            mobile_number = employee["Mobile number"]
            email = employee["E-mail"]
            job_title = employee["Job title"]
            office_number = employee["Office number"]
            skype = employee["Skype"]

            new_first_name = input(f"Enter first name ({first_name} - default): ")
            new_surname = input(f"Enter surname ({surname} - default): ")
            new_middle_name = input(f"Enter middle name ({middle_name} - default): ")
            new_mobile_number = input(f"Enter mobile number ({mobile_number} - default): ")
            new_email = input(f"Enter email ({email} - default): ")
            new_job_title = input(f"Enter job title {job_title} - default): ")
            new_office_number = input(f"Enter office number ({office_number} - default): ")
            new_skype = input(f"Enter Skype ({skype} - default): ")
            if new_first_name:
                employee['First name'] = new_first_name
            if new_surname:
                employee['Surname'] = new_surname
            if new_middle_name:
                employee['Middle name'] = new_middle_name
            if new_mobile_number:
                employee['Mobile number'] = new_mobile_number
            if new_email:
                employee['E-mail'] = email
            if new_job_title:
                employee['Job title'] = new_job_title
            if new_office_number:
                employee['Office number'] = new_office_number
            if new_skype:
                employee['Skype'] = new_skype
            return employee



if __name__ == "__main__":
    EMPLOYEES_LIST = 'list'
    ADD_EMPLOYEE = 'add'
    DEL_EMPLOYEE = 'delete'
    SEARCH_EMPLOYEE = 'search'
    UPDATE_EMPLOYEE = 'update'
    EXIT = 'quit'
    FIRM = []
    while True:
        print(f'''
        Choices:
        EMPLOYEES_LIST -> {EMPLOYEES_LIST}
        ADD_EMPLOYEE -> {ADD_EMPLOYEE}
        DEL_EMPLOYEE -> {DEL_EMPLOYEE}
        SEARCH_EMPLOYEE -> {SEARCH_EMPLOYEE}
        UPDATE_EMPLOYEE -> {UPDATE_EMPLOYEE}
        EXIT -> {EXIT}
        ---------------------''')
        choice = input('Enter choice: ')
        if choice == EXIT:
            break

        elif choice == EMPLOYEES_LIST:
            employees = get_employees(FIRM)
            print_result(employees)
            
        elif choice == ADD_EMPLOYEE:
            first_name = input('Enter first name: ')
            surname = input('Enter surname: ')
            middle_name = input('Enter middle name: ')
            mobile_number = input('Enter mobile number: ')
            email = input('Enter e-mail: ')
            job_title = input('Enter job title: ')
            office_number = input('Enter office number: ')
            skype = input('Enter Skype: ')
            employee = add_employee(
                first_name = first_name,
                surname = surname,
                middle_name = middle_name,
                mobile_number = mobile_number,
                email = email,
                job_title = job_title,
                office_number = office_number,
                skype = skype
            )
            print_result(employee)

        elif choice == DEL_EMPLOYEE:
            surname = input("Enter employee's surname: ")
            employee = del_employee(surname=surname)
            print_result(employee)

        elif choice == SEARCH_EMPLOYEE:
            surname = input("Enter surname: ")
            employee = search_employee(surname=surname)
            print_result(employee)

        elif choice == UPDATE_EMPLOYEE:
            surname = input("Enter surname: ")
            employee = update_employee(surname=surname)
            print_result(employee)
