#Продемонструвати, що таке замикання на прикладі вкладеної функції

def foo_outer(par):
    def foo_nested(loc):
        loc = loc*2
        return loc
    return foo_nested(par)

number = int(input("Enter a number you want to be doubled by nested function: "))
a = foo_outer(number)
del foo_outer
print ("Here it is: ", a)

#Продемонструвати, що таке lambda x: x ** 2

b = lambda x: x**2
result = int(input("Enter a number you want to be raised in second degree by lambda function:"))
print("Here is your result:", b(result))

# Продемонструвати, що таке map()
c = [1, 2, 3, 4, 5]
c_2 = map(lambda x: x + 5, c)

print("Here is map() function for list:", c, ". It increases it by 5:", list(c_2))
print("But you can see it just once!. Now you see the empty list:", list(c_2))

# Продемонструвати, що таке filter()
d = [1, 2, 3, 'a', 4, 5, 'b']

def foo(x):
    if type(x) == int:
        return True

d_filtered = filter(foo, d)
print('Finally, we worked with filter() function. Here you see list', d, '. Thanks to the filter, we removed all characters from it:', list(d_filtered))
