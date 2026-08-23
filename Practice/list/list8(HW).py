l1=[]
n=int(input("Enter the number of elements: "))
for i in range(n):
    x=int(input("Enter the element: "))
    l1.append(x)

double_digit=[]
non_double_digit=[]
    
for i in l1:
    if 10<=i<=99:
        double_digit.append(i)
    else:
        non_double_digit.append(i)
print("Only double digit numbers are---",double_digit)
print("Rest of the numbers are---",non_double_digit)        




# ls1=[]
# n1=int(input("Enter the length of the list="))
# for i in range(0,n1):
#     x=int(input("Enter the number="))
#     ls1.append(x)

# ls2=ls1.copy()
# ls1.clear()
# ls3=[]

# for i in range(0,n1):
#     if 10<=ls2[i]<=99:
#         ls1.append(ls2[i])
#     else:
#         ls3.append(ls2[i]) 

# print("All the double digits numbers are in list-1==>",ls1)
# print("Rest of the numbers are in list-2==>",ls3)