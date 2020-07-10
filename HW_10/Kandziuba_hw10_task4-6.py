#Задание 4
#Напишите функцию, удаляющую из списка целых
#некоторое заданное число. Из функции нужно вернуть
#количество удаленных элементов.

x = [1, 4, 4, 5, 6, 4]
print('There is a list', x)
num = int(input('Enter the number you want to delete: '))

def my_count(number):
    count = 0
    i = 0
    while i < len(x):
        if x[i] == number:
            del x[i]
            count +=1   
        else:
            i += 1
        
        return count

print('You deleted', my_count(num), 'items of the list. Now your list is:', x)


#Задание 5
#Напишите функцию, которая получает два списка в
#качестве параметра и возвращает список, содержащий
#элементы обоих списков.

l1 = [3, 'e', 5, 6, 8]
l2 = [4, 5, 'e', 6, 33, 'a', 53, 4]


def list_comb(a, b):
    return a+b

print('There are 2 lists:', l1, l2, 'There is their combination:', list_comb(l1, l2), sep = '\n')

#Задание 6
#Напишите функцию, высчитывающую степень каждого
#элемента списка целых. Значение для степени передаётся
#в качестве параметра, список тоже передаётся в качестве
#параметра. Функция возвращает новый список, содержащий полученные результаты.

pow = int(input("Enter the power for elements of the list: "))
list_p = [1, 3, 4, 4, 5, 6, 4]

def list_pow(lst, p):
    new_lst = []
    for i in lst:
        new_lst.append(i**p)
    return new_lst

print("There is a list:", list_p, "\nThere is a list of elements in", pow, "power: ", list_pow(list_p, pow))