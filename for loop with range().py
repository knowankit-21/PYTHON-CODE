#-------------------------------- TOPIC:------------------------------------------------

#----------------------The Basics of while Loop in python-------------------------------
#(1) Updating a variable
x = 0
x = x + 1

#(2) Basics of while Loop
# Repeats a piece of code until the condition becomes False.
n=1
while n<=3:
    print(n)
    n+=1

n=1
while n<=3:
    print(n,end=' ')
    n+=1

#--------------------------------conditionals and Loop----------------------------------
#(1) Sum of First n Natural Numbers.
n=int(input("Enter the value of n: "))
sum=0
while n>0:
    sum+=n
    n-=1
print(f"Sum is {sum}")

#----------------------------The infinite while Loopin python---------------------------
# INTRODUNCTION
# A while loop can run infinitely if the condition never becomes false.
n=100
while True:
    print(n)
    n-=1

# Breaking hte infinite while loop
while True:
    line=input("Enter the line (type 'q' to quit):")
    if line=='q':
        break
    print(line)

#---------------------------while Loop with else in Python------------------------------
#(1) Introdunction
#-> When the while condition becomes false and the loop runs normally,then the else block
# will be executed.

#(2) Use of while Loop with else
#-> Lets consider a list of fruits that includes four types of fruits: apple,banana,mango
# and strawberry.Write a program to determine whether the fruit orange is present in the list.

fruits=['apple','banana','mango','strawberry']
fruits_len=len(fruits)
index=0

while index<fruits_len:
    if fruits[index]=='orange':
        print('orange is available.')
        break
    index+=1
else:
    print("Orange is not available.")

#---------------------Introduction to the range() Function------------------------------
# Return a series of numbers.
# Syntax:- range(start,stop,step)
# Start:-starting position of the sequence.Default value is 0.
# Stop:-stopping position of the sequence.Never included in the result of the range()function.
# Step:-specifies the increment value.Default value of 1.

#--------------------------for Loop with range(stop)------------------------------------
# Generates a sequence of integers starting from 0 to stop -1.

for i in range(1,5):
    print(i)
print("Done!!")

#--------------------------for Loop with range(start,stop)------------------------------
# Generates a sequence of integers starting from start to stop -1.

for i in range(1,5):
    print(i)
print('Done!!')

#--------------------------for Loop with range(start,stop,step)-------------------------
# Generates a sequence of integers starting from start, incremented by step,and stopped
# at stop -1.

for i in range(1,10,2):
    print(i)
print('Done!!')

#---------------------------------Point To Remember-------------------------------------
#(1) The range() function only works with integer arguments.
#(2) All three arguments can be positive or negative.
#(3) The step value can not be Zero.

#--------------------------------Conditionals and Loops---------------------------------
# Sum of First n Natural Number using for Loop

n=int(input('Enter the value of n:'))
sum=0
for i in range(1,n+1):
    sum+=i
print(f"Sum of first {n} natural number is {sum}.")

#---------------------------for Loop-Reversing a Range of Number------------------------
# Reversing a Range Using Negative Step Value
for i in range(10,0,-1):
    print(i)
print('Done!!')

# Reversing a Range Using reversed() Function
for i in reversed(range(1,6,1)):
    print(i)
print('Done!!')

#---------------------------for Loop with strings in python-----------------------------
#(1)ACCESSING CHARACTERS OF A STRING

# for loop cab be used to access all characters of a string.
# HORIZONTAL
name='Ankit'
for i in name:
    print(i,end=' ')
print('Done!!')
# VERTICAL
name='Ankit'
for i in name:
    print(i)
print('Done!!')

#(2)iterating a string in Reverse Order
# Slicing can be used to reverse a string
# VERTICAL
name='Ankit'
for i in name[::-1]:
    print(i)
# HORIZONTAL
name='Ankit'
for i in name[::-1]:
    print(i,end=' ')

