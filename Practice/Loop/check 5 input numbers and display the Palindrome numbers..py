import math
for i in range(1,6):
    n=int(input("Enter 5 natural numbers="))
    temp=n
    rev=0
    while temp!=0:
        rem=temp%10
        rev=rev*10+rem
        temp//=10
    if rev==n:
        print(f"{n} is Palindrome number")    
    