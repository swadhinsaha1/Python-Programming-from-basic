# Write a program to merge two lists using the extend() function.
# list-1
ls1=[]
n1=int(input("Enter the length of the list(5 elements)="))
for i in range(0,n1):
    x=int(input("Enter the number="))
    ls1.append(x)    
# list-2
ls2=[]
n2=int(input("Enter the length of the list(7 elements)="))
for i in range(0,n2):
    x=int(input("Enter the number="))
    ls2.append(x)    

ls1.extend(ls2)
for k in range(0,n1+n2):
    print(ls1[k])