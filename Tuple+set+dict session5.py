#Tuples

#->A tuples in python is similar to a list. The difference between the two is that we cannot change the elements of a tuples
#once it is assigned whereas we can change the elements of a list.

#In short a tuples is an immutable list.A tuples can not be change in any way once  it is created.

#Characterstics
#1.Ordered
#2.Unchanged
#3.Allows dulicapte

#Plan of attack
#1.Creating a Tuple
#2.Accessing items
#3.Editing items
#4.Adding items
#5.Deletiing items
#6.Operations on tuples
#7.Tuples function

#List mai square bracket hota hai or tuples main small bracket

#1.Creating a Tuples
#empty
from networkx import reverse


t1=()
print(t1)
#create a tuple with a single item
t2=(2,)
print(t2)
#Homo
t3=(1,2,3,4)
print(t3)
#Hetro
t4=(1,2.3,'hello',True)
print(t4)
#2D->Tuples
t5=(1,2,3,(5,6))
print(t5)
#using type conversion
t6=tuple('hello')
print(t6)

#2.Accessing items

#same as string or list

#3.Editing items

#not possible in tuples

#4.Adding items

#not possible in tuples

#5.Deletiing items

#not possible agar ap pura tuple ko del karna chhate ho toh ho sakta hai not for single item

#6.Operations on tuples
# + and *
t1=(1,2,3)
t2=(4,5,6)
print(t1+t2)
print(t1*2)
#membership
t1=(1,2,3)
2 in t1
#iteration
t1=(1,2,3)
for i in t1:
    print(i)

#7.Tuples function
#len/sum/min/max/sorted
t1=(2,3,4,5)
print(len(t1))
print(sum(t1))
print(min(t1))
print(max(t1))
print(sorted(t1))
print(sorted(t1,reverse=True))

#Count
t=(1,2,3,4,5)
t1=t.count(5)
print(t1)

#Index
t=(1,2,3,4,5)
t1=t.index(5)
print(t1)

#Difference between tuples and list
#1.Syntax
#2.Mutability
#3.Speed
#4.Memory
#5.Build in functionality
#6.Eroor prone
#7.Usability

#Special syntax
a,b,c=(1,2,3)
print(a,b,c)

a=1
b=2
a,b=b,a
print(a,b)

a,b,*others=(1,2,3,4,5)
print(a,b)
print(others)

#Zipping tiples
a=(1,2,3,4,5)
b=(6,7,8,9)

t1=tuple(zip(a,b))
print(t1)

#Sets
#-> A set is an unordered collection of items. Every set elements is unique (no duplicates) and must be immutable
#(can not be changed),However ,a set itself is mutable. we can add ir remove items from it.
#sets can also be used to perform mathematical set operation like union, intersection symmetric diffrence etc

#characterstic
#1.unordered
#2.mutable
#3.no duclipates
#4. can not contain mutable data types

#Creating sets
#empty
s=set()
print(s)
print(type(s))
# 1D and 2D
s1={1,2,3}
print(s1)
s2={1,2,3,{4,5}}
print(s2) #2D is not possible
#homo and hetro
s3={1,2,3}
print(s3)
s4={1,2,2.5,'hello',(7,8,9)}
print(s4)
#using type conversion
s5=set([1,2,3])
print(s5)
#duplicate are not allowed
s6={1,1,2,2,3,3,4,4}
print(s6)
#set cannot have mutable items
s7={1,2,[3,4]}
print(s7)

s1={1,2,3}
s2={3,2,1}
print(s1==s2)

#Accessing items
s1={1,2,3}
s1=[0:3] #indexing are not allowed

#editing items
#not possible are not allowed

#Adding items
#ADD
s={1,2,3,4}
s.add(5)
print(s)
#Update
s={1,2,3}
s.update([4,5,6])
print(s)

#Deleting items
#del
s={1,2,3}
del s
print()
#dicard
s={1,2,4}
s.discard(2)
print(s)
#remove
s={1,2,3,4,5}
s.remove(2)
print(s)
#pop
s={1,2,3,4,5}
s.pop() # delete random number
print(s)
#clear
s={1,2,3,4,5}
s.clear()
print(s)

#Set operation
#Union(|)
s1={1,2,3,4,5}
s2={4,5,6,7,8}
print(s1|s2)
#Intersection(&)
s1={1,2,3,4,5}
s2={4,5,6,7,8}
print(s1&s2)
#Diffrence(-)
s1={1,2,3,4,5}
s2={4,5,6,7,8}
print(s1-s2)
print(s2-s1)
#Symmetric diffrence(^)
s1={1,2,3,4,5}
s2={4,5,6,7,8}
print(s1^s2)
#Membership test
s1={1,2,3,4,5}
# s2={4,5,6,7,8}
1 in s1
#Iteration
s1={1,2,3,4,5}
# s2={4,5,6,7,8}
for i in s1:
    print(i)

#Set function
#len/max/min/sum/sorted
s={1,2,3,5,6}
print(len(s))
print(max(s))
print(min(s))
print(sum(s))
print(sorted(s))
print(sorted(s,reverse=True))

#Union/Update
s1={1,2,3,4,5}
s2={4,5,6,7,8}

# s1|s2
print(s1.union(s2))
#Update
s1={1,2,3,4,5}
s2={4,5,6,7,8}
T=s1.update(s2)
print(s1)

#intersection/intersection_update
s1={1,2,3,4,5}
s2={4,5,6,7,8}
print(s1.intersection(s2))

s1={1,2,3,4,5}
s2={4,5,6,7,8}
s1.intersection_update(s2)
print(s1)

