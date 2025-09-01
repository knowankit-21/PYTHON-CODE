# Lists in python
# 1.what are list?
# 2.lists vs Arrays
# 3.characterstics of a list
# 4.how to creat list
# 5.access items from a list
# 6.editing items in a list
# 7.deleting items from a list
# 8.operations in list
# 9.functions on list

# 1.What are lists?
# ->Lists is a data type where you can store multiple items under 1 name.More technically
# lists act like dynamic array which means you can add more items on the fly..
# l=[20,'ankit',35.25,[30,60,90]]

# 2.Lists VS Arrays
# 1->Arrays are fixed in size but lists are not fixed in size.
# 2->Arrays are homogeneous but lists are heterogeneous.
# 3->Arrays are more faster than lists .which means python lists are slower
# 4->lists occupie more space than arrays

L = [1, 2, 3]

print(id(L))
print(id(L[0]))
print(id(L[1]))
print(id(L[2]))
print(id(L[3]))
print(id(1))
print(id(2))
print(id(3))

# 3.characterstics of a list
# 1.Ordered
# 2.Changeble/Mutable
# 3.Hetrogeneous
# 4.Can have dulcipate
# 5.Are Dynamic
# 6.can be nested
# 7.items can be Accessd
# 8.can contain any kind of objects in python

# 4.How to creat list
# 1.Empty
print([])
# 2.1D ->Homo
print([1, 2, 3, 4, 5])
# 3.2D ->Hetero
print([1, 2, 3, [4, 5]])
# 4.3D ->Homo
print([[[1, 2], [3, 4], [5, 6]]])
# 5.Hetrogenous
print([1, True, 4.5, 3 + 3j, "hello"])
# 6.Using type conversion
print(list("hello"))

# 5.Accessing items from a list
# 1.Indexing
L = [1, 2, 3, 4]
print(L[0])
L = [1, 2, 3, 4]
print(L[3])
L = [1, 2, 3, 4]
print(L[-2])
L = [1, 2, 3, [4, 5]]
print(L[-1])
L = [1, 2, 3, [4, 5]]
print(L[-1][-2])
L = [1, 2, 3, [4, 5]]
print(L[3][0])
L = [[[1, 2], [3, 4]], [[5, 6]]]
print(L[0][1][1])

# Slicing
L = [1, 2, 3, 4, 5]
print(L[0:3])
L = [1, 2, 3, 4, 5]
print(L[-3])
L = [1, 2, 3, 4, 5]
print(L[0::2])
L = [1, 2, 3, 4, 5]
print(L[::-1])

# Adding items to lists

# append
L = [1, 2, 3, 4, 5]
L.append(6)
print(L)

# extend
L = [1, 2, 3, 4, 5]
L.extend([6, 7, 8])
print(L)

# Insert
L = [1, 2, 3, 4, 5]
L.insert(1, 100)
print(L)

# 6.editing items in a list
L = [1, 2, 3, 4, 5]
# editing with indexing
L[-1] = 100
# editing with slicing
L[1:4] = [200, 300, 400]
print(L)

# 7.deleting items from a list
# del
L = [1, 2, 3, 4, 5]
# Indexing
del L[-1]
print(L)
# Slicing
L = [1, 2, 3, 4, 5]
del L[1:3]
print(L)
# remove
L = [1, 2, 3, 4, 5]
print(L)
L.remove(5)
# pop
L = [1, 2, 3, 4, 5]
L.pop()
print(L)
# clear
L = [1, 2, 3, 4, 5]
L.clear()
print(L)

# 8.operations in list
# Arithmetic / only use + and *
L1 = [1, 2, 3, 4, 5]
L2 = [6, 7, 8, 9, 10]
print(L1 + L2)

L1 = [1, 2, 3, 4, 5]
L2 = [6, 7, 8, 9, 10]
print(L1 * 2 + L2)

# loops
L1 = [1, 2, 3, 4, 5]
L2 = [1, 2, 3, [4, 5]]
L3 = [[[1, 2], [3, 4]], [[5, 6]]]

for i in L1:
    print(i)
for i in L2:
    print(i)
    for i in L3:
        print(i)

# 9.functions on list

# len/min/max/sorted
L = [3, 5, 2, 4, 0]
print(len(L))
L = [3, 5, 2, 4, 0]
print(max(L))
L = [3, 5, 2, 4, 0]
print(min(L))
L = [3, 5, 2, 4, 0]
print(sorted(L))  # Increasing order
L = [3, 5, 2, 4, 0]
print(sorted(L, reverse=True))  # Decreasing order

# Count
L = [1, 2, 3, 2]
count = L.count(2)
print(count)
#Index
L = [1, 2, 3,2,6,2, 2]
T1=L.index(6)
print(T1)
#reverse
L = [1, 2, 3,2,6,2, 2]
L.reverse()
print(L)
#sort(permanent) vs sorted(temporary)
L = [1, 2, 3,2,6,2, 2]
L.sort()
print(L)
#copy
L=[1,2,3,4,5,6]
L.copy()
print(L)

#List comprehension

#List comprehension provides a concise way of creating lists.
#newlist=[expression for items in iterable if condition ==True]
#Advantage of list comprehension
#1.More time efficient and space efficient than loops
#2.Requires fewer lines of code
#3.Tansforms iterative statements into a formula

#Que:-> Add 1 to 10 numbers to a list
L=[i for i in range(1,11)]
print(L)

#Que:-> Scalar multipilication on a vector
v=[1,2,3]
s=-3
L=[s*i for i in v]
print(L)

#Que:-> Add square
L=[1,2,3,4,5]
P=[i**2 for i in L]
print(P)

#Ques:-> print all number divided by 5 in the range og 1,50
P=[i for i in range(1,51) if i%5==0]
print(P)

#Que:-> find languages which start with letter p
languages=['java','python','php','c','javascript']
P=[i for i in languages if i.startswith('p')]
print(P)

#Que:-> Nested if with list comprehension
basket=['apple','guava','cherry','banana']
my_fruit=['apple','kiwi','grapes','banana']
P=[i for i in my_fruit if i in basket if i.startswith('a')]
print(P)

#Que:-> print a (3,3) matrix using list comprehension ->Nested list comprehension
P=[[i*j for i in range(1,4)] for j in range (1,4)]
print(P)

#Que:-> cartesian products
L1=[1,2,3,4]
L2=[5,6,7,8]
P=[i*j for i in L1 for j in L2]
print(P)

# 2 ways to traverse a list

#itemwise
L=[1,2,3,4]
for i in L:
    print(i)

#indexwise
L=[1,2,3,4]
for i in range(0,len(L)):
    print(i)

#Zip / index wise add karne ka kaam karta hain

#Que:-> write a program to add  items of 2  lists indexwise
L1=[1,2,3,4]
L2=[-1,-2,-3,-4,]
list(zip(L1,L2))
P=[i+j for i,j in zip(L1,L2)]
print(P)

#Disadvantage of python lists
#1:->Slow
#2:->Risky usages
#3:->eats up more memory
