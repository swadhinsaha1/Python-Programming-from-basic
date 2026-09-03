# Program to Calculate the Sum of Digits of Each Element in a List and Find the Element Having the Maximum Sum of Digits Without Using an Additional List
# [123, 456, 999, 2345, 321]
# The numner is 999
# And sum of digits is 27
l=[]
n=int(input("Enter the length of the list="))
for i in range(n):
    x=int(input("Enter the elements of the list="))
    l.append(x)
print(l)

large=0
number=0

for i in l:
    temp=i
    sum=0
    while temp>0:
        rem=temp%10
        sum+=rem
        temp//=10

    if sum>large:
        large=sum
        number=i

print("The numner is ",number)
print("And sum of digits is ",large)        



