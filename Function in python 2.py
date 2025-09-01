#-----------------------FUNCTION--------------------------------------------------------
# :-> Function are subprogram which are used to compute a value or perform a task.

#--------------------TYPE OF FUNCTION---------------------------------------------------
# 1.Built-in-Function
#     Ex:-print() , upper() etc
# 2.User defined Function
#     Ex:-def (write function name)

#------------------ADVANTAGE OF FUNCTION------------------------------------------------
# 1.Write once and use it as many times as you need. This provides code reusability.
# 2.Function facilities ease of code maintenance.
# 3.Divide large task into many small task so it will help you to debug code.
# 4.You can remove or add new feature to a function anytime.

#---------------------FUNCTION DEFINITION-----------------------------------------------
#:-> Write can define a function using dwf keyword followed by function name with parentheses.
#:-> This is also called as cresting a function , writing a function ,defining a function.

# -> Syntax:-
#            def Function_name():
#                Local variable
#                block of statement
#                return(variable or expression)

#-> Syntax:-
#             def Function_name(para1,para2...):
#                 Local variable
#                 block of statement
#                 return(variable or expression)

# Note:- Need to maintain proper indentation.

#---------------------------------------------------------------------------------------
# def add():                  def add(y):
#     x = 10                      x = 15
#     y = 20                      c = x + y
#     c = x + y                   print(c)
#     print(c)

#--------------------CALLING A FUNCTION-------------------------------------------------
# def add():                  def add(y):
#     x = 10                      x = 15
#     y = 20                      c = x + y
#     c = x + y                   print(c)
#     print(c)                 add(20)
#add()

#----------------------HOW FUNCTION WORK------------------------------------------------
#:-> The parameter y do not know which type of value they are about to recive till the
# value is passed at the time of calling the function. it means the type of data is determine
#only during runtime not at compile time this is called Dynamic typing.

#---------------------------------------------------------------------------------------

#Write once and use it as many time as you need

#defining a function
def disp():
    name = int(input("enter your name"))
    print(name)
    print("Welcome to",name)
#calling a function
disp()

#---------------------------------------------------------------------------------------

# Divide large task into many small task , helpful for debuging code

# Defining Function

def add():
    x = 10
    y = 20
    c = (x + y)
    print(c)
add()

def sub():
    x = 30
    y = 20
    c = (x-y)
    print(c)
sub()

#---------------------------------------------------------------------------------------

# Function without Argument and parameter
#Dedining a function without parameter
def add():
    x = 10
    y = 20
    c = (x + y)
    print(c)
#Calling a function without Argument
add()
# Function with Argument and parameter
#Dedining a function with parameter
def add(y):
    x = 20
    c = x + y
    print(c)
#Calling a function with Argument
add(10)
#---------------------------------------------
def add(y):
    x = 10.233
    print(x+y)
    print(f"formatted output{x+y:5.2f}")
add(10)

#----------------------------RETURN STATEMENT-------------------------------------------
# :->Return statements can be used to return something from function. In python,it is
# possible to return one or more varibale/values.

# Syntax:
# return(variable or expression);
# Ex:-             def add(y):         def add(y):         def add_sub(y):
# return 50            x=10                x=10                x=10
# return (50)          c=x+y               return x+y          c=x+y
# return (x+y)         return c         sum=add(20)            d=y-x
# return(y)        sum=add(20)          print(sum)             return c,d
# return(2,4)      print(sum)                              sum,sub=add(20)
# return (x,y)                                             print(sum)
#                                                          print(sub)


#Return statemant single value
def add():
    x = 10
    y = 10
    c = x + y
    return c
#calling a function
sum=add()
print(sum)

def add(y):
    x = 10
    return x + y
# calling a function
sum = add(10)
print(sum)

#Return statemant multiple value
def add():
    x = 10
    y = 20
    c = x + y
    d = y - x
    return c,d
# calling a function
sum, sub = add()
print(sum)
print(sub)

#-------------------------------NESTED FUNCTION-----------------------------------------
#:-> When we define one fuction inside another function,it is known as nested function
# or function nesting

def disp():
    print("Disp function")
    def show():
        print("show function")
    show()
disp()

#------------------------------------

def disp():
    def show():
        return "show function "
    result = show() + "Disp function"
    return result

a = disp()
print(a)

#--------------------------------------


def disp(st):
    def show():
        return "show function "
    result = show() + st + " Disp function"
    return result

print(disp('Ankit'))

#--------------------------PASS A FUNCTION AS PARAMETER---------------------------------
def disp(sh):
    return "Disp function" + sh()

def show():
    return "Show function"

result = disp(show)
print(result)

#--------------------------FUNCTION DECORATOR IN PYTHON---------------------------------

