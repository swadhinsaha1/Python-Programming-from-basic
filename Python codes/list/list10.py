# Extract the First Digit of Each Number in a List
l1=[]
n=int(input("Enter the length of the list= "))
for i in range(n):
    x=int(input("Enter the element="))
    l1.append(x)

print(l1)

for i in l1:
    temp=i
    count=0
    while(temp!=0):
        temp//=10
        count+=1
    first=i//(10**(count-1))
    print(first)
    