n=int(input("Enter the number of terms="))
sum=0
for i in range(1,n+1,2):
    sum+=i
    print(i)
print("Sum of ",n,"odd numbers=",sum)