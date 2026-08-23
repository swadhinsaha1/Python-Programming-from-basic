ls=[]
n=int(input("Enter the length of the list="))
for i in range(0,n):
    x=int(input("Enter the number="))
    ls.append(x)
x=int(input("Enter the number to be found and deleted=")) 
if x in ls:
    print("The number is found and deleted.")
else:
    print("The number is not found.")    
for v in range(0,n):
    if x in ls:
        #print("The number is found.")
        ls.remove(x)
for j in range(0,len(ls)):#akhane remove korar por joto gulo element baki thakbe toto gulo element ordhi loop ghurbe
    print(ls[j])