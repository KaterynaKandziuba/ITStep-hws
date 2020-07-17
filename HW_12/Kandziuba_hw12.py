#Task:
#Написати функцію-декоратор, яка підносить до квадрату значення, 
# що повертає функція, до якої декоратор застосовується.

def sqre(func):
    def wrapper(x):
        func(x)
        print("The square area is", x**2)
    return wrapper

@sqre
def foo(a: int):
    print(f'{a} is the square side length in centimeters.')
    a_m = a*100
    print(f'{a_m} is the square side length in meters.')
    return a_m


if __name__== '__main__':
    
    x = int(input("Enter the lenght of the square side: "))
    result = foo(x)
