# Count the Occurrences of a User-Entered Number in a Tuple Without Using the count() Method
tp=(34,56,76,44,97,23,34,5)
print(tp)
x=int(input("Enter the number to be checked="))
count=0
for i in tp:
    if x==i:
        count+=1
print(f"The number is present in the tupple {count} times")        


