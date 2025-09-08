#-----------------------------------Topic-----------------------------------------------
#(1) INTRODUCTION
#-> Decides whether a particular statement or block of statements will be executed or not.
x=10
if x<50:
    print("x is less than 50")

#(2) THE STATEMENT OUTSIDE IF BLOCK
#-> The statement outside if block will be executed regardless of whether the condition
# in the if statement is satisfied or not.

x=60
if x<60:
    print("x is less than 50")
print("End of the program")

#(3) THE SHORT HAND IF
#-> When only one statement to execute,put that in the same line as the if statement.

x=10
if x<50: print("x is less than 50")
print("End of the peogram")

#(4) NESTED IF STATEMENT
#-> The if statement inside another if statement is called nested if statement.

x=10
if x<50:
    if x==10:
        print("x is equal to 10")
    print("x is less than 50")
print("End of the program")

#----------------------------------Lecture2---------------------------------------------
#(1) INTRODUCTION
#-> The else statement can be used with if statement to execute a block of code when the
# if condition is not satisfied.
age=20
if age<=18:
    print('You can not vote !')
else:
    print('You can vote !')

#(2) THE SHORT HAND IF-ELSE
#-> Used when only one statement for if and one statement for else needs to be executed.
age=20
print('You can not vote !') if age<=18 else print('You can vote !')

#------------------------------------Lecture3-------------------------------------------
#(1) INTRODUCTION
#-> The if-else statement is used when decision has to be made among two alternatives.
#-> The if-elif-else statement is used when decision has to be made between more than two
# alternatives.
x=10
if x==5:
    print('x is 5')
elif x<5:
    print('x is less than 5')
else:
    print('x is greater than 5')

#(2) DIVISIBILITY TEST
#-> WAP to test whether a number is divisible by 2 or 3.
n=17
if n%2==0:
    print('Number is divisible by 2')
elif n%3==0:
    print('Number is divisible by 3')
else:
    print('Number is neither divisible by 2 nor 3')

