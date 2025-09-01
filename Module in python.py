#--------------------------------Module-------------------------------------------------
# A module is a file containing Python definitions and statements.
# A module is a file containing group of variable,methods,function and classes etc.
# They are executed only the first time the module name is encountered in an import
# statement.
# The file name is the module name with the suffix.py appended.
# Ex:-mymodule.py

#                             Types Of Module
# User-defined Modules
# Built-in Modules
#        Ex:-array,math,numpy,sys

#                          When And Why Use Module
# Assume that you are building a very large project,it will be very difficult to manage
# all logic within one single file so if you want to separate you similar logic to a
# separate file,you can use module.

# It will not only separate your logics but also help you to debug your code easily code
# easily as you know which logic is defined in which module.

# When a module is developed,it can be reused in any program that needs that module.

#                              Creating a Module

# file name = cal.py
# def add(a,b):
#     return a+b
# def sub(a,b):
#     return a-b

#                                 How To Use Module
# import statement is used to import modules.
# Syntax:-
# import module_name
# import module_name as alias_name
# form module_name import f_name as alias_f_name
# from module_name import*
# NOTE:-Module can import other modules.

#                                  Import Module Name
# This does not enter the names of the functions defined in modules directly in the current
# symbol table;it only enters the modules name there.
# Ex:-import cal

# How to access Methods,Function,Variable and classes?

# Using the modules name you can access the functions.
# Syntax:-module_name.function_name()
# Ex:-
# cal.add(10,20)
# cal.sub(20,10)               # When 2 module having same function name then This import
# add=cal.add                  # module is good approach to use.
# add(10,20)

#                     Import Module Name as alias name
# This does not enter the names of the functions defined in modules directly in the current
# symbol table; it only enters the module name there. If the module name id followed by
# as,then the name following as is bound directly to the imported module.
# Ex:-import cal as c

# How to access Methods,Function,Variables and Classes?

# Using the alias_name you can access the functions.
#Ex:-
# c.add(10,20)
# c.sub(20,10)
# add=c.add
# add(10,20)

#                      From module name import function name
# There is a variant of the import statement that imports names from a modules directly
# into the importing modules symbol table.
# Ex-from cal import add,sub

# How to access Methods, Function,Variable and Classes?

# You can access the function directly by its name.
# Ex-
# add(10,20)

#                      From module name import f name as a name
# Ex-from cal import add as s

# How to access Mehtods,Function,Varaible and Classes?

# You can access the functions directly by its alias name.
# Ex-
# s(10,20)

#                      From module name import*
# This imports all names except those beginning with an underscore(_).
# Ex:- from cal import*

# How to access Mthods,Functions,Variables and Classes?

# You can access the functions directly by its name.
# Ex-
# add(10,20)
# sub(20,10)

#                                    Example:-1
import cal
import second
print("The value of a is:",cal.a)

a=cal.Add(10,15)
print(a)

s=cal.Sub(20,15)
print(s)

#                                    Example:-2
import cal as c
print("The value of a is:",c.a)

a=c.Add(10,15)
print(a)

s=c.Sub(20,15)
print(s)

#                                    Example:-3
from cal import a ,name, add, sub
print(a)
name()
a=Add(10,20)
print(a)

s=Sub(20,10)
print(s)

#                                   Example:-4
from cal import a ,name, add as s, sub
print(a)
name()
a=s(10,20)
print(a)

s=s(20,10)
print(s)

#                                   Example:-5
from cal import*
print(a)

name()

A=Add(10,10)
print(A)

S=Sub(10,10)
print(S)

#                                   Example:-6
import first
import second

print(first.a)
first.name()

print(second.a)
second.name()

#                                    Example:-7
from first import name,a

print(a)
name()

from second import name,a

print(a)
name()

#                                    Example:-8
import first

a=first.Myclass()
a.name()
b=first.Myschool()
b.school()

#                                    Example:-9
import first
import second

N=first.Myclass()
N.name()
print()
S=first.Myschool()
S.school()
print()
C=second.Mycollage()
C.show_name()

#                                      Example:-10
import first
import second

N=first.Myclass()
N.name()
print()
S=first.Myschool()
S.school()
print()
C=second.Myclass()
C.collage()

#                                   Module Search Path
# When a module named cal is imported, the interpreter first searches for a built-in
# module with that name.If not found , it then searches for a file named cal.py in a list
# of directions given by the variables sys.path.

# sys.path is initialized from these locations.
# current Directory
# If not found then searches each directory in the shell variables PYTHONPATH
# If not found then searches installation-dependent default path.

# PYTHONPATH is a list of directory names,with the same syntax as the shell variables
# PATH.


