# Write a program to search for an element in a list using the in operator.
ls=[]
n=int(input("Enter the length of the list="))
for i in range(0,n):
    x=int(input("Enter the number="))
    ls.append(x)
x=int(input("Enter the number to be found="))    
if x in ls:
    print("The number is found.")
else:
    print("The number is not found.")    

        