# Unpick.py
# Reading object from the file
import pickle,student1
with open('student1.dat',mode='rb') as f:
    while True:
        try:
            obj=pickle.load(f)
            obj.disp()
        except EOFError:
            print('Done')
            break