#Difference/Difference_update
s1={1,2,3,4,5}
s2={4,5,6,7,8}
print(s1.difference(s2))

s1={1,2,3,4,5}
s2={4,5,6,7,8}
s1.difference_update(s2)
print(s1)

#Symmetric_difference/Symmetric_difference_update
s1={1,2,3,4,5}
s2={4,5,6,7,8}
print(s1.symmetric_difference(s2))

s1={1,2,3,4,5}
s2={4,5,6,7,8}
s1.symmetric_difference_update(s2)
print(s1)

#isdisjoint/issubset/issuperset
s1={1,2,3,4}
s2={7,8,5,6}
print(s1.isdisjoint(s2))

s1={1,2,3,4,5}
s2={3,4,5}
print(s1.issubset(s2))

s1={1,2,3,4,5}
s2={3,4,5}
print(s1.issuperset(s2))

#Copy
s1={1,2,3}
s2=s1.copy()

print(s1)
print(s2)

#Frozenset->ek bar banane ke badh na he item add pr jo add hoga woh na he hatha ga
#Frozenset is just an immitable version of a python set object

#Create frozenset
fs=frozenset([1,2,3,4])
print(fs)

fs1=frozenset([1,2,3])
fs2=frozenset([3,4,5])
print(fs1|fs2)

#what works and what does not
#works->all read functions
# does't work ->write operations

#when to use
#2D sets
fs=frozenset([1,2,frozenset([3,4])])
print(fs)

#Dictionary
#->Dictionary in python is a collection of keys values, used to store data values like a map,which, unlike other data types which hold only
# a single value as an element.

#In some language it is known as map or assosiative arryas
#dict={'name':'ankit','age':20,'gender':'male'}

#Characterstics:-
#1.Mutable
#2.Indexing has no meaning
#3.keys can not be duplicate
#4.keys can not mutable items

#Creating Dictionary
#Empty dictionary
d={}
print(d)
#1D dictionary/homo
d1={'name':'ankit','gender':'male'}
print(d1)
#with mixed keys
d2={(1,2,3):1,'hello':'world'}
print(d2)
#2D dictionary ->JSON
s={
    'name':'ankit',
    'collage':'lnct',
    'sem':4,
    'subject':{
        'dsa':50,
        'maths':45,
        'english':34,
    }
}
print(s)
#Using sequence and dict function
d4=dict([('name','ankit'),('age',18),(3,3)])
print(d4)
#duplicate keys
d5={'name':'ankit','name':'ankit'}
print(d5) #Duplicate are not allow
#Mutable items as keys
d6={'name':'ankit',(1,2,3):2}
print(d6) # mutable are not allow

#Accessing items
my_dict={'name':'ankit','age':18}
#Two method:-
print(my_dict['name'])
print(my_dict.get('age'))

#Adding key-value pair
d6={'name':'ankit','age':18}
print(d6)
d6['gender']='male'
print(d6)
d6['weight']=70
print(d6)

#Remove key-value pair
#Pop
d7={'name': 'ankit', 'age': 18, 'gender': 'male', 'weight': 70,3:3}
d7.pop(3)
print(d7)
#Popitem
d8={'name': 'ankit', 'age': 18, 'gender': 'male', 'weight': 70,3:3}
d8.popitem()
d8.popitem() #delete last value of the sentence
print(d8)
#del
d9={'name': 'ankit', 'age': 18, 'gender': 'male', 'weight': 70,3:3}
del d9['name']
print(d9)
#Clear
d10={'name': 'ankit', 'age': 18, 'gender': 'male', 'weight': 70,3:3}
d10.clear()
print(d10)

#Editing key-value pair
d11={'name': 'ankit', 'collage': 'lnct', 'sem': 4, 'subject': {'dsa': 50, 'maths': 45, 'english': 34}}
print(d11)
d11['sem']=1
print(d11)
d11['subject']['dsa']=45
print(d11)

#Dictionary operations
d12={'name': 'ankit', 'collage': 'lnct', 'sem': 4, 'subject': {'dsa': 50, 'maths': 45, 'english': 34}}
'name'in d12

#Method 1.
d={'name':'ankit','age':18,'gender':'male'}
for i in d:
    print(i)
#Method 2.
d={'name':'ankit','age':18,'gender':'male'}
for i in d:
    print(i,d[i])

#Dictionary function
#min/max/sorted/len
d={'name':'ankit','age':18,'gender':'male'}
print(len(d))
print(min(d))
print(max(d))
print(sorted(d))
print(sorted(d,reverse=True))

#items/keys/value
d={'name':'ankit','age':18,'gender':'male'}
print(d.items())
print(d.keys())
print(d.values())

#Update
d1={1:2,3:4,4:5}
d2={4:7,6:8}
d1.update(d2)
print(d1)

#Dictionary comprehension
#{Key:value for vars in iterable}

#Quest:-> print 1st 10 number and their square
s={i:i**2 for i in range(1,11)}
print(s)
#Using existing dict
distance={'delhi':1000,'mumbai':2000,'banglore':3000}
s={key:value*0.62 for (key,value) in distance.items()}
print(s)
#Using Zip
days=["sunday","monday","tuesday","wednesday","thursday","friday","saturday"]
temp_c=[30.3,34.3,43.4,34.3,33.3,23.4,23.2]

dt={i:j for (i,j) in zip(days,temp_c)}
print(dt)
#Using if condition
products={'phone':10,'laptop':10,'charger':0,'tablet':0}
p={key:value for (key,value) in products.items()if value>0}
print(p)
#Nested comprehension
#print tables of number from 2 to 4
t={i:{j:i*j for j in range(1,11)} for i in range(2,5)}
print(t)

























