# =========================
# TUPLE IN PYTHON
# =========================

t=(2,35,44,54,35,76,45,86,35,56)

# m=(23,34.6,"Swadhin",True)

# print(m)

# --a tuple can contain anything in it(integer,float,string,boolean etc...)


# print(t)

# --to print the tuple


# print(t.index(54))

# --used to know the index of the specific element

# --here I want to know the index of 54


# print(t.count(35))

# --used to know the specific element is available for how many times

# --here I want to know that 35 is present for how many times


# ------------------------------------------------
# TUPLE IS IMMUTABLE
# ------------------------------------------------

# --A tuple cannot be changed after it is created.

# --Therefore, the following list methods do NOT work directly on tuples:

# t.append(8)       # ERROR
# t.insert(2,5754)  # ERROR
# t.remove(35)      # ERROR
# t.pop()           # ERROR
# t.sort()          # ERROR
# t.reverse()       # ERROR
# t.extend((4,5))   # ERROR


# ------------------------------------------------
# LENGTH OF A TUPLE
# ------------------------------------------------

# print(len(t))

# --used to know the total number of elements in the tuple


# ------------------------------------------------
# MAXIMUM ELEMENT
# ------------------------------------------------

# print(max(t))

# --used to find the largest element in the tuple


# ------------------------------------------------
# MINIMUM ELEMENT
# ------------------------------------------------

# print(min(t))

# --used to find the smallest element in the tuple


# ------------------------------------------------
# SUM OF ALL ELEMENTS
# ------------------------------------------------

# print(sum(t))

# --used to find the sum of all the numerical elements in the tuple


# ------------------------------------------------
# SORTING A TUPLE
# ------------------------------------------------

# t=(35,12,87,23,45)

# print(sorted(t))

# --sorted() is used to sort the elements

# --IMPORTANT:
# --sorted() returns a LIST, not a tuple

# --output:
# [12,23,35,45,87]


# ------------------------------------------------
# CONVERTING LIST INTO TUPLE
# ------------------------------------------------

# l=[10,20,30,40]

# t=tuple(l)

# print(t)

# --used to convert a list into a tuple

# --output:
# (10,20,30,40)


# ------------------------------------------------
# CONVERTING STRING INTO TUPLE
# ------------------------------------------------

# x="Python"

# t=tuple(x)

# print(t)

# --used to convert a string into a tuple

# --output:
# ('P','y','t','h','o','n')


# ------------------------------------------------
# CONVERTING TUPLE INTO LIST
# ------------------------------------------------

# t=(10,20,30,40)

# l=list(t)

# print(l)

# --used to convert a tuple into a list

# --output:
# [10,20,30,40]

# --after converting into a list, we can use list methods
# --such as append(), remove(), pop(), sort(), etc.


# ------------------------------------------------
# CONCATENATION OF TUPLES
# ------------------------------------------------

# t1=(10,20,30)

# t2=(40,50,60)

# t3=t1+t2

# print(t3)

# --used to merge two or more tuples

# --output:
# (10,20,30,40,50,60)


# ------------------------------------------------
# REPETITION OF TUPLE
# ------------------------------------------------

# t=(1,2)

# print(t*3)

# --used to repeat the elements of a tuple

# --output:
# (1,2,1,2,1,2)


# ------------------------------------------------
# INDEXING IN TUPLE
# ------------------------------------------------

# t=(10,20,30,40,50)

# print(t[2])

# --used to access an element using its index

# --here I want to access the element at index 2

# --output:
# 30


# ------------------------------------------------
# NEGATIVE INDEXING
# ------------------------------------------------

# t=(10,20,30,40,50)

# print(t[-1])

# --negative indexing starts from the end

# --output:
# 50


# ------------------------------------------------
# SLICING A TUPLE
# ------------------------------------------------

# t=(10,20,30,40,50)

# print(t[1:4])

# --used to get a specific part of the tuple

# --output:
# (20,30,40)


# ------------------------------------------------
# MEMBERSHIP OPERATOR
# ------------------------------------------------

# t=(10,20,30,40)

# print(20 in t)

# --used to check whether an element is present in the tuple

# --output:
# True


# ------------------------------------------------
# NOT IN OPERATOR
# ------------------------------------------------

# t=(10,20,30,40)

# print(50 not in t)

# --used to check whether an element is NOT present in the tuple

# --output:
# True


# ------------------------------------------------
# ANY()
# ------------------------------------------------

# t=(0,0,5,0)

# print(any(t))

# --returns True if at least one element is True/non-zero

# --output:
# True


# ------------------------------------------------
# ALL()
# ------------------------------------------------

# t=(1,2,3,4)

# print(all(t))

# --returns True if all elements are True/non-zero

# --output:
# True


# ------------------------------------------------
# ENUMERATE()
# ------------------------------------------------

# t=("A","B","C")

# for i,x in enumerate(t):
#     print(i,x)

# --enumerate() gives both index and value

# --output:
# 0 A
# 1 B
# 2 C


# ------------------------------------------------
# ZIP()
# ------------------------------------------------

# t1=(1,2,3)

# t2=("A","B","C")

# print(tuple(zip(t1,t2)))

# --used to combine corresponding elements of two tuples

# --output:
# ((1,'A'),(2,'B'),(3,'C'))


# ------------------------------------------------
# COPYING A TUPLE
# ------------------------------------------------

# t=(10,20,30)

# g=t

# print(g)

# --tuples are immutable, so a simple assignment
# --is enough when you only need another reference


# ------------------------------------------------
# UNPACKING A TUPLE
# ------------------------------------------------

# t=(10,20,30)

# a,b,c=t

# print(a)
# print(b)
# print(c)

# --used to assign tuple elements to different variables

# --output:
# 10
# 20
# 30


# ------------------------------------------------
# NESTED TUPLE
# ------------------------------------------------

# t=((1,2),(3,4),(5,6))

# print(t)

# --a tuple can contain other tuples inside it


# ------------------------------------------------
# ACCESSING NESTED TUPLE
# ------------------------------------------------

# t=((1,2),(3,4),(5,6))

# print(t[1][0])

# --first [1] selects the second tuple
# --second [0] selects the first element of that tuple

# --output:
# 3


# ------------------------------------------------
# IMPORTANT DIFFERENCE BETWEEN LIST AND TUPLE
# ------------------------------------------------

# LIST:
# l=[10,20,30]

# l.append(40)
# l.remove(20)
# l[0]=100

# --Lists are mutable.
# --Their elements can be changed.


# TUPLE:
# t=(10,20,30)

# t[0]=100

# --ERROR

# --Tuples are immutable.
# --Their elements cannot be changed after creation.


# =================================================
# IMPORTANT TUPLE METHODS
# =================================================

# 1. count()
# 2. index()


# =================================================
# IMPORTANT BUILT-IN FUNCTIONS
# =================================================

# len()
# max()
# min()
# sum()
# sorted()
# tuple()
# list()
# any()
# all()
# enumerate()
# zip()


# =================================================
# IMPORTANT TUPLE OPERATIONS
# =================================================

# +       -> Concatenation
# *       -> Repetition
# []      -> Indexing
# [start:end] -> Slicing
# in      -> Membership checking
# not in  -> Membership checking