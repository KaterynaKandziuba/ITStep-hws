
import random

#Визначаємо довжину кожного списку:
num1 = int(input("Enter the number of elements in the first list: "))
list_1 = []

num2 = int(input("Enter the number of elements in the second list: "))
list_2 = []

#Визначаємо мінімальне та максимальне значення для чисел списку
min_value_1 = int(input('Enter the minimum value for the first list:'))
max_value_1 = int(input('Enter the maximum value for the first list:'))

min_value_2 = int(input('Enter the minimum value for the second list:'))
max_value_2 = int(input('Enter the maximum value for the second list:'))


#Наповнюємо перший список
for i in range(num1):
    a = random.randint(min_value_1, max_value_1) 
    list_1.append(a)
print('Your first list is: ', list_1)

#Наповнюємо другий список
for i in range(num2):
    b = random.randint(min_value_2, max_value_2) 
    list_2.append(b)
print('Your second list is: ', list_2)

#Формуємо список, в якому будуть елементи двох списків
list_3_1 = list_1 + list_2
print('There is a combination of both previous lists: ', list_3_1)

#Формуємо список, в якому будуть елементи списків без повторень
list_3_2 = []

for i in list_1:
    if i not in list_2:
            list_3_2.append(i)

for i in list_2:
    if i not in list_3_2:
        list_3_2.append(i)

print('There are both lists without overlaps of their elements: ', list_3_2)

#Формуємо список з елементів, що є спільними для списків
list_3_3 = []

for i in list_1:
    if i in list_2 and i not in list_3_3:
            list_3_3.append(i)
print('There are same elements for both lists: ', list_3_3)

#Формуємо список з унікальних елементів для кожного списку
list_3_4 = []

for i in list_1:
    if i not in list_2 and i not in list_3_4:
            list_3_4.append(i)

for i in list_2:
    if i not in list_1 and i not in list_3_4:
        list_3_4.append(i)
print('There are unique elements for both lists: ', list_3_4)


#Формуємо список з мінімальними та максимальними значеннями для кожного зі списків
list_3_5 = []
swapped = True

#Відсортуємо методом "Бульбашки" кожен зі списків:
while swapped:
    swapped = False
    for j in range(len(list_1)-1):
        if list_1[j] > list_1[j+1]:
            swapped = True
            list_1[j], list_1[j+1] = list_1[j+1], list_1[j]
print('Sorted list #1 is: ', list_1)

swapped = True
while swapped:
    swapped = False
    for j in range(len(list_2)-1):
        if list_2[j] > list_2[j+1]:
            swapped = True
            list_2[j], list_2[j+1] = list_2[j+1], list_2[j]
print('Sorted list #2 is: ', list_2)

list_3_5.append(list_1[0])
list_3_5.append(list_1[-1])
list_3_5.append(list_2[0])
list_3_5.append(list_2[-1])
print('There is the list, which contains minimum and maximum elements for the first and second lists: ', list_3_5)



