import math
for i in range(1,6):
    n=int(input("Enter 5 natural numbers="))
    temp=n
    sum=0
    while temp!=0:
        rem=temp%10
        sum+=math.factorial(rem)
        temp//=10
    if sum==n:
        print(f"{n} is krishnamurty number")    
    