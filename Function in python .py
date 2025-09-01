# Let's create a function (with doc string)
def is_even(num):
    """This function returns if a given number id odd or even
    input-any valid integer
    output-odd/even
    created on - 22july2025
    """
    # if type(num) == int:
    if isinstance(num, int):
        if num % 2 == 0:
            print("even")
        else:
            print("odd")
    else:
        print("please enter valid value")


# Function use karna:-

for i in range(1, 11):
    x = is_even(i)
    print(x)

# How to check documents
print(is_even.__doc__)

# PARAMETERS Vs ARGUMENTS
# parameters hota hai function ko bante time or arguments hota hai function use karte time


# Types of arguments
# 1.Default Arguments
def power(a, b):
    return a**b


print(power(2, 3))


# 2.Positional Arguments
def power(a, b=3):
    return a**b


print(power(2))


# 3.Keyword Arguments
def power(a, b):
    return a**b


print(power(b=3, a=2))

# *args and **kwargs
# *args and **kwwargs are special python keywords that are used to pass the variable length of arguments to a function...


# *args
# allows us to pass a variable number of non-keywords arguments to a function
def multiply(*args):
    product = 1
    for i in args:
        product = product * i

    print(args)
    return product


m = multiply(2, 3, 4, 4, 5, 5, 5)
print(m)

# **kwargs
# **kwargs allows us to pas any number of keywords arguments.
# keywords arguments mean that they contain a key-value pair, like a python dictyionary.


def display(**kwargs):
    for key, value in kwargs.items():
        print(key, "->", value)


display(india="delhi", srilanka="colombo", nepal="kathmandu", pakistan="islamabad")

# Points to remember while using *args and **kwargs
# 1.order of the arguments matter(normal->*args->**kwargs)
# 2.The words *args and **kwargs are only a conversation you can use any name of your choise

# Without returns function statements


# Variable scope
def g(y):
    print(x)
    print(x + 1)


x = 5
g(x)
print(x)


def h(y):
    x += 1


x = 5
h(x)
print(x)


def f(x):
    x = x + 1
    print("in f(x): x=", x)
    return x


x = 3
z = f(x)
print("in main program scope: z=", z)
print("in main program scope:x=", x)

# Nested functions


# Function are 1st class citizens
# Type and id
def square(num):
    return num**2


sq = square(3)
print(sq)
# reassign

# deleting a function
del square

# storing


# returning a function
def f():
    def x(a, b):
        return a + b

    return x


val = f()(3, 4)
print(val)


# function as arguments
def func_a():
    print("inside func_a")

    def func_b(z):
        print("inside func_c")
        return z()

    print(func_b(func_a))


# Benefits of using a function
# 1.Code Modularity
# 2.Code Readibility
# 3.Code Reuability

# Lambda Function
# -> A lambda functions is a small anonymous function.
# -> A lambda function can take any number of arguments, but can only have one expressions.

# lambda a,b: a+b

# x-> x^2
a = lambda x: x**2
print(a(8))

# x,y -> x+y
a = lambda x, y: x + y
print(a(2, 3))

# Diff between lambda Vs normal function
# 1. No name
# 2.lambda has no return value(infact,returns a function)
# 3.lambda is written in 1 line
# 4.not reusable

# Then why use lambda function?
# ->They are used for HOF(High Order Function)

# check if a string has 'a'
a = lambda s: "a" in s
a("hello")

# odd or even
a = lambda x: "even" if x % 2 == 0 else "odd"
print(a(5))


# High Order Function
def square(x):
    return x**2


def tranform(f, L):
    output = []
    for i in L:
        output.append(f(i))

        print(output)

        L = [1, 2, 3, 4, 5]
        tranform(lambda x: x**3, L)


# Map
# square the items of a list
L = list(map(lambda x: x**2, [1, 2, 3, 4, 5]))
print(L)
# odd or even labelling of list items
L = [1, 2, 3, 4, 5]
OE = list(map(lambda x: "even" if x % 2 == 0 else "odd", L))
print(OE)
# fetch name from list of dict
users = [
    {"name": "A", "age": 12, "gender": "female"},
    {"name": "V", "age": 14, "gender": "female"},
    {"name": "D", "age": 18, "gender": "female"},
    {"name": "T", "age": 18, "gender": "female"},
    {"name": "S", "age": 19, "gender": "female"},
]
L = list(map(lambda users: users["name"], users))
print(L)

# Filter
# NUMBER  greater than 5
L = [3, 4, 5, 6]
G = list(filter(lambda x: x >= 5, L))
print(G)
# fetch fruits starting with 'a'
fruits = ["apple", "guava", "grapes", "cherry"]
F = list(filter(lambda x: x.startswith("a"), fruits))
print(F)

# Reduce
# sum of all items
import functools

R = functools.reduce(lambda x, y: x + y, [1, 2, 3, 4, 5])
print(R)

# find min
M = functools.reduce(lambda x, y: x if x < y else y, [23, 11, 45, 10, 1])
print(M)
#find max
M = functools.reduce(lambda x, y: x if x > y else y, [23, 11, 45, 10, 1])
print(M)

