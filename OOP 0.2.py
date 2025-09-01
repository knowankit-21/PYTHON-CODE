# -----------------------------CLASS-----------------------------------------------------
# -> A python class is a group of attributes and methods.
# WHAT IS ATTRIBUTES?
# -> Attributes are represented by variable that contains data.
# WHAT IS METHODS?
# -> Method performs an action or task. it is similar to function.

# ----------------------HOW TO CREATE CLASS----------------------------------------------
# class Classname(object):                      class Classname(object):
#    def__init__(self):                               def__init__(self):
#          self.variable_name=value                        self.variable_name=value
#          self.variable_name='value'                      self.variable_name='value'
#    def method_name(self):                           def method_name(self):
#       Body Of Method                                     Body Of Method

# CLASS-class keyword is used to create a class
# OBJECT-object represents the base class name from where all classes in python are derived.
# This class is also dervied from object class. this is optional.
# __init__()-This methid is used to initialize the variable.This is a special method.we do
# not call this method explicitly.
# SELF-self is a variable which refers to current class instance/object.

#--------------------------------RULE---------------------------------------------------
#(1) The class name can be any valid identifier.
#(2) It can not be python reserved word.
#(3) A valid class name start with a letter , followed by any number of letter , number
# or underscores.
#(4) A class name generally strts with capital letter.

#--------------------------HOW TO CREATE A CLASS----------------------------------------
from multiprocessing import Value
from os import fpathconf
from re import M

from zmq import has


class Mobile:
    def __init__(self):
        self.model='RealMe X'
    def show_model(self):
        print('Model;',self.model)

#class Classname:                               class Classname:
#    def __init__(self):                            def __init__(self,f1,f2):
#           self.variable_name=value                      self.variable_name=value
#           self.variable_name='value'                    self.variable_name='value'
#    def method_name(self):                         def method_name(self):
#           Body of method                                 body of method
#    def method_name(self,f1,f2):                   def mehtod_name(self,f1,f2):
#           Body of mehtod                                 body of method

#----------------------------OBJECT-----------------------------------------------------
# 1.Object is class type variable or class instance.To use a class , we should create an
# object to the class.
# 2.Instance creation represents allotting memory necessary to store the actual data of the variable.
# 3.Each time you create an object of a class a copy of each variable defined in the class is created.
# 4.In other words you can say that each object of a class has its own copy of data members defined in
# the class.

#syntax:-
# object_name=class_name()
# object_name=class_name(arg)

#----------------------------HOW TO CREATE AN OBJECT------------------------------------
# class Mobile:
#     def __init__(self):
#         self.model='RealMe X'
#     def show_model(self):
#         print('Model':,self.model)

# realme=Mobile()

#----------------------------------------

# class Mobile:
#     def __init__(self,m):
#         self.model=m
#     def show_model(self):
#         print('Model':,self.model)

# realme=Mobile('RealMe X')

#----------------------------HOW ITS WORKS----------------------------------------------
# realme = Mobile()
# 1. A block of memory is allocated on heap. The size of allocated memory is to be decided from
# the attributes and methods available in the class(Mobile).
# 2. After allocating memory block, the special methods __init__() is called internally .This
# method  stores the initial data into the variables.
# 3. The allocated memory location address of the instance is returned into object(realme).
# 4.The memory loction is passed to self.

#-----------------------------ACCESSING CLASS MEMBER USING OBJECT-----------------------
# We can acces variable and methods of a class using class object or instance of class.

# object_name.variable_name
# realme.model

# object_name.method_name()
# realme.show_model();

# object_name.method_name(parameter_list)
# realme.show_model(1000);

#---------------------------------SELF VARIABLE-----------------------------------------
# 1.self is a default variable that contains the memory address of the current object.
# 2.This variable is used to refer all the instance variable and methid.
# 3.When we create object of a class, the object name contains the memory location of the
# object.
# 4.This memory location is internally passed to self as self knows the memory address of
# the objects so we can access variable and method of object.
# 5.self is the first arguments to any object method because the first argument is always the
# object reference. THis is automatic, whether you call it self or not.

# def __init__(self):
# def show_method(self):

#---------------------------------OBJECT------------------------------------------------
#-Each time you create an object of a class a copy of each variable defined in the class
# is created.

class Mobile:
    def __init__(self):
        self.model='REALME X'
    def show_model(self):
        print('Model:',self.model)

realme = Mobile()
redmi = Mobile()
geek = Mobile()

# Example-1
class Myclass:
    def show(self):
        print("my name is ankit")

x = Myclass()
x.show()

# Example-2
class Myclass(object):
    def show(self):
        print("my name is ankit")

x = Myclass()
x.show()

# Example-3
class Mobile:
    def __init__(self):
        self.model = 'RealMe X'

    def show_model(self):
        print("Model:",self.model)

realme = Mobile()
realme.show_model()

# Example-4
class Mobile:
    def __init__(self):
        self.model = 'RealMe X'

    def show_model(self):
        print("Model:",self.model)

