l1=[]
n=int(input("Enter the length of the list="))
for i in range(0,n):
    x=int(input("Enter the number for the list="))
    l1.append(x)
print(l1)
l2=[]    
for i in l1:
    temp=i
    rev=0
    while(temp!=0):
        rem=temp%10
        rev=rev*10+rem
        temp//=10
    l2.append(rev)
print(l2)

