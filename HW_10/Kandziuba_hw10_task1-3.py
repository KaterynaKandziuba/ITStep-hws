#Задание 1
#Напишите функцию, вычисляющую произведение
#элементов списка целых. Список передаётся в качестве параметра.
#Полученный результат возвращается из функции.

def items_product(aList):
    product = 1
    for position in range(len(aList)):
        product = product * aList[position]
    return product

list_a = [1, 2, 4, 5, 8]

print("Product of items of some list is", items_product(list_a))

#Задание 2
#Напишите функцию для нахождения минимума в
#списке целых. Список передаётся в качестве параметра.
#Полученный результат возвращается из функции.

def my_min(list_b):
    return min(list_b)

nums = [1, 3, 5, 7, 9]
print("Minimum value of some list is", my_min(nums))


#Задание 3
#Напишите функцию, определяющую количество простых чисел в списке целых. 
#Список передаётся в качестве параметра. 
#Полученный результат возвращается из функции.

last = int(input('We will look for prime numbers in list. Enter the last number of the list: '))
list_c = []
for i in range(last+1):
    list_c.append(i)
print(list_c)

def my_prime(x):
    prime_list = []
    for number in range(2, len(x)):
        swapper = True
        for i in range(2, number):
            if number % i == 0:
                
                swapper = False
            if swapper:
                 prime_list.append(number)
            
            return prime_list

print("Prime numbers are:", len(my_prime(list_c)), '=', my_prime(list_c))