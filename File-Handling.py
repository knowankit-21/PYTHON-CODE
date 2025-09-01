#----------------------------------Files------------------------------------------------
# File is the collection of data that is available to a program .We can retrieve and use
# data stored in a file whenever we required.

# Advantages:-
#1.Stored Data is permanent unless someone remove it.
#2.Stored data can be shared.
#3.It is possible to update or remove the data.

#                                    Type of Files
# There are two types of file:-
# 1.Text-File-It stores data in the form of charachters. It is used to store characters
# and strings.

#2.Binary File-It stores data in the form of bytes,a group of 8 bits each.It is used to store
# text,images,pdf,csv,video and audio.

#Example:-
f=open('student.txt',mode='w')
f.write('Hello How are you')
f.close() # store in cooding file

#-----------------------------------Text Mode and Binary Mode---------------------------
# Text Mode:-A file opened in text mode,treats its contents as if it contains text
# string of the str type.

# When you get data from a text mode file,Python first decodes the raw bytes using either
# a platform-dependent encoding or,specified one.

#Binary Mode:-A file opened in Binary Mode, Python uses the data in the file without
# any deconding , binary mode file reflects the raw data int he file.

# Example:-
f=open('Ankit.txt',mode='w')
f.write('Hello\n')
f.write('Ankit\n')
f.write('Hello How are you')
f.close()
print('writing success')

# Text Mode
f=open('Ankit.txt',mode='r')
data=f.read()
print(data)
f.close()

# Binary Mode
f=open('Ankit.txt', mode='rb')
data = f.read()
print()
f.close()

#------------------------------------opening a files------------------------------------
# If we want to use a file or its data,first we have to open it.

# open()-Open() function is used to open a file. It returns a pointer to the beginning
# of the file.
# This is called file handler or file object.

# syntax:-open('filename',mode='r','buffering,encoding=None,errors=None,newline=None,closefd=True,
# opener=None)

# filename-It represents a name of a file.

# mode-It represents the purpose of opening the file.It defaluts to 'r' which means open for
# reading in text mode.

# buffering-It is an integer value used to set the size of the buffer for the file.In the
# binary mode we can pass 0 as bufferning integer to inform not to use any bufferning .In
# text mode we  can pass 1 for bufferning to retrieve data from the file one line at a time.
# we can pass any positive integer.Default is 4096 or 8192  bytes.

# encoding-name of the enconding used to decode or encode the file.It should be used only in
# text mode. Ex:-utf-8

# errors-an optional string that specifies how encoding and decoding errors are to be handled
# this cannot be used in binary mode.some of the standard values are strict,ignore,replace etc.

# newline-this parameter controls how universal newline mode works (it only applies to text mode).
# It can be None,'','\n','\r', and '\r\n'.

# closefd-If closefd is False and a file descriptor rather than a filename was given, the
# underlying file descriptor will be kept open when the files is closed.If a filename is given
# closefd must be True (the default) otherwise an error will be raised.

# opener-A custom opener can be used by passing a callable as opener.

# f=open('student.txt','w')

f=open('student.txt')
print(f)

#--------------------------------Text File Mode-----------------------------------------

# (r) - Open for reading.The file pointer is positioned at the beginning of the file.If the
# doesnot exist it will show FileNotFoundError.

# (w) - Open for writing.If any data is already present int he file,it will overwrite the data. if
# the file does not exist it will create that file.

#(x) - Open for exclusive creation with write.The specified file must not be available,if the
# specified file is available it will show error FileExistsError.

#(a) - Open for appending.The file pointer is positioned at the end of the file.It appends new
# data at the end of file.If the file does not exists it will create a new file for writing data.

#(r+) - Open for reading and then writing.

#(w+) - Open for writing and then reading. it will overwrite existing data.

#(a+) - Open for appending then reading . it won't(will not) overwrite existing data.

#                                     Binary File Mode

#(rb) - Open for reading.The file pointer is positioned at the beginning of the file. If
# the file doesnot exist it will show FileNotFoundError.

#(wb) - Open for writing .if any data is already present in the file,it will overwrite the data.
# if the file doesnot exist it will create that files.

#(xb) - Open for exclusive creation with write.The specified file must not be available, if the
# specified file is available it will show error FileExistError.

#(ab) - Open for appending. The file pointer is positioned at the end of the file.it appends
# new data at the end of file. If the file does not exist it will create a new file for writing data.

#(rb+) - Open for reading and then writing.

#(wb+) - Open for writing and then reading. It will overwrite existing data.

#(ab+) - Open for appending then reading.It will not overwrite existing data.

#-----------------------------Closing a File--------------------------------------------
# close() - This method is used to close,opened file.
# Once we close the file, file object is deleted from the memory  hence file willbe no
# longer accessible unless we open it again.
# if you do not explicitly close a file,Python garbage collector will eventually destory
# the object and close the open file for you but the file may stay open for a while so you
# should always close opened file.

