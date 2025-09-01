#1.Python output
print("hello world")
print(4)
print(9.5)
print(True)

print("hello",3,4.43,True)

print("hello",3,4.43,True,sep='/')

print("hello")
print("world")

print("hello",end='-')
print("world")

#2.Data types
#1.integers
print(8)

#2.Decimal/Float
print(8.5)

#3.Boolean
print(True)
print(False)

#4.Text/string
print("hello world")

#5.complex number
print(6+7j)

#6.list
print([1,2,3,4])

#7.Tuple
print((1,2,3,4))

#8.sets
print({1,2,3,4})

#9.Dictionary
print({'name':'ankit','gender':'male','age':18,'weight':71})

# type(indetifiy which type of function)
type(6)
type(5.5)
type("hello world")
type([1,2,3,4])
type({1,2,3,4})

#3.Variable type
name="ankit"
print(name)

#1.Dynamic typing
a=5
b=6
print(a + b)

#2.static typing
#int  a=5

#3.Dynamic binding
a=6
print(a)
a="ankit"
print(a)

a=4
b=6
c=7
print(a,b,c)

a,b,c=1,2,3
print(a,b,c)

a=b=c=5
print(a,b,c)

#Comments

#4.Keywords & identifiers
#total 32 keywords and donot chosice keywords as a variable in python..
#you create name in your programe is called identifiers...
#write to rule of identifiers
# 1. you can not start with digit
#1name="ankit"
#print(1name)
name1="ankit"
print(name1)
# 2.You can only use one special chrs like _
#first-name="ankit"
#print(first-name)
first_name="ankit"
print(first_name)
_='ankit'
print(_)
#3.idemtifiers can not be keywords

#5.Users input
#1.static input-only take information like calender,clock
#2.Dynamic input-like youtube,rapido,flipcart take information and give command

#take input from users and store in a variable
fnum= input('enter first number')
snum= input('enter second number')
#add the two variables
result=int(fnum) +int(snum)
#print the results
print(result)

#6.Type conversion
#Implicit vs Explicit
#Explicit
#str->int
print(int(4.5))
#int to str
print(str(5))
#int to float
print(float(4))

#7.Literals
#1.Binary literals
a=0b1010
print(a)
#2.Decimal literals
b=100
print(b)
#3.octal literals
c=0o310
print(c)
#4.Hexadecimal literals
d=0x12c
print(d)
#4.Float literals
float_1 = 10.5
float_2 = 1.5e2 # 1.5*10^2
float_3 = 1.5e-3 # 1.5*10^-3
#5.Complex literals
x=3.14j
print(a,b,c,d)
print(float_1,float_2,float_3)
print(x,x.imag,x.real)

# Method to write string
string='this is python'
string="this is python"
string="""this is python"""

a=True+4 #True means +1
b=False+10 #False means 0
print(a)
print(b)

# None is used for variable declare
a=None
print(a)