realme = Mobile()
realme.model = 'RealMe Pro2'

print(realme.model)
realme.show_model()

# Example-5
class Mobile:
    def __init__(self):
        self.model = 'RealMe X'

    def show_model(self):
        price=18000
        print("Model:",self.model,"price", price)

realme = Mobile()
realme.model = 'RealMe Pro2'

print(realme.model)
realme.show_model()

# Example-6
class Mobile:
    def __init__(self,m):
        self.model = m

    def show_model(self,p):
        self.price=p
        print("Model:",self.model,"price", self.price)

realme = Mobile('RealMe X')
realme.show_model(1000)

#---------------------------------CONSTRUCTOR-------------------------------------------
#(1)Python supports a special type of method called constructor for initializing the instance
# variable of a class.
#(2)A class constructor,if defined is called whenever a program creates an objects of that class.
#(3)A constructor is called only once at the time of creating an instance.
#(4)If two instance are created for a class , the constructor will be called once for each instance.

#--------------------------------CONTRUCTOR WITHOUT PARAMETER---------------------------
# class Mobile:
#     def __init__(self):
#         self.model='RealMe X'

# realme = Mobile()

#--------------------------------CONTRUCTOR WITH PARAMETER-------------------------------
# class Mobile:
#     def __init__(self,m):
#         self.model=m
# realme = Mobile('RealMe X')

# class Mobile:
#     def __init__(self,m,v=80):
#         self.model=m
#         self.volume=v
# redmi = Mobile('Redmi7s,40')

#Example-1
class Mobile:
    def __init__(self):
        print("Mobile constructor called")

Mobile()

#Example-2
class Mobile:
    #constructor without parameter
    def __init__(self):
        self.model='Realme x'

    def show_model(self):
        print("model:",self.model)

realme=Mobile()
realme.show_model()

#Example-3
class Mobile:
    #constructor
    def __init__(self,m,v=80):
        self.model=m
        self.volume=v

    def show_model(self,p):
        price = p                #Local variable
        print("Model:",self.model,"and price",price)
        print("volume:",self.volume)

#Passing Argument to constructor
realme = Mobile('Realme x')
#Acessing Method from outside class
realme.show_model(1000)

#-----------------------------------TYPES OF VARIABLE-----------------------------------
# 1-Instance variable   AND    2.Class variable/Static variable

#--------------------------------INSTANCE VARIABLE--------------------------------------
# 1. Instance variables are the variables whose separate copy is created in every object.
# 2. Instance variable are defined and initialized using a constructor with self parameter.
# EX-
class Mobile:
    def __init__(self):
        self.model='Realme x'     #<- Instance variable
    def show_model(self):
        print(self.model)
realme=Mobile()

#-------------------------------ACCESSSING INSTANCE VARIABLE----------------------------
#WITH INSTANCE METHOD
# To access instance variable, we need instance methods with self as first parameter then
# we can access instance variable using self.variable_name.
class Mobile:
    def __init__(self):
        self.model='realme x'   #<- Instance variable
    def show_model(self):    #<- Instance method
        self.model      #<-  Accessing Instance variable
realme=Mobile()

#-----------------------------ACCESSING INSTANCE VARIABLE-------------------------------
#OUTSIDE CLASS
# We can access instance variable using object_name.variable_name
class Mobile:
    def __init__(self):
        self.model='realme x'   #<- Instance variable
    def show_model(self):    #<- Instance method
        self.model      #<-  Accessing Instance variable

realme=Mobile()
realme.model           #<-  Accessing Instance variable from outside class

#-----------------------------CLASS VARIABLE/STATIC VARIABLE----------------------------
# class variables are the variable whose single copy is avaiable to all the instance of the class.
# if we modify the copy of the class variable in an instance, it will effect all the copies in the
# other instance.
#ex-
class Mobile:
    fp='YES'    #Class variable
    def __init__(self):
        self.model='Realme X'

    def show_model(self):
        print(self.model)

realme=Mobile()

#--------------------------ACCESSING CLASS/STATIC VARIABLE------------------------------
#WITH CLASS METHOD
# To access class variable, we need class methods with cls as first parameter then we can access
# class variable using cls.variable_name.
class Mobile:
    fp='YES'           #class variable
    def __init__(self):
        self.model='Realme x'
    def show_model(self):
        print(self.model)
        @classmethod
        def is_fp(cls):      #class methods
            cls.fp        #Accessing class variable inside class method

realme=Mobile()

#OUT SIDE THE CLASS
# we can access class variable using classname.variable_name
class Mobile:
    fp='YES'       #class variable

    @classmethod
    def show(cls):      #class methods
        cls.fp   #Accessing class variable inside class method

realme=Mobile()

Mobile.fp     #Accessing class variable outside class

#Example-1
class Mobile:
    fp='yes'

    @classmethod
    def is_fp(cls):
        print(cls.fp)

realme=Mobile()
print(Mobile.fp)