# What will happened if we do not close opened file:-

# Data of the file may be corrupted or deleted.
# Memory utilized by the files is not freed it may cause of insufficient memory.

f=open('Ankit.txt')
# Operation
f1=open('Ankita.txt')



f.close()
f1.close()

#------------------------------File object variable-------------------------------------
# name-This shows the name of specified file.
# Syntax:-file_object.name

# Mode-This shows mode (purpose) of the file.
# Syntax:-file_object.mode

# closed -This used to check whether file has closed or not.
# It shows True if file is closed else shows False.
# Syntax:-file_object.closed

#                              File object Methods
# readable()-This method is used to check whether file is readable or not.
# it returns True if file is readable else returns False.
# Syntax:-file_object.readable()

# writable()-This method is used to check whether file is writable or not .
# it returns True if file is writable else return False.

# Exapmle:-1
f=open('student.txt',mode='r',encoding='utf-8')
print('File Name:',f.name)
print('File Mode:',f.mode)
print('File Readable:',f.readable())
print('File Writable:',f.writable())
print('File Closed:',f.closed)
f.close()
print('File Closed:',f.closed)

#Example:-2
f=open('student.txt',mode='w',encoding='utf-8')
print('File Name:',f.name)
print('File Mode:',f.mode)
print('File Readable:',f.readable())
print('File Writable:',f.writable())
print('File Closed:',f.closed)
f.close()
print('File Closed:',f.closed)

#Example:-3
f=open('student.txt',mode='a',encoding='utf-8')
print('File Name:',f.name)
print('File Mode:',f.mode)
print('File Readable:',f.readable())
print('File Writable:',f.writable())
print('File Closed:',f.closed)
f.close()
print('File Closed:',f.closed)

#Example:-4
f=open('student.txt',mode='x',encoding='utf-8')
print('File Name:',f.name)
print('File Mode:',f.mode)
print('File Readable:',f.readable())
print('File Writable:',f.writable())
print('File Closed:',f.closed)
f.close()
print('File Closed:',f.closed)

#Exapmle:-5
f=open('student.txt',mode='r+',encoding='utf-8')
print('File Name:',f.name)
print('File Mode:',f.mode)
print('File Readable:',f.readable())
print('File Writable:',f.writable())
print('File Closed:',f.closed)
f.close()
print('File Closed:',f.closed)#

#Exapmle:-6
f=open('student.txt',mode='w+',encoding='utf-8')
print('File Name:',f.name)
print('File Mode:',f.mode)
print('File Readable:',f.readable())
print('File Writable:',f.writable())
print('File Closed:',f.closed)
f.close()
print('File Closed:',f.closed)

#Exapmle:-7
f=open('student.txt',mode='a+',encoding='utf-8')
print('File Name:',f.name)
print('File Mode:',f.mode)
print('File Readable:',f.readable())
print('File Writable:',f.writable())
print('File Closed:',f.closed)
f.close()
print('File Closed:',f.closed)

#                              Checks file exists or not
# isfile()-This method is used to check whether specified file is exists or not.
# This methods belongs to path module which is sub module of os module.

# Syntax:-
# import os
# os.path.isfile(filename)

#Example:-1
import os
print(os.path.isfile('student.txt')) # if file exists output True

#Example:-2
import os
print(os.path.isfile('ankit.taxt')) # if file not exists output False

#example:-3
import os
if os.path.isfile('student.txt'):
    f=open('student.txt')
    print("File opened")
    f.close()
else:
    print("File Not Found")

#Example:-4
import os
if os.path.isfile('ankit.txt'):
    f=open('student.txt')
    print("File opened")
    f.close()
else:
    print("File Not Found")

#---------------------------Writing Data to the file-1----------------------------------
# write()-This method is used to store/write.character or string into the file represented
# by the file object.It returns the number of character written.

# Syntax:-file_object.write(string)

#Example:-1
f = open('ankit.txt',mode='w')
f.write('Hello') # kitne bar v run kr lo hello change nhii hoga use W
f.close()

#Example:-2
f = open('ankit.txt',mode='w')
p=f.write('Hello')
print(p)  # how many letter written in hello word
# use a in mode pehla helo likha toh woh v add hoga or jo pehla likha tha woh v rhe ga
# hello k age append kr dega
f.close()

#Example:-3
f = open('ankit.txt',mode='w')
f.write('Hello Everyone!')
f.write('My name is')
f.write('Ankit Sharma')  # print as no space
f.close()

#Example:-4
f = open('ankit.txt',mode='w')
f.write('Hello Everyone! ')
f.write('My name is ')
f.write('Ankit Sharma ') # print word  b\w space
f.close()

