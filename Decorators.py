#------------------------------------Topic----------------------------------------------
#-> A decorators in python is a function that receives another function as input and adds
# some functionallity(decorators) to and it and returns it.

#-> This can happen only because python functions are 1st class citizens.

#-> There are two types of decortors available in python.
#(1)Built in decorators like @staticmethod,@classmethod,@abstractmethod,and @property etc.
#(2)User defined decorators that we programmers can create according to our needs.

#EXAMPLE:-1
def my_decorator(func):
    def wrapper():
        print('************************')
        func()
        print('************************')
    return wrapper

@my_decorator
def hello():
    print('hello')

H=hello()
print(H)

#EXAMPLE:-2
import time

def timer(func):
    def wrapper():
        start=time.time()
        func()
        print('time taken by',func.__name__,time.time()-start,'secs')
    return wrapper

@timer
def hello():
    print('hello world')
    time.sleep(2)

H=hello()
print(H)

#EXAMPLE:-3
import time

def timer(func):
    def wrapper(*args):
        start=time.time()
        func(*args)
        print('time taken by',func.__name__,time.time()-start,'secs')
    return wrapper

@timer
def hello():
    print('hello world')
    time.sleep(2)

@timer
def square(num):
    time.sleep(1)
    print(num**2)

H=hello()
print(H)

S=square(2)
print(S)

#EXAMPLE:-4
def sanity_check(data_type):
    def outer_wrapper(func):
        def inner_wrapper(*args):
            if type(args[0])==data_type:
                func(*args)
            else:
                raise TypeError('Ye data_type nhii chale ga!')
        return inner_wrapper
    return outer_wrapper

@sanity_check(int)
def square(num):
    print(num**2)

@sanity_check(str)
def greek(name):
    print('hello',name)

s=square(2)
print(s)
g=greek('ankit')
print(g)

