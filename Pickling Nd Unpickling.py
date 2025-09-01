#--------------------------------Pickling-----------------------------------------------
# Pickling is a process of converting a class object into a byte stream so that it can be
# stored into a file.This is also called as object serialization.
# we use pickle module to perform pickling and unpickling

#---------------------------------Pickling Function-------------------------------------
# dump()-This function is used to perform the pickling.It returns the pickled representation
# of the object as a bytes object,instead of writting it to a file.
# This method belongs to pickle module.
#Syntax:-
# import pickle
# pickle.dump(object,file)

#---------------------------------unplicking--------------------------------------------
# unpickling is a process whereby byte stream is converted back into a class onject.
# It is inverse operation of pickling.This is also called as de-serilization.Pickling
# and unpickling should be done using binary files since they support byte streams.

# we use pickle module to perform pickling and unpickling.

# warning:The pickle module is not secure against erroneous or maliciously construted
# data. Never unpickle data received from an untrusted or unauthenticated source.

#-------------------------------Unplicking Function-------------------------------------
# load()-This function is used to read an pickled object from a binary file and returns
# it into object.This method belongs to pickle module.
# Syntax:-
# import pickle
# pickle.load(file)

#--------------------Why do we need pickling nd unpickling------------------------------
# When we store structured data in the file and want to perform calculation that time we
# need pickling and unpickling.

#Example:-1
import pickle

class Student:
    def __init__(self,name,roll,address):
        self.name=name
        self.roll=roll
        self.address=address

    def disp(self):
        print(f'Name:{self.name} Roll:{self.roll} Address:{self.address}')

with open('student3.dat',mode='wb') as f:
    student3=Student('Ankit',101,'J.bad')
    pickle.dump(student3,f)
    print('Pickling Done!!')

with open('student3.dat',mode='rb') as f:
    obj=pickle.load(f)
    print('Unpickling Done!!')
    obj.disp()

#Example:-2

class Student:
    def __init__(self,name,roll,address):
        self.name=name
        self.roll=roll
        self.address=address

    def disp(self):
        print(f'Name:{self.name} Roll:{self.roll} Address:{self.address}')

with open('student3.dat',mode='wb') as f:
    student3=Student('Ankit',101,'J.bad')
    student4=Student('Tanu',102,'Patna')
    pickle.dump(student3,f)
    pickle.dump(student4,f)
    print('Pickling Done!!')

with open('student3.dat',mode='rb') as f:
    obj1=pickle.load(f)
    obj2=pickle.load(f)
    print('Unpickling Done!!')
    obj1.disp()
    obj2.disp()

#Example:-3
import pickle,student5

with open('student3.dat',mode='wb') as f:
    student3=student5.Student('Ankit',101,'J.bad')
    student4=student5.Student('Tanu',102,'Patna')
    pickle.dump(student3,f)
    pickle.dump(student4,f)
    print('Pickling Done!!')

with open('student3.dat',mode='rb') as f:
    obj1=pickle.load(f)
    obj2=pickle.load(f)
    print('Unpickling Done!!')
    obj1.disp()
    obj2.disp()

#Example:-4 done in another file line,student1,pickling.py,unplickling,py
