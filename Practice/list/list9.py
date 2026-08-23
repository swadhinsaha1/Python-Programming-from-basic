# list-1
ls1=[]
n1=int(input("Enter the length of the list(5 elements)="))
for i in range(0,n1):
    x=int(input("Enter the number="))
    ls1.append(x)   
    ls1.sort() 
# list-2
ls2=[]
n2=int(input("Enter the length of the list(7 elements)="))
for i in range(0,n2):
    x=int(input("Enter the number="))
    ls2.append(x)    
    ls2.sort() 
   
i=0
z=0
while(i<n2):
    if (z<n2):
        if (ls2[i]<ls1[z]):
            print(ls2[i])
            i=i+1
        else:
            print(ls1[z])
            z=z+1
    else:
        i=i+1