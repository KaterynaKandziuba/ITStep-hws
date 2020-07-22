
#Task 1
# Есть три кортежа целых чисел необходимо найти
#элементы, которые есть во всех кортежах.
a = (1, 2, "?", 5, 6, 0)
b = (0, 2, 3, 5)
c = ("!", 2, 2, 3, 5, 0)
print('There are 3 tuples: ', a, b, c)

def task_1(a: tuple, b: tuple, c: tuple):
    same_in_ab = []
    tuple_of_the_same = []
    for i in a:
        if i in b:
            same_in_ab.append(i)
    for j in c:
        if j in same_in_ab:
            tuple_of_the_same.append(j)
    
    tuple_of_the_same = tuple(tuple_of_the_same)
    print("Same elements of all: ", tuple_of_the_same)
    return tuple_of_the_same

task_1(a, b, c)


#Task 2
#Есть три кортежа целых чисел необходимо найти
#элементы, которые уникальны для каждого списка.

def task_2(a: tuple, b: tuple, c: tuple):
    dif_tuple = []
    for i in a:
        if i not in b:
            if i not in c:
                dif_tuple.append(i)
    for j in b:
        if j not in a:
            if i not in c:
                dif_tuple.append(j)
    for k in c:
        if k not in a:
            if k not in b:
                dif_tuple.append(k)

    dif_tuple = tuple(dif_tuple)
    print("Different elements of all", dif_tuple)
    return dif_tuple

task_2(a, b, c)

#Task 3
#Есть три кортежа целых чисел необходимо найти элементы, 
#которые есть в каждом из кортежей и находятся
#в каждом из кортежей на той же позиции.
def task_3(a: tuple, b: tuple, c: tuple):
    same_el_i = []
    if len(a) <= len(b) and len(a) <= len(b):
        for i in range(len(a)):
            if a[i] == b[i] and a[i] == c[i]:
                same_el_i.append(a[i])
    elif len(b) < len(a) and len(b) <= len(c):
        for i in range(len(b)):
            if b[i] == a[i] and b[i] == c[i]:
                same_el_i.append(b[i])
    else:
        for i in range(len(c)):
            if c[i] == a[i] and c[i] == b[i]:
                same_el_i.append(c[i])
    
    same_el_i = tuple(same_el_i)
    print("Same elements with same indexes", same_el_i)
    return same_el_i

task_3(a, b, c)