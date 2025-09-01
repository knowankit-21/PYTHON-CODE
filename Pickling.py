# Pick.py
# Storeing object in the file.
import pickle,student1

n=int(input('Enter Number of student:'))
with open('student1.dat',mode='wb') as f:
    for i in range(n):
        name=input("Enter the student name:")
        roll=int(input('Enter the student roll no :'))
        address=input('Enter the student address:')
        student=student1.Student(name,roll,address)
        pickle.dump(student,f)

print('Pickling Done')
