n = int(input("Enter the number of terms="))
sum = 0
import math

for i in range(1, n + 1):
    term=1/math.factorial(i)
    sum +=term
print("Sum of the series---")
print(f"Sum of 1 + 1/2! + 1/3! + ..... + 1/{n}! = {sum}")