#Example-2
class Mobile:
    fp='yes'    #class variable

    def __init__(self):
        self.model='Realme X'    #Instance variable

    def show_model(self):    #Instance Method
        print("Model:",self.model)   #Accessing instance variable

    @classmethod
    def is_fp(cls):
        print("finger print:",cls.fp)   #Accessing class variable

realme=Mobile()
realme.show_model()
Mobile.is_fp()

#----------------------------------NAMESPACE--------------------------------------------
# In python,Namespace represents a memory block where names are mapped to objects.
# Class Namespace-A class maintains its own namespace known as class namespace.In the
# namespace,the names are mapped to class variables.
# Instance Nmaespace-Every instance have its own namespace known as instance namespace.
# In the instance namespace,the names are mapped to instance variables.

class Mobile:
    fp='YES'

    @classmethod
    def is_fp(cls):
        print("Finger print:",cls.fp)

realme=Mobile()
redmi=Mobile()
ankit=Mobile()

print("class FP:",Mobile.fp)
print("Realme:",realme.fp)
print("Redmi:",redmi.fp)
print("ankit:",ankit.fp)
print()
Mobile.fp="No"
print("class FP:",Mobile.fp)
print("Realme:",realme.fp)
print("Redmi:",redmi.fp)
print("ankit:",ankit.fp)
print()
realme.fp="Not working"
print("class FP:",Mobile.fp)
print("Realme:",realme.fp)
print("Redmi:",redmi.fp)
print("ankit:",ankit.fp)

#-----------------------------TYPES OF METHODS------------------------------------------
#1.Instance Methods
#   -Accessor Methods
#   -Mutator Methods

#2.Class Methods
#3.Static Methods

#                             Instance Method
# Instance methods are the methods which act upon the instance variables of the class.
# Instance method need to know the memory address of the instance which is provided
# through self variable by defaults as firts parameters for the instance methods
# syntax:-
# def method_name(self):
#     function body      #Instance methods without parameter/Formal Arguments

# def method_name(self,f1,f2):
#     function body   #Instance variable with parameter/Formal Arguments

#                         Calling Instance Method without Arguments
# Instance methods are bound to object of the class so we call instance methods with object name.
# Syntax:- object_name.methods_name()
# Ex:- realme.show_model()

class Mobile:
    def show_model(self):
        print("Realme x")

realme=Mobile()
realme.show_model()   #calling instance methods w/o arguments

#                           Instance methods with parameter
class Mobile:
    def __init__(self):
        self.model="Realme x"   # Instance variable

    def show_model(self,p):    # Instance methods withs parameter
        self.price=p  # parameter
        print(self.model,self.price)

realme=Mobile()

#                            Calling instance method with arguments
# Syntax:- object_name.methods_name(Actual_arguments)
# Ex:-realme.show_model(1000)
class Mobile:
    def __init__(self):
        self.model="Realme x"
    def show_model(self,p):
        self.price=p
        print(self.model,self.price)

realme=Mobile()
realme.show_model(1000)   # calling methods with arguments

#---------------------------------ACCESSOR AND MUTATOR METHODS--------------------------
#                                  Acessor Methods
# This method is used to access or read data of the variables.This methods do not modify
# the data in the variable. This is also called as getter method.
# Ex-
# def get_value(self):
# def get_result(self):
# def get_name(self):
# def get_id(self):

#Ex-1-------Acessor methods / Getter methods
class Mobile:
    def __init__(self):
        self.model='Realme X'

    def get_model(self):
        return self.model

realme=Mobile()
m=realme.get_model()
print(m)

#                                     Mutator Methods
# This method is used tp access or read and modify data of the variables. This method
# modify the data in the variable.This is also called as setter method.
# EX-
# def set_value(self):
# def set_result(self):
# def set_name(self):
# def set_id(self):

class Mobile:
    def __init__(self):
        self.model='Realme x'

    def set_model(self):
        self.model='Realme 2'

realme=Mobile()
m=realme.set_model()
print(m)

class Mobile:

    def set_model(self,m):
        self.model=m

realme=Mobile()
realme.set_model('Realme x')

# Example-2-----Mutator methods / setter methods
class Mobile:
    def __init__(self):
        self.model='Realme x'  # Instance variable

    def set_model(self):
        self.model='Realme 2'  # Mutator Methods

realme=Mobile()
print(realme.model)
realme.set_model()
print(realme.model)   # calling mutator methods

# Example-3
class Mobile:
    def set_model(self,m):     # Mutator methods
        self.model=m

realme=Mobile()
realme.set_model('Realme x')
print(realme.model)    # calling mutator methods

#-----------------------------CLASS METHODS---------------------------------------------
# Class methods are the methods which act upon the class variables or static variable of
# the class.
# Decorator @classmethod need to write above the class method.
# By default, the first parameter of the class method is cls which refers to the class itself.

# Syntax-

# @classmethod
# def method_name(cls):
#     method body

# @classmethod
# def method_name(cls,f1,f2):
#     method body

