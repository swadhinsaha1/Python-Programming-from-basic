# ---------type:-1-----------------
l1=[]
n=int(input("Enter the number of elements: "))
for i in range(n):
    x=int(input("Enter the element: "))
    l1.append(x)

l2=[]
n=int(input("Enter the number of elements: "))
for i in range(n):
    x=int(input("Enter the element: "))
    l2.append(x)

print("List1:", l1)
print("List2:", l2)



l1.extend(l2)
print("After merging two lists:",l1)

odd=[]
even=[]

for i in l1:
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)   

print("all the even numbers=",even)         
print("all the odd numbers=",odd)         




# ---------type:-2-----------------
# #list-1
# ls1=[]
# n1=int(input("Enter the length of the list="))
# for i in range(0,n1):
#     x=int(input("Enter the number="))
#     ls1.append(x)
# #list-2
# ls2=[]
# n2=int(input("Enter the length of the list="))
# for i in range(0,n2):
#     y=int(input("Enter the number="))
#     ls2.append(y)

# ls1.extend(ls2)

# odd=[]
# even=[]

# for j in range(0,n1+n2):
#     if ls1[j]%2==0:
#         even.append(ls1[j])
#     else:
#         odd.append(ls1[j])
 

# print("All the even numbers now in list-1==>",even)        
# print("All the odd numbers now in list-2==>",odd)     




# ---------type:-3-----------------
# #list-1
# ls1=[]
# n1=int(input("Enter the length of the list="))
# for i in range(0,n1):
#     x=int(input("Enter the number="))
#     ls1.append(x)
# #list-2
# ls2=[]
# n2=int(input("Enter the length of the list="))
# for i in range(0,n2):
#     y=int(input("Enter the number="))
#     ls2.append(y)

# ls1.extend(ls2)

# ls3=[]
# ls3=ls1.copy()

# ls1.clear()
# ls2.clear()

# for j in range(0,n1+n2):
#     if ls3[j]%2==0:
#         ls1.append(ls3[j])
#     else:
#         ls2.append(ls3[j])
# print("All the even numbers now in list-1==>",ls1)        
# print("All the odd numbers now in list-2==>",ls2)        