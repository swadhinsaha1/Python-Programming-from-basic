l1=[]
n=int(input("Enter the number of elements: "))
for i in range(n):
    x=int(input("Enter the element: "))
    l1.append(x)

print(l1)
x=int(input("Enter the element to be deleted: "))
  
while x in l1:
    l1.remove(x)
print(l1)    




# l1=[]
# n=int(input("Enter the number of elements: "))
# for i in range(n):
#     x=int(input("Enter the element: "))
#     l1.append(x)

# print(l1)
# x=int(input("Enter the element to be deleted: "))
  
# if x in l1:
#     for i in l1.copy():
#         if i==x:
#             l1.remove(i)
# print(l1)