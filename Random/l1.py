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
l1.sort()
l2.sort()

print("List1:", l1)
print("List2:", l2)


l1.extend(l2)
l1.sort()
print("the final sorted list is--",l1)

# l3=l1.copy()
# l1.clear()
# l2.clear()
# for i in l3:
#     if i%2==0:
#         l1.append(i)
#     else:
#         l2.append(i)   

# print("all the even numbers=",l1)         
# print("all the odd numbers=",l2)         


