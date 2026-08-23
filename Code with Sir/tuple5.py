tp=(34,67,43,74,34,65,34,8,9,65)
count=0
x=int(input("Enter the number to be found="))
for i in tp:
    if x==i:
        count+=1
print(count)