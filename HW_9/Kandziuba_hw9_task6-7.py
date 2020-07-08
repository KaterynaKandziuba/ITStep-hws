#Задание 6
#Напишите функцию, которая считает количество
#цифр в числе. Число передаётся в качестве параметра. Из
#функции нужно вернуть полученное количество цифр.
#Например, если передали 3456, количество цифр будет 4.

a = int(input("Enter your number: "))

def digits(n):
    counter = 0;
    i = 1
    while n > 0:
        n = n//(10**i)
        counter +=1
    print("Your number has", counter, "digits.")

digits(a)


#Задание 7
#Напишите функцию, которая проверяет является ли
#число палиндромом. Число передаётся в качестве параметра. Если число палиндром,
# нужно вернуть из функции true, иначе false.

number = int(input('Enter a number to check if it is a palindrome:'))

def palindrome(n):
    n = str(n)
    n_rev = n[::-1]
    
    if n == n_rev: 
        return True
    else: 
        return False

if palindrome(number): 
    print("Yeap!")
else: 
    print('Oh, no!')