#                             Class methods without parameter
class Mobile:
    @classmethod   # Decorator
    def show_model(cls):   # class methods
        print('Realme x')

realme=Mobile()

class Mobile:
    fp='YES'   # class variable
    @classmethod   # Decorator
    def show_model(cls):  # class method
        print(cls.fp)   # Acessing class variable inside class method

realme=Mobile()

#                          calling class method without Argument
# Syntax:-Classname.method_name()

class Mobile:
    @classmethod
    def show_model(cls):
        print("Realme x")

realme=Mobile()
Mobile.show_model()    #calling class method without Arguments

#                           class method with parameter
class Mobile:
    fp="Yes"
    @classmethod
    def show_model(cls,r):  # Defining method with parameter
        cls.ram=r
        print(cls.fp,cls.ram)

realme=Mobile()

#                            calling class method with arguments
# Syntx:-Classname.method_name(Actual_arguments)
#Ex:-Mobile.show_model('4GB')
class Mobile:
    fp="Yes"
    @classmethod
    def show_model(cls,r):
        cls.ram=r
        print(cls.fp,cls.ram)

realme=Mobile()
Mobile.show_model(101)   #calling method with arguments

#Example:-
class Mobile:
    fp="Yes"
    @classmethod
    def show_model(cls,r):
        cls.ram=r
        print("Finger print:",cls.fp)
        print("Ram:",cls.ram)

realme=Mobile()
Mobile.show_model("4GB")

#--------------------------------STATIC METHOD------------------------------------------
# Static method are used when some processing is related to the class but does not need
# the class or its instances to perform any work.
# We use static method when we want to pass some value from outside and perform some action
# in the method.

# Decorator @staticmethod need to write above the static method.

# Syntax:-
# @staticmethod
# def method_name():   # static method without parameter/Formal Arguments
#       method body

# @staticmethod
# def method_name(f1,f2):  # static method with parameter/Formal Arguments
#     method body

#                         Static method without arguments
class Mobile:
    @staticmethod
    def show_model():
        print("Realme X")

realme=Mobile()

class Mobile:
    fp="Yes"
    @staticmethod   #static method
    def show_model():
        print(Mobile.fp)

realme=Mobile()

#                         calling static method without arguments
# Syntx:-Classname.method_name()
class Mobile:
    @staticmethod
    def show_model():
        print("Realme X")

realme=Mobile()
Mobile.show_model()

#                          static method with parameter
class Mobile:
    @staticmethod
    def show_model(m,p):
        model=m
        price=p
        print(model,price)
realme=Mobile()

#                          calling static method with arguments
# Syntx:-Classname.method_name(Actual_arguments)
# Ex-Mobile.show_model(1000)
class Mobile:
    @staticmethod
    def show_model(m,p):
        model=m
        price=p
        print(model,price)

realme=Mobile()
Mobile.show_model("Realme X",1000)

# Example:-
class Mobile:
    @staticmethod
    def show_model():
        print("Realme X")

realme=Mobile()
Mobile.show_model()

# Example:-
class Mobile:
    fp="Yes"
    @staticmethod
    def show_model():
        print("Realme X")
        print("Finger print:",Mobile.fp)

realme=Mobile()
Mobile.show_model()

#--------------------------Passing Member of one class to another class-----------------
class Student:
    def __init__(self,n,r):
        self.name=n
        self.roll=r

#Instance method
def disp(self):
    print("student name:",self.name,)
    print("student roll:",self.roll)

class User:
    #Static method
    @staticmethod
    def show(s):
        print("user name:",s.name)
        print("user roll:",s.roll)

# Creating objects of students class
stu=Student('Ankit',23)
User.show(stu)

#----------------------------------NESTED CLASS-----------------------------------------
# A class within a class is called as nested class or nesting of a class.

# class OuterClassName:
#       def __init__(self):
            # self.variable_name=Value
            # self.innerClassObjectName=self.InnerClassName()
#       def method_name(self):
              # method body

#class InnerClassName:
#      def __init__(self):
#          self.variable_name=value
#      def method_name(self):
#             method body

class Army:
    def __init__(self):
        self.name='Ankit sharma'
        self.age=25
        self.gender='Male'
        self.relationship='unmarried'
        self.location='Kashmir'
        self.From='Bihar,patna'
        self.gn=self.Gun()
    def show(self):
        print("Name:",self.name)
        print("Age:",self.age)
        print("Gender:",self.gender)
        print("Relationship:",self.relationship)
        print("Location:",self.location)
        print("From",self.From)

    class Gun:
        def __init__(self):
            self.name='AK47'
            self.capacity='75 Rounds'
            self.lenght='34.4 inch'
        def disp(self):
            print("Gun Name:",self.name)
            print("Capacity:",self.capacity)
            print("Length:",self.lenght)

a=Army()
a.show()
p=a.gn
p.disp()

#---------------------------------INHERITANCE-------------------------------------------
# This mechanism of deriving a new class from an old one (existing class) such that the
# new class inherit all the members (variables and methods) of old class is called
# inheritance or derivation.

