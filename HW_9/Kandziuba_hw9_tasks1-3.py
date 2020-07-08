#Задание 1
#Напишите функцию, которая отображает на экран
#форматированный текст:

def bill_text():
   str = '''\"Don't compare yourself with anyone in this world…
 if you do so, you are insulting yourself\".
   \t\t\t\t\tBill Gates'''
   return print(str)

bill_text()


#Задание 2
#Напишите функцию, которая принимает два числа
#в качестве параметра и отображает все четные числа
#между ними.
a = int(input("To get even numbers, add the first number of the list: "))
b = int(input("And the second one: "))

def even_num(x, y):
    p = print("Even numbers between {} and {}:".format(x, y))
    for i in range(x+1, y):
        if i%2 == 0:
            print(i)
    return

even_num(a, b)


#Задание 3
#Напишите функцию, которая отображает пустой или
#заполненный квадрат из некоторого символа. Функция
#принимает в качестве параметров: длину стороны квадрата, 
#символ и переменную логического типа:
# - если она равна True, квадрат заполненный;
# - если False, квадрат пустой.

a_sq = int(input("Enter the lengh of the side of the square: "))
char_sq = input("Enter the character the square will consist of: ")
b_sq = bool(input("If you want to fill the square, press any bottom on your clipboard. If not, just press \"Enter\": "))

def sq(a, char, b):
    if b:
        print((char*a + '\n')*a)
    else: 
        print((char*a + '\n')+((char + (" " * (a-2)) + char + '\n')*(a-2)) + (char*a + '\n'))
    return

sq(a_sq, char_sq, b_sq)