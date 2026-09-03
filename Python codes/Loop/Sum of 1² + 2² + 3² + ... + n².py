n=int(input("Enter the number of terms="))
sum=0
for i in range(1,n+1):
    sum+=(i**2)
print("Sum of the series---")    
print("Sum of 1² + 2² + 3² + ... +",n,"²=",sum)
print(f"Sum of 1² + 2² + 3² + ... + {n}² = {sum}")
print("Sum of 1² + 2² + 3² + ... + " + str(n) + "² = " + str(sum))
print("Sum of 1² + 2² + 3² + ... + ", n, "² = ", sum, sep="")