#Створити множини: A, B, C з довільними елементами.
from random import randint

A = set([randint(1, 100) for i in range(10)])
B = set([randint(1, 100) for i in range(10)])
C = set([randint(1, 100) for i in range(10)])

print(f"There are sets A: {A}, \nB: {B} \nand C: {C}")

#1. Знаходимо різні елементи для A, B

def different(A: set, B:set):
    return A^B

D = different(A, B)
print("Different elements of A and B:", D)

#2. Знаходимо однакові елементи для A, C
def similar(A: set, B: set):
    return A&C
S = similar(A, C)
print ("Similar elements of A and C:", S)

#3. Знаходимо об'єднання всіх трьох множин
def united(A: set, B: set, C: set):
    return A|B|C

U = united(A, B, C)
print ("United elements of A, B, and C:", U)

