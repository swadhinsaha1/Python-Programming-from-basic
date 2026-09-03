# Find the Middle Digit of Odd Numbers and Display Even Numbers from a List
l=[]
n=int(input("Enter the length of the list="))
for i in range(0,n):
    x=int(input("Enter the number for the list="))
    l.append(x)
for i in l:
    count=0
    temp=i
    while(temp!=0):
        temp//=10
        count+=1
    if(count%2!=0):
        p=i//(10**(count//2))
        middle=p%10
        # print(module,"--->",i)
        print(f"{i}------>{middle}")