#Задание 4
#Напишите функцию, которая возвращает минимальное
#из пяти чисел. Числа передаются в качестве параметров.


n = input("Enter 5 numbers to find the minimal: \n")
list_n = n.split()
indx = 0

for i in list_n:
    list_n[indx] = int(list_n[indx])
    indx += 1

def min_num(a, b, c, d, e):
            if a<=b and a<=c and a<=d and a<=e: 
                print(a, "is the minimal number")
            elif b<=a and b<=c and b<=d and b<=e: 
                print(b, "is the minimal number")
            elif c<=a and c<=b and c<=d and c<=e: 
                print(c, "is the minimal number")
            elif d<=a and d<=b and d<=c and d<=e: 
                print(d, "is the minimal number")
            else: 
                print(e, "is the minimal number")

min_num(list_n[0], list_n[1], list_n[2], list_n[3], list_n[4])


#Задание 5
#Напишите функцию, которая возвращает произведение чисел в указанном диапазоне. 
# Границы диапазона передаются в качестве параметров. 
# Если границы диапазона перепутаны (например, 5 — верхняя граница, 25 —
#нижняя граница), их нужно поменять местами.

x1 = int(input('Indicate the start of a range :'))
x2 = int(input('Indicate the end of a range :'))

def product(a, b):
    res = 1
    if a>b:
        a, b = b, a
       
    for i in range(a, b):
        res = res*i
    
    print('The product of numbers in range is: ', res)

product(x1, x2)