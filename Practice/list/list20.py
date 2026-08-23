# Program to Calculate the Total Sum of All Individual Digits Present in list
l=[]
n=int(input("Enter the length of the list="))
for i in range(n):
    x=int(input("Enter the elements of the list="))
    l.append(x)
print(l)
sum=0
for i in l:
    temp=i
    while temp>0:
        rem=temp%10
        sum+=rem
        temp//=10
print(sum)