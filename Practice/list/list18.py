# Rotate the Last Digit to the Front of Each Number in a List
# expected output-------->
# [1234, 5678, 9087, 246, 13579]
# [4123, 8567, 7908, 624, 91357]
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
    k=i-last
    q=i//10
    z=(last*(10**(count-1)))+q
    l2.append(z)
print(l2)    

