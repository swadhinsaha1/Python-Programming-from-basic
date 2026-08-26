# Search for and Delete a User-Entered Name from a Tuple Using a Loop
tp=("Aryan","Pritam","Suman","Ranja")
print(tp)
s=input("Enter the name=")
n=-1
for i in range(0,len(tp)):
    if s==tp[i]:    
        n=i
if n!=-1:
    print("The name is found.")    
    l=list(tp)
    l.remove(s)
    tp=tuple(l)
    print(tp)
else:
    print("The name is not found.")    