#-----------------------------eval() in python------------------------------------------
# WHAT IS eval() IN PYTHON?
#(1.) eval() is a built-in function used in python.
#(2.) eval function parses the string,argument and evaluates it as a python expression.
#(3.) string-as a python expression.

# Syntax of eval():-
# eval(expression,globals=None,locals=None)
# expression:-A string to evaluate
# globals:-available global methods and variables
# locals:-available local methods and variables

# globals,locals:-optional arguments
# expression:-mandatory

# Return value of eval()?
# result of expression present in string argumnent.

#Example:-1
num=3
var=eval('num*num')
print(var)
print(type(var))

#Example:-2
num=3.0
var=eval('num*num')
print(var)
print(type(var))

#Example:-3
var=eval('print("hello world")')
print(var)

#Example:-4
var=eval('[1,2,3]+[4,5]')
print(var)
print(type(var))

#Example:-5
data=eval(input("Enter the list:"))  #[1,2,3]
print(data)
print(type(data)) #To check any type of data like:-int,list,tuple

#Example:-6
x=int(input("Enter the value of x:"))
eq='x*(x+2)'
ans=eval(eq)
print(ans)

#Example:-7
x=int(input("Enter the value of x:"))
eq=input("Enter the equation:")

ans=eval(eq)
print(ans)

# WHERE IS THE EVAL FUNCTION MOSTLY USED?
#(1.) To solve mathematical expression from string.
#(2.) To take inputs.
#(3.) if the user wnats to evaluate the string into code then can use eval function.

# WARNING WHEN USING eval():-
#(1.) Unix system (macOS,Linux etc)
#(2.) imported the os module
#(3.) command:-eval('rm-rf*')

