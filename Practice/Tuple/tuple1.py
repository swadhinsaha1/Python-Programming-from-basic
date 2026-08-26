# Display a Tuple and Print Its Elements Using a for Loop and Tuple Unpacking
tp=(45,34,75,24,4,37)
print(tp)

#printing all the elements using for loop
for x in tp:
    print(x,end=" ")


#printing all the elements without using for loop
print()
print(*tp)    