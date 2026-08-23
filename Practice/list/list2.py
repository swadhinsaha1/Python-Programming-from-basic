# Write a program to insert an element at a specified position in a list.
ls=[]
n=int(input("Enter the length of the list="))
for i in range(n):#also applicable for range(0,n) and range(1,n+1)
    x=int(input("Enter the number="))
    ls.append(x)
print("The list is:", ls)
y=int(input("Enter the position to insert="))
z=int(input("Enter the value="))
ls.insert(y-1,z)
print("The updated list is:", ls)