#(3)ACCESSING WORDS OF A STRING
# split()function can be used to split a string into words.
sentence="ankit tanu anshul apple banana."
count=0
for world in sentence.split():
    count+=1
print(f"There are {count} words in the sentence.")

#------------------------------- for Loop with Lists in Python--------------------------
#(1)ITERATING OVER A LIST
# for loop can be used to iterate over a list.
cars=['Audi','BMW','Toyota']
for car in cars:
    print(car)

#(2)ITERATING OVER A LIST USING FOR LOOP AND RANGE()
# for loop along with range() function can be used to iterate over a list.
cars=['Audi','BMW','Toyota']
for i in range(len(cars)):
    print(cars[i])

#(3)LIST COMPREHENSIONS
# List comprehension can produce the result in less lines of code.
cars=['Audi','BMW','Toyota']
[print(car) for car in cars]

#----------------------------for Loop with Dictionary in Python-------------------------
#(1)ITERATING OVER A DICTIONARY
# for loop can be used to iterate over a dictionary.
course={'name':'Python','instructor':'jaspreet'}
for x in course:
    print(x)  # print name or instructor

#(2)ACCESSING VALUES OF A DICTIONARY
# values can be accessed using square-bracket notation.
course={'name':'Python','instructor':'jaspreet'}
for x in course:
    print(course[x]) # print python or jaspreet

# values can also be accessed using values() method.
course={'name':'Python','instructor':'jaspreet'}
for y in course.values():
    print(y)  # print python or jaspreet

#(3)ACCESSING KEYS OF A DICTIONARY
# keys can be accessed using keys() method.
course={'name':'Python','instructor':'jaspreet'}
for x in course.keys():
    print(x) # print name or instructor

#(4)ACCESSING KEYS AND VALUES OF A DICTIONARY
# keys and values can be accessed using items() method.
course={'name':'Python','instructor':'jaspreet'}
for x,y in course.items():
    print(x,y) # print both name,python and instructor,jaspreet

#----------------------------for Loop with else in Python-------------------------------
# USE OF FOR LOOP WITH ELSE.
fav_language=['python','c','java','ruby']
for language in fav_language:
    if'python'==language:
        print('I LIKE PYTHON')
        break
else:
    print('I DONOT LIKE PYTHON')

#-------------------------break and continue statements in python-----------------------
# THE BREAK STATEMENT
# Used to terminate the running loop.
#EXAMPLE:-1
numbers=list(range(0,100))
for number in numbers:
    if number>50:
        break
    print(number,end=' ')
#EXAMPLE:-2
while True:
    num=input("Enter the number(q for quit): ")
    if num=='q':
        break
    print(num)
# THE CONTINUE STATEMENT
# Used to skip the current iteration of the loop.
#Exanple:-1
for i in range(5):
    if i==2 or i==4:
        continue
    print(i)
#EXAMPLE:-2
n=0
while n<=10:
    n+=1
    if n%2!=0:
        continue
    print(n,end=' ')

#--------------------------------Nested for loop in python------------------------------
# NESTED FOR LOOP:
# Refers to a for loop within a for loop.
list1=[1,2,3]
list2=[4,5,6]
for i in list1:
    for j in list2:
        print(i,j)
    print()

#----------------------------------for Loop vs while Lopp-------------------------------
#(1) for Loop needs an iterable object to iterate.
#(1) while Loop executes based on some condition.

#      syntax:for for loop                    syntax:for while loop
#      for var in iterable:                   while condition:
#             do somethig                         do something

#(2) for loop is used when the number of iteration is known in advance.
#(2) while loop is used when the number of iterations is not known in advance.

#EXAMPLE:-of for loop
for i in range(1,9):
    print(i)

items=[0]
for item in items:
    print(item)
    items.append(item)

#EXAMPLE:of while loop
while True:
    n=input("Enter the number(q for quit)")
    if n=='q':
        break
    print(n)

item=0
while True:
    print(item)


