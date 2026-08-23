# Interchange First and Last Digits of Each Number in a List
#exaple---[215,4567,6435]
#         [512,7564,5436]
l1=[]
n=int(input("Enter the length of the list="))
for i in range(0,n):
    x=int(input("Enter the number for the list="))
    l1.append(x)
print(l1)
l2=[]
for i in l1:
    temp=i
    count=0
    while(temp!=0):
        temp//=10
        count+=1
    last=i%10
    first=i//(10**(count-1)) 
    q=i%(10**(count-1))
    z=(last*(10**(count-1)))+(q-last)+first
    l2.append(z)
print(l2)    

