# Remove the First Occurrence of an Element and Append It to the End of a List
l=[]
n=int(input("Enter the length of the list="))
for i in range(0,n):
    x=int(input("Enter the number for the list="))
    l.append(x)
print(l)

x=int(input("Enter the number to be deleted="))
if x in l:
    l.remove(x)
    l.append(x)
    print(l)    
else:
    print("The number is not present in the list")    