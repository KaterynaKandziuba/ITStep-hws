#Проверяем, является ли введенная пользователем строка полиндромом

list_1 = input('Enter something: ')
list_1_rev = list_1[::-1]

if list_1 == list_1_rev:
    print('You entered a polindrom!')
else: print('Your string is not a polindrom')




