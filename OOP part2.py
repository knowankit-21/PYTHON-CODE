# write OOP classes to handle the following scenarious:-
# 1. A users can create and view 2D coordinate
# 2. A users can find out the distance between 2 coordinate
# 3. A users can find the distance of a coordinate from origin
# 4. A users can check if a point lies on a given line
# 5. A users can find the dostance between a given 2D point and a given line

class Point:

    def __init__(self,x,y):
        self.x_cod = x
        self.y_cod = y

    def __str__(self):
        return "<{},{}>".format(self.x_cod,self.y_cod)

    def euclidean_distance(self,other):
        return((self.x_cod - other.x_cod)**2 + (self.y_cod - other.y_cod)**2)**0.5

    def distance_from_origin(self):
        #return (self.x_cod**2 + self.y_cod**2)**0.5
        return self.euclidean_distance(Point(0,0))

class line:

    def __init__(self,A,B,C):
        self.A = A
        self.B = B
        self.C = C

    def __str__(self):
        return "{}x + {}y + {} = 0".format(self.A,self.B,self.C)

    def point_on_line(line,point):
        if line.A*point.x_cod + line.B*point.y_cod + line.C==0:
          return "Lies on the line"
        else:
            return "Does not lies on the line"

    def shortest_distance(line,point):
        return abs(line.A*point.x_cod + line.B*point.y_cod + line.C)/(line.A**2 + line.B**2)**0.5

    l1 = line(1,1,-2)
    p1 = Point(1,10)
    print(l1)
    print(p1)

    print(l1.shortest_distance(p1))
#---------------------------------------------------------------------------------------------------

# How objects access attributes

class Person:

    def __init__(self,name_input,country_input):
        self.name = name_input
        self.country = country_input

    def greet(self):
        if self.country == "india":
            print("Namaste",self.name)
        else:
            print("Hello",self.name)

# How to access attributes:-
p = Person("nitish","india")

print(p.name)

# How to access methods:-
print(p.greet())

# what if i try to access non-existent attributes

#print(p.gender()) Not working bcos gender is not inside the class

#Attributes crreation from outside of the class

p.gender = "male"

#---------------------------------------------------------------------------------------

# Reference variable
#1. Reference variable hold the objects
#2. We can create objects without reference variable as well
#3. An objects can have multiple reference  variable
#4. Assigning a new reference varibale to an existing objects does not create a new object

# object without a reference
class Person:

    def __init__(self):
        self.name="Ankit"
        self.gender = "male"

p = Person()
q=p

# Multiple ref
print(id(p))
print(id(q))

# change attribute value with the help of 2nd object
print(p.name)
print(q.name)
q.name = "anshul"
print(q.name)
print(p.name)

#---------------------------------------------------------------------------------------

#Collection of objects

# 1.list of objects
class Person:

    def __init__(self,name,gender):
        self.name = name
        self.gender = gender

p1 = Person('nitish','male')
p2 = Person('ankit','male')
p3 = Person('ankita','female')

L=[p1,p2,p3]

for i in L:
    print(i.name,i.gender)

# 2.dict of objects
class Person:

    def __init__(self,name,gender):
        self.name = name
        self.gender = gender

p1 = Person('nitish','male')
p2 = Person('ankit','male')
p3 = Person('ankita','female')

d = {'p1':p1,'p2':p2,'p3':p3}

for i in d:
    print(d[i].gender)