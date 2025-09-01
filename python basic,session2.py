#1.Operators in python
#1.Arithmethic operators
print(2+3) #Addition
print(2-3) #Subtraction
print(5/2) #Division
print(2*3) #Multiplication
print(5//2) #Integers Division(important)
print(5%2) #Modulus operators jo remander aata hain(important)
print(5**2) #Power of operators(25)

#2.Relational operators
print(4>3) #Greater than operators
print(2<4) #Less than operators
print(4>=4) #Greater than equal to operators
print(4<=4) #Less than equals to operators
print(4==4) #Double equals to operators(important)
print( 4!=4) #Not equals to operators(important)

#3.Logical operators/three type AND OR NOT
print(1 and 0)
print(1 or 0)
print(not 1)

#4.Bitwise operators
#Bitwise AND
print(2 & 3)
#Bitwise OR
print(2 | 3)
#Bitwise XOR
print(2 ^ 3)

#5.Assignment operators
a = 2 # a is variable,2 is literals,= is assignment
# a=a+2
a += 2
print(a)

#6.Membership operators
#in/not in
print('D' in 'Delhi')
print('D' not in 'Delhi')
print(1 in [2,3,4,5])
print(2 in (3,4,5))
print(4 not in {2,3,5,6})

#Find the sum of the three digit number
number=int(input('enter 3 digit number'))
#345%10 -> 5
a=number%10
number=number//10
#34%10 -> 4
b=number%10
number=number//10
#3%10->3
c=number%10
number=number//10
print(a+b+c)

#2.If-else
email=input('enter you email')
password=input('enter your password')
if email=='ankit9341599420@gmail.com' and password=='123':
    print('welcome')
else:
    print('Not correct')

    # example of if-else-elif, first step email and password both are correct second step email is correct but password is wrong

email=input('enter you email')
password=input('enter your password')
if email=='ankit9341599420@gmail.com' and password=='123':
    print('welcome')
elif email=='ankit9341599420@gmail.com' and password !='123':
    print('In correct try again')
    password=input('enter password again')
    if password=='123':
        print('welcome finally')
    else:
        print('Beta tum se na ho paaaye ga')
else:
    print('Not correct')

    # example of if-else find the min of three given number
    a=int(input('first number'))
    b=int(input('second number'))
    c=int(input('third number'))
    if a<b and a<c:
        print('smallest',a)
    elif b<c:
        print('smallest is',b)
    else:
        print('smallest is',c)

# menu driven calculator
num1=int(input('enter 1st number'))
num2=int(input('enter 2nd number'))
op=input('enter the operatiion')
if op=='+':
    print(num1+num2)
elif op=='-':
    print(num1-num2)
elif op=='*':
    print(num1*num2)
else:
    print(num1/num2)

# For atm
menu=input("""
Hi! How can i help you.
           1.Enter 1 for pin change
           2.Enter 2 for balance check
           3. Enter 3 for exit
""")
if menu == '1':
    print("pin change")
elif menu=='2':
    print("balance check")
else:
    print("exit")

#3.modules in python
#1.math
import math
print(math.factorial(5))
print(math.sqrt(196))
#2.keywords
import keyword
print(keyword.kwlist)
#3.random
import random
print(random.randint(1,100))
#4.datetime
import datetime
print(datetime.datetime.now())
help('modules')

#Loops in python
#1.Needs for loops
#2.while loop
#3.for loop

#2.while loop/For table
number=int(input('enter the number'))
i=1
while i<11:
    print(a,'*','=',number*i)
    i +=1
    #while loop with else
    x=1
    while x<3:
        print(x)
        x+=1
    else:
        print('limit cross')
# guess game
import random
jackpot=random.randint(1,100)
guess=int(input('guess karo'))
counter=1
while guess != jackpot:
#if guess<jackpot:
    print('galat! guess higher')
else:
    print('galat! guess lower')
    guess= int(input('guess karo'))
    counter+=1
#else:
print('correct guess')
print('attempts',counter)
#For loop demo
for i in range(1,11):
    print(i)
#jump of number 2 gap
for i in range(1,11,3):
    print(i)
# back count
for i in range(10,0,-1):
    print(i)
for i in ('Delhi'):
    print(i)