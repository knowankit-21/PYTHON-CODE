# OPP-> object oriented program,and also help in real world application created .

# OPP topic ->1. Class 2. Object 3. Inheritan 4. Abstraction 5. Polymorphism 6. Encapsulation

# CLASS:-> class is a blue print,and also says classes is set of rule followed by object.
# 1.Data or property
# 2.Functions or behaviour
# Class are two type:
# 1.Built in classes like list,tuple,set string.
# 2. users define classes

# OBJECT:->object is an instance of the class
# object example:-> 1. car----->wagonar
#                  2. sports--->cricket
# Syntax to create an object:-
# objectname=classname()
# wargonr=car()
# cricket=sports()

# pascal case:
# like AnkitKumar, do word ek sath or dono start hoge capital letter se.

# create atm by the help of oop:-
class Atm:
    # constructor
    def __init__(self):
        self.pin = ""
        self.blance = 0

    def menu(self):
        user_input = input("""
    Hi,how can i help you?
    1.press 1 to create pin
    2.press 2 to change pin
    3.press 3 to check blance
    4.press 4 to withrawl
    5.Anything else to exit
""")

        if user_input == "1":
            self.create_pin()
        elif user_input == "2":
            self.change_pin()
        elif user_input == "3":
            self.check_blance()
        elif user_input == "4":
            self.withdraw()
        else:
            exit()

    def create_pin(self):
        user_pin = input("enter your pin")
        self.pin = user_pin

        user_blance = int(input("enter yoyr blance"))
        self.blance = user_blance

        print("pin create successfully")
        self.menu()


def change_pin(self):
    old_pin = input("enter your old pin")

    if old_pin == self.pin:
        # let him to change the pin
        new_pin = input("enter your new pin")
        self.pin = new_pin
        print("change pin successfully")
        self.menu()
    else:
        print("wrong pin")
        self.menu()


def check_blance(self):
    user_pin = input("enter your pin")
    if user_pin == self.pin:
        print("your blance is", self.blance)
    else:
        print("wrong pin")


def withdraw(self):
    user_pin = input("enter the pin")
    if user_pin == self.pin:
        # allow to withdraw amount
        amount = int(input("enter the amount"))
        if amount <= self.blance:
            self.blance = self.blance - amount
            print("withdraw successfully.blance is", self.blance)
        else:
            print("error")
    else:
        print("wrong pin , Try again ")
    self.menu()


# Method Vs Function
# L=[1,2,3]
# len(L) ->Function->bcos it is the outside the list class
# L.append()->Method -> bcos it is the inside the list class

#---------------------------------------------------------------------------------------

class Temp:

    def __init__(self):
        print("hello")

obj = Temp()

#---------------------------------------------------------------------------------------

class Fraction:

  #parameterized constructor:-
    def __init__(self,x,y):
        self.num=x
        self.den=y

    def __str__(self):
        return "{}/{}".format(self.num,self.den)

    def __add__(self,other):
        new_num=self.num*other.den + other.den*self.den
        new_den=self.den*other.den

        return "{}/{}".format(new_num,new_den)

    def __sub__(self,other):
        new_num=self.num*other.den - other.den*self.den
        new_den=self.den*other.den

        return "{}/{}".format(new_num,new_den)

    def __mul__(self,other):
        new_num=self.num*other.num
        new_den=self.den*other.den

        return "{}/{}".format(new_num,new_den)

    def __truediv__(self,other):
        new_num=self.num*other.den
        new_den=self.den*other.num

        return "{}/{}".format(new_num,new_den)

    def convert_to_decimal(self):
        return self.num/self.den


fr1 = Fraction(3,4)
fr2 = Fraction(1,2)

print(fr1 + fr2)
print(fr1 - fr2)
print(fr1 * fr2)
print(fr1 / fr2)