#Example:-5
f = open('ankit.txt',mode='w')
f.write('Hello Everyone!\n')
f.write('My name is\n')
f.write('Ankit Sharma')
f.close()

# mode=x has written in new file not working in same file, har time new file chaiye isse.
# \n means new line

#------------------------------Writing Data to the file-2-------------------------------
# writelines()-This method is used to store/write group of string (list,tuple,set) into
# the file represented by the file object.

#Syntax:-file_object.writelines(group of string)

#Example:-1
f =open("student.txt",mode='w')
list=['AN','VA','DI','SH','TA']
f.writelines(list)
f.close()
print('success')

#Example:-2
f =open("student.txt",mode='w')
list=['AN','VA','DI','SH','TA']
f.writelines(list)
f.close()
print('success')

f =open("student.txt",mode='a')
list=['AN\n','VA\n','DI\n','SH\n','TA\n']
f.writelines(list)
f.close()
print('success')

#-----------------------------Reading Data from file------------------------------------
# read(size)-This method is used to read data/content from a file and returns it as string
# in text mode or bytes objects in binary mode.

# Syntax:-file_object.read(size)
# Where size represents the number of bytes to be read from the beginning of the file.
# when size is omitted or negative,the entire contents of the file will be read and
# returned.
# if the end of the file has been reached , file_object.read() will return an empty
# sting('')

#Example:-1
f=open('student.txt',mode='r')
data=f.read()
print(data)
f.close()
print('completed!!')

#Example:-2
f=open('student.txt',mode='r')
data=f.read(2)   # only print two letter
print(data)
f.close()
print('completed!!')

#Example:-3
f=open('student.txt',mode='r')
data1=f.read(2)
data2=f.read(2)
print(data1)
print(data2)
f.close()
print('completed!!')

#----------------------------------Reading Data from file-2-----------------------------
# readline()-This method is used to read single line from a file.
# Syntax:-file_object.readline()

# readlines()-This method is used to read all lines from a file.It will returns list of line.
# Syntax:-file_object.readlines()

#Example:1
f = open('student.txt',mode='r')
data1=f.readline()
data2=f.readline()
print(data1)
print(data2)
f.close()

#Example:-2
f = open('student.txt',mode='r')
data1=f.readlines()
print(data1)
f.close()

#Example:-3
f = open('student.txt',mode='r')
data1=f.readlines()
for i in data1:
    print(i)
f.close()

#---------------------------Tell methods------------------------------------------------
# tell()-This method is used to find cureent position of file pointer from beginning of the
# file.Position starts from 0.
# Syntax:-file_object.tell()

#Example:-1
f = open('student.txt',mode='r')
print(f.tell())
data1=f.read(3)
print(data1)
print(f.tell())
data2=f.read(2)
print(data2)
print(f.tell())

#                              seek method
# seek()-This method is used to move file pointer from one position to another position
# from beginning of the file.Position starts from 0 and it must be positive integer.
# Syntax:-file_object.seek(position)

#Example:-1
f = open('student.txt',mode='r')
print(f.tell())
f.seek(7)
print(f.tell())
data=f.read()
print(data)

#Example:-2
f = open('student.txt',mode='r')
print(f.tell())
f.seek(7)
print(f.tell())
data=f.read()
print(data)

#-----------------------------------Text file mode--------------------------------------
#(r+)-open for reading and then writting.
#(w+)-open for writting and then reading.It will overwise existing data.
#(a+)-open for appending then reading.It won't overwrite existing data.

#Read then write
f = open('student.txt',mode='r+')
print(f.tell())
data=f.read()
print(f.tell())
f.write('youtube')
print(f.tell())
print(data)
print(f.tell())

# Writting and then reading It will overwrite existing data.
f = open('student.txt',mode='w+')
print(f.tell())
f.write('youtube')
print(f.tell())
f.seek(0)
print(f.tell())
data=f.read()
print(f.tell())
print(data)

#Appending and then reading It won't overwrite esisting data
f = open('student.txt',mode='a+')
print(f.tell())
f.write('youtube')
print(f.tell())
f.seek(0)
print(f.tell())
data=f.read()
print(f.tell())
print(data)

#-----------------------------How to copy File contents in python-----------------------
f1 = open('student.txt',mode='r')
f2 = open('student1.txt',mode='w')
data=f1.read()
f2.write(data)
f1.close()
f2.close()

#----------------------------------With statement---------------------------------------
# The with statement can be used while openning a file.
# When we open a file using with statement there is no need to close the file explicity.

#Syntax:-with open('file_name',mode='r')as file_object:
#                statements

#Ex:-
# with open('student1.txt',mode='r')as f:
#               f.read()

with open('student1.txt',mode='r') as f:
    data = f.read()
    print(data)
    print(f.closed)
print(f.closed)

