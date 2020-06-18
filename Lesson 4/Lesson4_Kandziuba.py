#Завдання 1
#Користувач вводить 3 числа. 
#Далі в залежності від вибору користувача потрібно знайти суму або добуток цих чисел. 
#(Тобто програма запитує в користувача, що потрібно зробити)

num1 = int(input('You need to enter 3 numbers. Enter the first one: '))
num2 = int(input('Great! Please, enter one more: '))
num3 = int(input('Good job! You need to enter the last one: '))
print('You entered: ', num1, num2, num3, '\nNow you can summarize or multiply them.')

dec = input('What do you choose? ')
var1 = 'summarize'
var2 = 'multiply'

if dec == var1:
    print('Your result is: ', num1+num2+num3)
elif dec == var2:
    print('Your result is: ', num1*num2*num3)
else: print('Errort. Check your spelling and try again.')


#Завдання 2
#Користувач вводить 3 числа. 
# Далі в залежності від вибору користувача потрібно знайти 
# найбільше з 3-х, найменше, або середнє арифметичне. (Подібно до 1-го)

number1 = int(input('Now we are comparing numbers. You need to enter 3 numbers again. Enter the first one: '))
number2 = int(input('Admire your perseverance! Please, enter the second one: '))
number3 = int(input('Cool! You need to enter the last one: '))
print('You entered: ', number1, number2, number3, '\nNow you have 3 options.')

big = int()
least = int()
#Определям наибольшее число перебором
if number1>=number2: 
    if number1>=number3: big = number1
    else: big = number3
else:
    if number2>=number3: big = number2
    else: big = number3
#Определяем наименьшее число перебором
if number1<=number2: 
    if number1<=number3: least = number1
    else: least = number3
else:
    if number2<=number3:least = number2
    else: least = number3

decision = input('If you need the biggest number, enter \'1\'. If you need the least number, enter \'2\'. And if you need mean, enter \'mean\': ')
variant1 = str(1)
variant2 = str(2)
variant3 = 'mean'

if decision == variant1:
   print('Your result is: ', big)
elif decision == variant2:
    print('Your result is: ', least)
elif decision == variant3:
    print('Mean = ', (number1+number2+number3)/3)
else: print('Errort. Check your spelling and try again.')

#Завдання 3
#Користувач вводить з клавіатури кількість метрів. 
#В залежності від вибору - програма конвертує їх в сантиметри, міліметри, або кілометри.

lenght = int(input('You need to enter lenght in meters: '))
variant = input('Great! Please, choose to which unit to convert: centimetres, millimetres, or kilometres: ')

unit1 = 'centimetres'
unit2 = 'millimetres'
unit3 = 'kilometres'

if variant == unit1:
    print('Your result is: ', lenght*100, "centimetres")
elif variant == unit2:
    print('Your result is: ', lenght*1000, 'millimetres')
elif variant == unit3:
    print('Your result is: ', lenght/10, 'kilometres')
else: print('Errort. Check your spelling and try again.')