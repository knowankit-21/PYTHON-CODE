#-------------------------Recurision in python------------------------------------------
#-> When a function calls itself, then that function is called as recurision function and
# process is called as recurision.
def demo():
    print('hello')
    demo()

 # function k behar nhii print kar k function andhar call krna hee recurision hota hai.

#Check Recurision Limit:-
import sys
print(sys.getrecursionlimit())
i=0
def demo():
    global i
    i=i+1
    print('hello',i)
    demo()

#How To Modifie This Limit:-
print(sys.getrecursionlimit())
print(sys.setrecursionlimit(2))
i=0
def demo():
    global i
    i=i+1
    print('hello',i)
    demo()

#ADVANTAGE OF RECURSION
#-clean code, complex problems can be solve.
#DISADVANTAGES OF RECURSION
#-Hard to debug,Not memory efficient.

#---------------------------------------------------------------------------------------
#BASIC TYPES OF RECURSION:-
#(1.)Direct Recursion:-when a function calls itself.
n=int(input('Enter the value of n:'))

def natural(n):
    if n==0:
        return
    print(n)
    return natural(n-1)
natural(n)

#(2.)Indirect Recursion:-A function calls another function which then calls the first
# function again.
def num(n):
    if n<=0:
        return
    print(n,end=" ")
    num1(n-1)

def num1(n):
    print(n,end=" ")
    num(n-1)

num1(10)
#A function calls another function which then calls the first
# function again.

#---------------------------------------------------------------------------------------
#Write a python program for factorial of a number using recursion.
# Syntax:
# def fact():
#     if condn:
#         return
#     return[recursion call]

def fact(n):
    if n == 0:
        return 1
    return n*fact(n-1)

print(fact(5))

#---------------------------------------------------------------------------------------
#PRINT YOUR NAME 10 TIMES WITHOUT USING LOOP AND MANUALLY.
count=1
def printer(name):
    global count
    if count<=10:
        print(name)
        count+=1
        printer(name)

printer("Ankit")

#---------------------------------------------------------------------------------------
#FACTORIAL USING RECURSION IN PYTHON
n=int(input("Enter the value of n:"))
def fact(n):
    if n<0:
        return('negative number can not be calculated:')
    elif n==0:
        return 1
    else:
        return n*fact(n-1)

result=fact(n)
print(f"Factorial of {n} is {result}")

#---------------------------------------------------------------------------------------
#POWER OF NUMBER USING RECURSION
def power(n,p):
    if p==0:
        return 1
    return n*power(n,p-1)

power(2,5)

#USE MY TYPE
import math

n=int(input("Enter the base value:"))
p=int(input("Enter the power:"))

def fact(n,p):
    if n==0 and p==0:
        return 0
    else:
        return math.pow(n,p)

result=fact(2,5)
print(result)

#---------------------------------------------------------------------------------------
def count_of(n):
    if n<10:
        return 1
    return 1+count_of(n//10)

n=int(input('Enter the value of n: '))
print(count_of(n))

#---------------------------------------------------------------------------------------
#FIBONACCI SERIES USING RECURSION
def fibo(n):
    if n==1:
        return 0
    elif n==2:
        return 1
    else:
        return (fibo(n-2)+fibo(n-1))

n=int(input('Enter number of terms: '))
for i in range(n,n+1):
    print(fibo(n))

#---------------------------------------------------------------------------------------