#      Old Class-New Class

#                             Super Class and Sub Class
# The old class is referred to as the super class and the new one is called the sub class.
# Parent class - Base class or Super class
# Child class - Derived class or sub class

# All classes in python are built from a single super class called 'object' so whenever
# we create a class in python object will become super class for them internally.
# class Mobile(object):
# class Mobile:

# The main advantage of inheritance is code reusability.

#---------------------------WHY DO WE NEED INHERITANCE----------------------------------
# class Employee:
#     id=1
#     @classmethod
#     def getid(cls):
#         return cls.id
#     def setname(self,name):
#         self.name=name
#     def getname(self):
#         return self.name
#     def setsalary(self,salary):
#         self.salary=salary
#     def getsalary(self):
#         return self.salary
#     def setovertime(self,ot):
#         self.ot=ot
#     def getovertime(self):
#         return self.ot

# class Manager:
#     id=1
#     @classmethod
#     def getid(cls):
#         return cls.id
#     def setname(self,name):
#         self.name=name
#     def getname(self):
#         return self.name
#     def setsalary(self,salary):
#         self.salary=salary
#     def getsalary(self):
#         return self.salary
#     def setseniorname(self,sname):
#         self.sname=sname
#     def getsniorname(self):
#         return self.sname

#Parent class
# class Employee:
#     id=1
#     @classmethod
#     def getid(cls):
#         return cls.id
#     def setname(self,name):
#         self.name=name
#     def getname(self):
#         return self.name
#     def setsalary(self,salary):
#         self.salary=salary
#     def getsalary(self):
#         return self.salary
#     def setovertime(self,ot):
#         self.ot=ot
#     def getovertime(self):
#         return self.ot

#Child class
#     def setsalary(self,salary):
#         self.salary=salary
#     def getsalary(self):
#         return self.salary
#     def setovertime(self,ot):
#         self.ot=ot
#     def getovertime(self):
#         return self.ot

#---------------------------------TYPES OF INHERITANCE----------------------------------
#1.Single Inheritance
#2.Multli-level Inheritance
#3.Hierarchical Inheritance
#4.Multiple Inheritance

#                             Declaration of child class
# class childclassname(parentclassname):
#          members of child class

# class Mobile(object):
#       members of child class

# class Mobile:

#                              Single inheritance
# If a class is derived from one base class (Parent class), it is called single inheritance.

# oBJECT-FATHER-SON

class Father:
    money=1000
    def show(self):
        print("Parent class instance method")

    @classmethod
    def show_money(cls):
        print("Parent class class method",cls.money)

    @staticmethod
    def stat():
        a=10
        print("parent class static method",a)


class Son(Father):
    def disp(self):
        print("child class instance method")

a=Son()
a.disp()
a.show()
a.show_money()
a.stat()

#------------------------------CONSTRUCTOR IN INHERITANCE-------------------------------
# By default,The constructor in the parent class is available to the child class.
# Example-1
class Father:
    def __init__(self):
        self.money=1000
        print("Father class constructor")

    def show(self):
        print("Father class instance method")

class Son(Father):
    def disp(self):
        print("Son class instance method")

s=Son()
print(s.money)
s.show()
s.disp()

# Example-2
class Father:
    def __init__(self,m):
        self.money=m
        print("Father class constructor")

    def show(self):
        print("Father class instance method")

class Son(Father):
    def disp(self):
        print("Son class instance method")

s=Son(1000)
print(s.money)
s.show()
s.disp()

# Example-3
class Father:
    def __init__(self,m):
        self.money=m
        print("Father class constructor")

    def show(self):
        print("Father class instance method")

class Son(Father):
    def disp(self):
        print("Son class instance method",self.money+1000)

s=Son(1000)
print(s.money)
s.show()
s.disp()

#-----------------------------CONSTRUCTOR OVERRIDING------------------------------------
# If we write constructor in the both classes,parent class and child class then the
# parent class contructor is not available to the child class.
# In this case only class constructor is accessible which means child class constructor
# is replacing parent class constructor.
# constructor overriding is used when programmer want to modify the existing behaviour of a
# constructor.

#Exmaple-1
class Father:
    def __init__(self):
        self.money=2000
        print("Father class constructor")

    def show(self):
        print("Father class Instance method")

class Son(Father):
    def __init__(self):
        self.money=5000
        self.car='BMW'
        print("Son class constructor")

    def disp(self):
        print("Son class instance method")

f=Father()
print(f.money)
f.show()
print()
s=Son()
print(s.money)
print(s.car)
s.disp()

#Example:-2
class Father:
    def __init__(self,m):
        self.money=m
        print("Father class constructor")

    def show(self):
        print("Father class Instance method")

class Son(Father):
    def __init__(self,r):
        self.money=r
        self.car='BMW'
        print("Son class constructor")

    def disp(self):
        print("Son class instance method")

f=Father(2000)
print(f.money)
f.show()
print()
s=Son(5000)
print(s.money)
print(s.car)
s.disp()

