#Read and Print List Elements
ls=[]
n=int(input("Enter the length of list="))
for i in range(1,n+1):
    x=int(input("Enter any number="))
    ls.append(x)
for j in range(0,n):
    print(ls[j])