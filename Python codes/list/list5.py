# Write a program to search for an element in a list and delete it using the remove() function.
#My code
l=[]
n=int(input("Enter the number of elements: "))
for i in range(n):
    x=int(input("Enter the element: "))
    l.append(x)
print("List:", l)
y=int(input("Enter the element searching for deleting="))
if y in l:
    print("The element is found.")
    l.remove(y)
    print("The list after deleting",l)
else:
    print("not present")    


# #Sir's Code
# ls=[]
# n=int(input("Enter the length of the list="))
# for i in range(0,n):
#     x=int(input("Enter the number="))
#     ls.append(x)
# print(ls)
# x=int(input("Enter the number to be found and deleted="))    
# if x in ls:
#     print("The number is found.")
#     ls.remove(x)
#     for j in range(0,len(ls)):#akhane remove korar por joto gulo element baki thakbe toto gulo element ordhi loop ghurbe
#         print(ls[j])
# else:
#     print("The number is not found.")    