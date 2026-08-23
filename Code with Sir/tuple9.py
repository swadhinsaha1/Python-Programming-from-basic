tp=("Aryan","Pritam","Suman","Ranja")
s=input("Enter the name to be deleted=")
n=-1
for i in range(0,len(tp)):
    if(s==tp[i]):
        n=i
if n!=-1:
    print("The name is found.")    
    ls=list(tp)
    ls.remove(s)
    tp=tuple(ls)
    print(tp)
else:
    print("The name is not found.")    


