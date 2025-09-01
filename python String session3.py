#Sequence sum
# Question->1/1!+2/2!+3/3!+......
# Code here
from itertools import count
from logging import StringTemplateStyle
import string


n=int(input('Enter n'))
result=0
fact=1
for i in range(1,n+1):
    fact=fact*i
    result=result+i/fact
    print(result)

#Nested loop
# unique pair
for i in range (1,5):
    for j in range(1,5):
        print(i,j)

# Question-> pattern1 print
# *
# **
# ***
# ****
# *****
# Code here
rows=int(input('Enter row number'))
for i in range(1,rows+1):
    for j in range(1,i+1):
        print('*',end='')
    print()

#Question-> Pattern2 print
#1
#121
#12321
#1234321
#code here
rows=int(input('Enter row number'))
for i in range(1,rows+1):
    for j in range(i,i+1):
        print(j,end='')
        for k in range(i-1,0,-1):
            print(k,end='')
            print()

#Loop control statements
#1.Break
#2.Continue
#3.Pass

#BREAK LOOP
for i in range(1,10):
    if i==5:
        break
    print(i)

#Question-> Inditifie prime number
lower=int(input('enter lower range'))
upper=int(input('enter upper range'))

for i in range(lower,upper+1):
    for j in range(2,i):
        if i%j==0:
            break
        else:
            print(i)
#Continue
for i in range(1,10):
    if i==5:
        continue
    else:
        print(i)
#Pass
for i in range(1,10):
    pass

#String are sequence of charcters
#in python speciffically,string are a sequence of a unicode charcters
# 1. creating strings
# 2.accessing strings
# 3.adding charcters to strings
# 4.editing strings
# 5.deleting Strings
# 6.Loops operation on Strings
# 7.strings functions

#1.CREATING STRINGS
s='ankit'
s="ankit"
s='''ankit'''
s="""ankit"""
s=str('ankit')
print(s)
#example='it's raning outside' (not correct)
        #="it's raning outside"

#2.ACCESSING SUBSTRINGS FROM A STRING
 #Positive Indexing
s='hello world'
print(s[2])
 #Negative Indexing
s='hello world'
print(s[-3])
#  Slicing
s='hello world'
print(s[0:5])

s='hello world'
print(s[1:])

s='hello world'
print(s[:3])

s='hello world'
print(s[2:7:2])

s='hello world'
print(s[6:0:-2])

#Reverseing the string
s='ankit'
print(s[::-1])

s='hello world'
print(s[-5:])

s='hello world'
print(s[-1:-6:-1])

#4.Editing and Deleting strings
# change strings in python are not allowed
#Deleting strings
s='hello world'
del s
print(s)

#5.Operation in strings
#Arithmetic operations/Only two operators are working
s='ankit'+'anshul'
print(s)

s='ankit'+' '+'anshul'
print(s)

s='ankit'' ' *5
print(s)

s='*'' '*5
print(s)

#Relational operations
s='delhi'=='mumbai'
print(s)

s='delhi'!='delhi'
print(s)

s='mumbai'>'pune'
print(s)#lexiographically

s='Pune'<'pune'
print(s)#for more information go to ascii chart on google

#Logical operations
s='hello' and 'world'
print(s)
s='' and 'world'
print(s)
s='hello' and ' '
print(s)

s='hello' or 'world'
print(s)
s='' or 'world'
print(s)
s='hello' or ''
print(s)

#6.Loops on Strings
for i in 'delhi':
    print(i)
for i in 'delhi':
    print('pune')
#7.Members ship operation
s='d' in 'delhi'
print(s)
s='d' not in 'delhi'
print(s)

#Common functions
# len()
# max()
# min()
# sorted()

s=len('hello world') #also count the space
print(s)
s=max('hello world') #according to ascii chart
print(s)
s=min('hello world')
print(s)
s=sorted('hello world') #increasing order of alphabet
print(s)
s=sorted('hello world',reverse=True) #decresing order of alphabet
print(s)

#Capitalize/Tittle/Upper/Lower/Swapcase
s='hello world'
print(s.capitalize()) # first letter should be capital

s='hello world'
print(s.title()) # starting letter should be capital

s='hello world'
print(s.upper()) # All letter should be capital

s='HeLlO WoRlD'
print(s.lower()) #All letter should be capital

s='HeLlO WoRlD'
print(s.swapcase()) # small letter should be capital and capital should be small

#Count/Find/Index
s='My name is ankit'
print(s.count('i'))

s='my name is ankit'
print(s.find('is'))

s='my name is ankit'
print(s.index('is'))

#endswith/startswith
s='my name is ankit'
print(s.endswith('it'))

s='my name is ankit'
print(s.startswith('my'))

#Format
s='ankit'
p='male'
print('hi! my name is {} and I am a {}'.format(s,p))

name=input('Enter your name')
print(name.format())

#isalnum/isalpha/isdigit/isidentifier
s='ankit1234'
print(s.isalnum())
s='ankit123$'       #isalnum means alphabet and number only indetifie
print(s.isalnum())
s='ankit'
print(s.isalnum())
s='12234'
print(s.isalnum())

s='ankit'
print(s.isalpha())
s='1234'
print(s.isalpha())

s='1234'
print(s.isdigit())
s='ankit123'
print(s.isdigit())

s='1name'
print(s.isidentifier())
s='name1'
print(s.isidentifier())
s='first-name'
print(s.isidentifier())
s='first_name'
print(s.isidentifier())

#Split/join
s='my name is ankit kumar'
print(s.split())


print(" ".join(['my', 'name', 'is', 'ankit', 'kumar']))

print("_".join(['my', 'name', 'is', 'ankit', 'kumar']))

#Replace
s='my name is ankit sharma'
print(s.replace('ankit','anshul'))

#Strip
s='ankit                    '
print(s.strip()) #delete the space