#-------------------------------CONSTRUCTOR WITH SUPER MEHTOD---------------------------
# If we write constructor in the both classes, parent class and child class then the parent
# class constructor is not available to the child class.
# In this case only child class constructor is accessible which means child class constructor
# is replacing parent class constructor.
# Super() method is used to all call parent class constructor or methods from the child class.

#Example:-1

class Father:
    def __init__(self):
        self.money=2000
        print("Father class constructor")

    def show(self):
        print("Father class instance method")

class Son(Father):
    def __init__(self):                 #calling parent class constructor
        super().__init__()
        print("Son class constructor")

    def disp(self):
        print("Son class instance method",self.money)

f=Father()
print(f.money)
f.show()
s = Son()
s.disp()

#Example:-2
class Father:
    def __init__(self,m):
        self.money=m
        print("Father class constructor")

    def show(self):
        print("Father class instance method")

class Son(Father):
    def __init__(self,m,j):
        super().__init__(m)         #calling parent class constructor
        self.job=j
        print("Son class constructor")

    def disp(self):
        print("Son class instance method",self.money,"job:",self.job)

f=Father(1000)
print(f.money)
f.show()
s = Son('python',1000)
s.disp()

#------------------------------------MULTI-LEVEL INHERITANCE----------------------------
# In multi-level inheritance,the class inherits the feature of another derived class
# (Child Class).

#Example:-1

class Father:
    def showF(self):
        print("Father class method")

class Son(Father):
    def showS(self):
        print("Son class method")

class GrandSon(Son):
    def showG(self):
        print("GrandSon class method")

g=GrandSon()
g.showG()
g.showS()
g.showF()

#Example:-2

class Father:
    def __init__(self):
        print("Father class constructor")
    def showF(self):
        print("Father class method")

class Son(Father):
    def __init__(self):
        super().__init__()          #calling Father class constructor
        print("Son class constructor")
    def showS(self):
        print("Son class method")

class GrandSon(Son):
    def __init__(self):
        super().__init__()        #calling son class constructor
        print("GrandSon class contructor")
    def showG(self):
        print("GrandSon class method")

g=GrandSon()
g.showG()
g.showS()
g.showF()

#--------------------------------Hierarchical Inheritance-------------------------------
# class Father(object):
#     member of class Father

# class Son(Father):
#     member of class Son

# class Daughter(Father):
#     members of class Daughter

#Example-1

class Father:
    def showF(self):
        print("Father class method")

class Son(Father):
    def showS(self):
        print("Son class method")

class Daughter(Father):
    def showD(self):
        print("Daughter class method")

D=Daughter()
D.showD()
D.showF()

#Example-2


class Father:
    def __init__(self):
        print("Father class constructor")
    def showF(self):
        print("Father class method")

class Son(Father):
    def __init__(self):
        print("Son class constructor")
    def showS(self):
        print("Son class method")

class Daughter(Father):
    def __init__(self):
        print("Daughter class constructor")
    def showD(self):
        print("Daughter class method")

D=Daughter()
F=Father()
D.showD()
D.showF()

#Example-3

class Father:
    def __init__(self):
        print("Father class constructor")
    def showF(self):
        print("Father class method")

class Son(Father):
    def __init__(self):
        super().__init__()
        print("Son class constructor")
    def showS(self):
        print("Son class method")

class Daughter(Father):
    def __init__(self):
        super().__init__()
        print("Daughter class constructor")
    def showD(self):
        print("Daughter class method")

D=Daughter()
D.showD()
D.showF()

#-----------------------------------Multiple Inheritance--------------------------------
# If a class is derived from more then one parent class, then it is called multiple
# inheritance.

# Example-1
class Father:
    def showF(self):
        print("Father class method")

class Mother:
    def showM(self):
        print("Mother class method")

class Son(Father,Mother):
    def showS(self):
        print("Son class method")

s=Son()
s.showF()
s.showM()
s.showS()

#Example-2

class Father:
    def __init__(self):
        super().__init__()
        print("Father class constructor")
    def showF(self):
        print("Father class method")

class Mother:
    def __init__(self):
        super().__init__()
        print("Mother class constructor")
    def showM(self):
        print("Mother class method")

class Son(Father,Mother):
    def __init__(self):
        super().__init__()
        print("Son class contructor")
    def showS(self):
        print("Son class method")

s=Son()
s.showF()
s.showM()
s.showS()

#--------------------------------Method Resolution Order(MRO)---------------------------
# In the multiple inheritance scenario members of class are searched first in the current
# class.If not found,the search continues into parent classes in depth-first,left to right
# manner without searching the same class twice.
# 1.Search for the child case before going to its parent class.
# 2.When a class is inherited from serval classes,it searches in the order from left to
# right in the parent classes.
# 3.It will not visit any class more than once which means a class in the inheritance
# hierarchy is traversed only once exactly.

# s=Son()
# The search will start from Son.As the object of son is created,the constructor of son
# is called.

