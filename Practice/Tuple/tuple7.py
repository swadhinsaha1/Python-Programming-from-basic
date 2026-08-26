# Create a List from User Input and Convert It into a Tuple
l=[]
n=int(input("Enter the length of the list="))
for i in range(0,n):
    x=int(input("Enter the elements="))
    l.append(x)
print("The list is ",l)    
tp=tuple(l)
print("The tuple is ",tp)