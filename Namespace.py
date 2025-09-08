#---------------------------------Topic-------------------------------------------------
#                               Namespaces
#-> A namespace is a space that holds names(identifiers).Programmatically speaking,
# namespace and dictionary of identifiers(keys) and their objects(values)

# There are 4 types of namespaces:
#     1.Local Namespace
#     2.Global Namespace
#     3.Enclosing Namespace
#     4.Builtin Namespace

#                              Scope and LEGB Rule
#-> A scope is a textual region of a python program where a namespace is directly accessible.
#-> The interpreter searches for a name from the inside out, looking in the local,enclosing,
# global, and finally the built-in scope.if the interpreter doesnot find the name in any
# of these locations,then Python raises a Namespace exception.

#---------------------------------Local and Global--------------------------------------

#Ex:-(1) Local and Global

a=2 #Global variable

def temp():
    b=3 #Local variable
    print(b)

temp()
print(a) #First print Local variable then print global variable.

#Ex:-(2) Local and Global-> same name

#-> if the Local and Global variable both are same then
# First print Local variable and print global variable.

a=2 #Global variable

def temp():
    a=3 #Local variable
    print(a)

temp()
print(a) #First print Local variable then print global variable.

#Ex:-(3) Local and Global-> local does not have but global has

#-> Agar local variable na ho or sirf global variable ho toh v print hoga.


a=2 #Global variable

def temp():
    print(a)

temp()
print(a) #First print Local variable then print global variable.

#Ex:-(4) Local and Global-> editing global by the help of local varibale.

#-> In this case not possible to edit global varibale.

a=2 #Global variable

def temp():
    a+=1
    print(a)

temp()
print(a)

#-> To edit the global variable by the help of local variable import global in the local
# variable.

a=2 #Global variable

def temp():
    global a
    a+=1
    print(a)

temp()
print(a)

#Ex:-(5) Local and Global-> global creating inside local

def temp():
    global a
    a=1
    print(a)

temp()
print(a) #First print global

#Ex:-(6) Local and Global-> function parameter is local

def temp(z):
    print(z)

a=5
temp(5)
print(a) # First print local

#---------------------------------Builtin Namespace-------------------------------------

#Ex:-(1) How to see all the built-ins
import builtins
print(dir(builtins))
#-------------------------

L=[1,2,3]
print(max(L)) # To check max number in list

#--------------------------
#Ex:-(2) Renaming built-ins
L=[1,2,3]

def max():
    print('hello')
max(L)

#-------------------------------------Enclosing scope-----------------------------------
#Ex:-(1)
#-> First print inner func then print outer func and then print main func

def outer():
    def inner():
        print('inner function')
    inner()
    print('outer function')

outer()
print('main program')

#Ex:-(2)

def outer():
    a=3
    def inner():
        a=4
        print(a)
    inner()
    print('outer function')

a=1
outer()
print('main program')

# nonlocal keyword

def outer():
    a=1
    def inner():
        nonlocal a
        a+=1
        print('inner',a)
    inner()
    print('outer',a)

outer()
print('main program')
#---------------------------------------------------------------------------------------