# Son has super().__init__() inside his contructor so its parent class,the one in the left
# side 'Father' class constructor is called.

# Father class also has super().__init__() inside his constructor so its parent 'object'
# class constructor is called.

# object does not have any constructor so the search will continue down to right hand side
# class(Mother) of object class so mother class constructor is called.

# As mother class also has super().__init__() so its parent class 'object' constructor
# is called but as object class already visited the search will stop here.

#--------------------------------Polymorphism-------------------------------------------
# Polymorphism is a word that came from two greek words,poly means many and morphos means
# forms.
# If a variable,object or method perform different behavior according to situation,it is
#  called polymorphism.

#1.Duck Typing
#2.Operator overloading
#3.Method overloading
#4.Method overriding

#----------------------------------Duck Typing------------------------------------------
# In python,we follow a principle-If'it walks like a duck and talk like a duck,it must be
# a duck'which means python does not care about which class of object it is ,if it is an
# object and required behavior is present for that object then it will work.The type of
# object is distinguished only at runtime.This is called as duck typing.

# Python does not care about which class of object it is,in order to call an existing
# method on an object.If the method is defined on the object,then it will be called.

class Duck:
    def walk(self):
        print("thapak thapak")

class Horse:
    def walk(self):
        print("tabdak tabdak")

class Cat:
    def talk(self):
        print("Meow Meow")

def myfunction(obj):
    obj.walk()


d=Duck()
myfunction(d)
h=Horse()
myfunction(h)

#---------------------------------Strong Typing-----------------------------------------
# We can check whether the object passed to the method has the method being invoked or not.
# hasattr()Function is used to check whether the object has a method or not.
# Syntax:-hasattr(object,attribute)
# where attributes can be a method or variable. if it is found in the object then this
# method returns True else False.

#Example:-1

class Duck:
    def walk(self):
        print("thapak thapak")

class Horse:
    def walk(self):
        print("tabdak tabdak")

class Cat:
    def talk(self):
        print("Meow Meow")

def myfunction(obj):
    if hasattr(obj,'walk'): #using this method do not show error.
        obj.walk()


d=Duck()
myfunction(d)
h=Horse()
myfunction(h)
c=Cat()
myfunction(c)

#Example:-2
class Duck:
    def walk(self):
        print("thapak thapak")

class Horse:
    def walk(self):
        print("tabdak tabdak")

class Cat:
    def talk(self):
        print("Meow Meow")

def myfunction(obj):
    if hasattr(obj,'walk'): #using this method do not show error.
        obj.walk()
    if hasattr(obj,'talk'):
        obj.talk()


d=Duck()
myfunction(d)
h=Horse()
myfunction(h)
c=Cat()
myfunction(c)

#-----------------------------------Method Overloading----------------------------------
# When more than one method with the same name is defined in the same class,it is known as
# method overloading.
# In pyhton,If a method is written such that it can perform more than one task, it is
# called method overloading.

class Myclass:
    def sum(self,a=None,b=None,c=None):
        if a!=None and b!=None and c!=None:
            s = a+b+c
        elif a!=None and b!=None:
            s = a+b
        elif a!=None:
            s = a
        else:
            s = 'Provide at least one digit'
        return s

obj=Myclass()
print(obj.sum(10,10,10))

#----------------------------------Method Overriding------------------------------------
# If we write method in the both classes,parent class and child class then the parent
# class method is not available to the child class.
# In this case only child class method is accessible which means child class method is replacing
# parent class method.
# Method overriding is used when programmer want to modify the existing behaviour of a method.

#Example:-1
class Add:
    def result(self,a,b):
        print("Addition:",a+b)

class Multi(Add):
    def result(self,a,b):
        print("Multiplication:",a*b)

m=Multi()
m.result(10,20)

#Example:-2
class Add:
    def result(self,a,b):
        print("Addition:",a+b)

class Multi(Add):
    pass


m=Multi()
m.result(10,20)

#Example:-3
class Add:
    def result(self,a,b):
        print("Addition:",a+b)

class Multi(Add):
    def result(self,a,b):
        print("Multiplication:",a*b)

m=Multi()
m.result(10,20)

m=Add()
m.result(10,20)

#Example:-4
class Add:
    def result(self,a,b):
        print("Addition:",a+b)

class Multi(Add):
    def result(self,a,b):
        print("Multiplication:",a*b)

m=Multi()
m.result(10,20)

#                              Method with super()Method
# super() method is used to call parent class constructor or methods from the child class.
# Stntx:-super().methodName()
class Add:
    def result(self,a,b):
        print("Addition:",a+b)

class Multi(Add):
    def result(self,a,b):
        super().result(10,20)
        print("Multiplication:",a*b)

m=Multi()
m.result(10,20)

#-------------------------------Operator Overloading------------------------------------
class A:
    def __init__(self,x):
        self.x=x
    def __add__(self,other):
        return self.x + other.x

class B:
    def __init__(self,x):
        self.x = x

a = A(100)
b = B(200)
print(a+b)

