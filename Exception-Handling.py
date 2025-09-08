# WHAT IS EXCEPTION?
#Ans:-An exception is an event which occurs during the execution of program that disrupts
# normal flow of program.
# Situation that python can not cope with it.

#EXAMPLE:-
# num1=10                                        in1=100
# num2=0                                         in2="hello"
# result=num1/num2                               result=in1+in2
# print(result) #ZeroDivisionError               print(result)  #TypeError

# WHY IT IS DANGEROUS?
#1.Lead to sudden termination of program.
#2.Can block the application.
#3.Data loss problem can occur.
#4.Corrupt data files.

# EXCEPTION VS ERROR:-
#1.Errors can not be handled.
#2.Exceptions can be handled using exception handling syntax.
# ex:-print("hello)

#---------------------------------------L2----------------------------------------------

# FOUR TYPE OF EXCEPTION:-
#1.try block
#2.except block
#3.else block
#4.finally block

#Syntax:-
# try:
#     code containing exceptions(suspicious code)
# except (ExceptionName):
#     code to handle exceptions(if occurred)
# else:
#     code to execute if no exceptions occured.
# finally:
#     Always executed

#EXAMPLE:-1
num1=int(input("Enter your 1st number:"))
num2=int(input("Enter your 2nd number:"))
try:
    result=num1/num2
    print(result)
except ZeroDivisionError:
    print("Divide by Zero is not possible:")

#Example:-My code
num1=int(input("Enter your 1st number:"))
num2=int(input("Enter your 2nd number:"))

if num2==0:
    print("Divide by Zero is not possible:")
else:
    result=num1/num2
    print(result)

#EXAMPLE:-2
num1=int(input("Enter your 1st number:"))
num2=int(input("Enter your 2nd number:"))
try:
    result=num1/num2
    print(resul)
except NameError:
    print("Variable missing")

#EXAMPLE:-3 Best Method
num1=int(input("Enter your 1st number:"))
num2=int(input("Enter your 2nd number:"))
try:
    result=num1/num2
    print(result)
except (ZeroDivisionError,NameError) as obj:
    print(obj)

#EXAMPLE:-4
num1=int(input("Enter your 1st number:"))
num2=int(input("Enter your 2nd number:"))
try:
    result=num1/num2
    print(resul)
except:
    print("some thing went wrong")
else:
    print("an exception did not occur")
finally:
    print("Always executed")

#-------------------------------------L3------------------------------------------------
# Print Exception name
#              1.using exception class object.
#              2.using sys module
# which Exception first?

#Example:-5 NameError
num1=int(input("Enter your 1st number:"))
num2=int(input("Enter your 2nd number:"))
try:
    result=num1/num
    print("Division is:",result)
except Exception as var:
    print(var)
    print(var.__class__)

print("Rest of code")

#Example:-6 ZeroDivisionError
num1=int(input("Enter your 1st number:"))
num2=int(input("Enter your 2nd number:"))
try:
    result=num1/num2  # when den is zero
    print("Division is:",result)
except Exception as var:
    print(var)
    print(var.__class__)

print("Rest of code")

#Example:-5 valueError
try:
    num1=int(input("Enter your 1st number:"))
    num2=int(input("Enter your 2nd number:"))

    result=num1/num2
    print("Division is:",result)
except Exception as var:
    print(var)
    print(var.__class__)

print("Rest of code")

#Example:6
import sys
num1=int(input("Enter your 1st number:"))
num2=int(input("Enter your 2nd number:"))
try:
    result=num1/num2
    print("Division is:",result)
except:
    print(sys.exc_info()[0])
    print(sys.exc_info()[1])

#-------------------------------Python raise keyword------------------------------------
# User-defined exceptions:-
# Exceptions created by programmers,

# raise keyword/statement:-
#1.An exceptions can be raised forcefully by using the raise clause in pyhton.
#2.raise statement is used when we want to throw exception for particular condition.

