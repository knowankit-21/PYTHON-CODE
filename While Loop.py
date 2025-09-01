#----------------------LOOP CONTROL SSTATEMENT------------------------------------------
#->Loop control statement are used when a section of code may either be executed a fixed
# number of times, or while some condition is true.

#-----------------------WHILE LOOP------------------------------------------------------
#->The while loop keeps repeating an action until an associated condition returns false.
#Syntax:
#               while (condition):
#                     statement
#               Rest of code

a=1
while a<=10:
    print(a)
    a+=1
#---------------
a=2
while a<=20:
    print(a)
    a+=2

#--------------------------WHILE LOOP WITH ELSE-----------------------------------------
# This repeatedly tests the condition and,if it is True,execures the statement 1;if the
# condition is False (which may be the first time it is tested) the statement 2
# of the else clause, is executed and the loop terminates.The else suite will be always
# executed irrespective of the statemets in the loop are executed or not.

#Syntax:
#             while(condition):
#                   statements 1
#             else:
#                   statements 2
#             Rest of the code

a=1
while a<=5:
    print(a)
    a+=1
else:
    print("while condition false so else part executed")

#---------------------------INFINITE WHILE LOOP-----------------------------------------
#Syntax:
#             while(True):
#                  statement
#             Rest of the code

#              while(True):
#                   statement
#                   if(condition):
#                        break
#               Rest of the code

i=0
while True:
    i+=1
    print(i)
    if (i==3):
        break

#-----------------------------NESTED WHILE LOOP-----------------------------------------
# while (condition):
#       statements
#       while(condition):
#           statements
#       statements
# Rest of code

i=1
while i<=3:
    print("outer Loop", i)
    i+=1
    j = 1
    while j<=5:
        print("Inner Loop", j)
        j+=1

print("Rest of the code")

#Agar tumhe pta ho ki loop kitne baar chalna hai toh for i in range('jitna bar chalna ho'):
#Agar tumhe pta nahi ho kitne bar chalna ho toh while True: ka use kre ge.