#-------------------------------Abstract Class------------------------------------------
# A class derived from ABC class which belongs to abc module, is known as abstract class
# in python.
# ABC class is known as meta class which menas a class that defines the behavior of other
# class classes.so we can say meta class ABC defines that the class which is derived from
# it becomes an abstract class.
# Abstract class can have abstract method and concrete methods.
# Abstract class needs to be extended and its method implemented.
# PVM can not create objects of an abstract class.

# Ex:-from abc import ABC,abstractmethod
# Ex:-class Father(ABC)

#                                Abstract Method
# A abstract method is a method whose action is redefined in the child classes as per the
# requirement of the object.
# We can declare a method as abstract method by using @abstratmethod decorator.

# Ex:-from abc import ABC,abstractmethod
# class Father(ABC):
#      @abstractmethod
#      def disp(self):
#            pass

#                                 Concrete Method
# A concrete method is a method whose action is defined in the abstract class itself.
# Ex:-from abc import ABC, absttractmethod
# class Father(ABC):
#      @abstractmethod
#       def disp(self):
#           pass
#       def show(self):
#          print("Concrete method")

#                                  Rule
#1.PVM can not create objects of an abstract class.
#2.It is not necessary to declare all methods abstract in a abstract class.
#3.Abstract class can have abstract method and concrete methods.
#4.If there is any abstract method in a class,that class must be abstract.
#5.The abstract methods of an abstract class must be defined in its child class/subclass.
#6.If you are inheriting any abstract class that have abstract method, you must
# either provide the implemenation of the method or make this class abstract.

#                                When use Abstract Class
# We use abstract class when there are some common feature shared by all the objects as they
# are.

                              # Defence Force:
                              #      Gun=Ak 47
                              #      Area=

# Army                      Air Force                        Navy
# Gun=AK 47                Gun=Ak 47                        Gun=Ak 47
# Area=Land                Area=Sky                         Area=Sea

# Gun is the common feature shared by all Forces but area is different for them.

# Example:-1
from abc import ABC, abstractmethod

class Father(ABC):
    @abstractmethod
    def disp(self):
        pass

    def show(self):
        print("Concrete method")

class Child(Father):
    def disp(self):
        print("Child class")
        print("Defining Abstract Method")

c=Child()
c.disp()
c.show()

#Example:-2
from abc import ABC, abstractmethod

class DefenceForce(ABC):
    @abstractmethod
    def area(self):
        pass

    def gun(self):
        print("Gun= AK47")

class Army(DefenceForce):
    def area(self):
        print("Area=Land")

class AirForce(DefenceForce):
    def area(self):
        print("Area=Sky")

class Navy(DefenceForce):
    def area(self):
        print("Area=Sea")

a=Army()
af=AirForce()
n=Navy()

a.gun()
a.area()
print()
af.gun()
af.area()
print()
n.gun()
n.area()

#Example:-3
from abc import ABC, abstractmethod

class DefenceForce(ABC):
    def __init__(self):
        self.country='INDIA'
    @abstractmethod
    def area(self):
        pass

    def gun(self):
        print("Gun= AK47")
        print("Country:",self.country) # common part are write here

class Army(DefenceForce):
    def area(self):
        print("Area=Land")

class AirForce(DefenceForce):
    def area(self):
        print("Area=Sky")

class Navy(DefenceForce):
    def area(self):
        print("Area=Sea")

a=Army()
af=AirForce()
n=Navy()

a.gun()
a.area()
print()
af.gun()
af.area()
print()
n.gun()
n.area()

#-----------------------------------Interface-------------------------------------------
from abc import ABC,abstractmethod
class Father(ABC):
    @abstractmethod
    def disp1(self):
        pass
    @abstractmethod
    def disp2(self):
        pass

class Child(Father):
    def disp1(self):
        print("Child class")
        print("Disp 1 Abstarct Method")

class GrandChild(Child):
    def disp2(self):
        print("GrandChild class")
        print("Disp 2 Abstract Method")

gc=GrandChild()
gc.disp1()
gc.disp2()

#-----------------------------------Abstract class vs Interface-------------------------
#1.An abstract class an have abstract methods as well as concrete methods,but all methods
# of an interface are abstract.
#2.We use abstract class when there are some common feature shared by all the objects
# as they are while we use interface if all feature need to be implemented differently
# objects.
# 3.Its programmer job to write child class for abstract class while in interface,any
# third party vendor will take responsibility to write child class.
#4.Interface are slow when compared to abstract class.

#-----------------   -------------Encapsulation-----------------------------------------
# Encapsulation hides the internal state of an object and restricts direct access.

# Syntax:-
class Pen:
    def __init__(self):
        self.name='Ankit'
        self.__colour = 'blue'  # Private (Encapsulation)
        self.age='19'

    def display(self):
        print("Name:",self.name,"colour:",self.__colour,"age:",self.age)

P=Pen()
P.age='18' # age should be change but colour should not be change
P.display()



# Double underscore(__color) makes it private.
# Keeps internal data safe from outside interference.
