#ex:-input age=-10
#         ValueError: invalid age

#syntax:-raise ExceptionName("exception message")

#EXAMPLE:-1
try:
    age=int(input("Enter your age:"))
    if age<0:
        raise ValueError
    print("Your age is:",age)
except ValueError:
    print("Enter valid age")

#EXAMPLE:2
try:
    age=int(input("Enter your age:"))
    if age<0:
        raise ValueError("plz write positive value")
    print("Your age is:",age)
except ValueError as var:
    print(var)

#---------------------------------------------------------------------------------------
# Write a python program for FiveDivisionError Exception.

#EXAMPLE:1

class FiveDivisionError (Exception):
    #this is exception class called when five division error happens,
    pass
try:
    num1=int(input("Enter your 1st number:"))
    num2=int(input("Enter your 2nd number:"))
    if num2==5:
        raise FiveDivisionError("Can not divided by 5")
    div=num1/num2
    print("Division is:",div)
except (FiveDivisionError,ZeroDivisionError) as f:
    print(f)

#EXAMPLE:2
class FiveDivisionError (Exception):
    #this is exception class called when five division error happens,
    def __init__(self):
        print("Can not divided by five")
    pass
try:
    num1=int(input("Enter your 1st number:"))
    num2=int(input("Enter your 2nd number:"))
    if num2==5:
        raise FiveDivisionError
    div=num1/num2
    print("Division is:",div)
except (FiveDivisionError,ZeroDivisionError) as f:
    print(f,end='')

#---------------------------------------------------------------------------------------
# Requirements:-
#-Withdraw money from bank.
#   -Balance in bank should not be less than 1000.
#   -user account will be blocked for an hour if user put 3 times wrong pin.
import time
class BalanceExceptionError(Exception):
    pass

class AttemptExceptionError(Exception):
    pass
attempts=1

def withdraw():
    global attempts
    saved_pin=1234    #hard-coded
    balance=10000     #hard-coded

    pin=int(input("Enter the pin:"))
    if pin==saved_pin:
        try:
            amt=float(input("Enter the amount to withdraw:"))
            temp_bal=balance-amt
            if temp_bal<1000:
                raise BalanceExceptionError("Insufficient balance")
            balance=balance-amt
            print("Remained balance is:",balance)
        except Exception as var:
            print(var)
    else:
        ans=input("Do you want to continue again:(y/n):")
        if ans.lower()=='y':
            attempts+=1
            try:
                if attempts==4:
                    raise AttemptExceptionError("To many attempts,your account is blocked for an hour")
            except Exception as var:
                print(var)
                time.sleep(3600)
            else:
                withdraw()
        else:
            print("Thank you")
            return

withdraw()

#---------------------------------------------------------------------------------------

try:
    f=open("student.txt",mode="r")
except Exception as var:
    print(var)
else:
    f.close()

#------------------------------------Excepthook in Python-------------------------------
# What happens?

#-the interpreter calls sys.excepthook() with three arguments.

#(1) the exception class
#(2) exception instance/value
#(3) a traceback object

#This function prints out a given traceback and exception to sys.stderr.

import sys
def format_traceback(exc_type,exc_value,exc_trackback):
    print("Something went wrong")
    print(exc_type)
    print(exc_value)
    print(exc_trackback)

sys.excepthook="format_tracekback"
def display():
    print(1+"hello")

display()

#---------------------------------------------------------------------------------------

#(1).Handling exceptions while taking input.

def get_squares():
    try:
        num=int(input("Enter the number:"))  #if you are print hello then error
        print("square is:",num**2)
    except Exception as e:
        print(e)
        get_squares()

get_squares()

print("Rest of the code")

#(2).A pitfall while using exception handling.

try:
    f = open("data1.txt",mode="r")
    my_data = f.read()
    print(my_data)
except Exception as e:
    print(e)
else:
    print("read operation success !")
finally:
    try:
        f.close()
    except:
        pass

#---------------------------------------------------------------------------------------












