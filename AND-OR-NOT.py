#----------------------------------AND--------------------------------------------------
#(1) Use of Logical AND with if statement

#-> Used to combine multiple conditions into a single expression.
#-> Helps in avoiding nested if statements.

age=20
nationality = 'Indian'

if age>18 and age<30 and nationality == 'Indian':
    print('You are eligible for the exam.')

#(2) Logical AND with if-else Statement

#-> If any one conditions is not satisfied, then else block will be executed.

age=32
nationality = 'Indian'

if age>18 and age<30 and nationality == 'Indian':
    print('You are eligible for the exam.')
else:
    print('You are not eligible for the exam.')

#(3) Logical AND with-elif-else statement

age=32
nationality = 'American'

if age>18 and age<30 and nationality == 'Indian':
    print('You are eligible for the exam. Exam fee is ₹1500')

if age>18 and age<30 and nationality == 'American':
    print('You are eligible for the exam.Exam fee is $50.')
else:
    print('You are not eligible for the exam.')

#---------------------------------------OR----------------------------------------------
#(1) Logical OR with is statement

#-> If any of the conditions are satisfied,then the statements inside the if block will be
# executed.

today = 'sunday'
if today == 'saturday' or today == 'sunday':
    print('Its a weekend !')

#(2) Logical OR with if-else statement

today = 'sunday'
if today == 'saturday' or today == 'sunday':
    print('Its a weekend !')
else:
    print('Its is a weekday !')

#(3) Logical OR with if-elif-else statement

today='Tuesday'
if today == 'saturday' or today == 'sunday':
    print('Its a holiday !')
elif today == 'Monday' or today == 'friday':
    print('work 2 hours extra !')
else:
    print('Normal work hours !')

#---------------------------------------NOT---------------------------------------------
#(1) Logical NOT with a Boolean value

#-> If the Boolean value is True, then the Not operator return False.

x=False
if not x:
    print('x is false.')

#(2) Logical NOT with a string

#-> If the string is empty, then the NOT operator will return True.

name='ankit'
if not name:
    print('No name !')
else:
    print(f"Your name is {name}.")

name=''
if not name:
    print('No name !')
else:
    print(f"Your name is {name}.")

#(3) Logical NOT with a List,Dictionary or tuple

#-> If a list,dictionary or tuple is empty then the NOT operators will return True.

name=['ankit','Himanshu','Diwas','Anshul']
if not name:
    print('No name')
else:
    print(f"There are a total of {len(name)} name.")


name=[]
if not name:
    print('No name')
else:
    print(f"There are a total of {len(name)} name.")







