#--------------------------FOR LOOP-----------------------------------------------------
# The for loop is usefull to iterate over the elements of sequence such as string ,list
# tuple etc.

st="ANKIT"
for i in st:
    print(i)

#---------------------------FOR LOOP WITH RANGE-----------------------------------------
a=range(5)
for i in a:
    print(i)

a=range(1 , 5)
for i in a:
    print(i)

a=range(1 , 10 , 2)
for i in a:
    print(i)

a=range(10,0,-1)
for i in a:
    print(i)

st="ANKIT"
n=len(st)
for i in range(n):
    print(i,"=",st[i])

#-----------------------------FOR LOOP WITH ELSE----------------------------------------
# The for loop is usefull to iterate over the elements of sequence such as string,list,
#tuple etc.The else suite will be always execuited irrespective of the statements in the
#loop are executed or not.

st="ANKIT"
for i in st:
    print(i)
else:
    print("DONE !")

#-------------------------------NESTED FOR LOOP-----------------------------------------
# for loop inside another for loop is known as nested for loop.

for i in range(2):
    print("outer loop",i)
    for j in range(3):
        print("inner loop",i)