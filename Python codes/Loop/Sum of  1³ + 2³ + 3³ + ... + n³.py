n=int(input("Enter the number of terms="))
sum=0
for i in range(1,n+1):
    sum+=(i**3)
print("Sum of the series---")    
print(f"Sum of 1³ + 2³ + 3³ + ... + {n}³ = {sum}")
