# Search for a Name in a Tuple and Replace It with a New Name Using Its Index
tp=("Aryan","Pritam","Suman","Ranja","om","Rahul","Sourav")
print(tp)
s=input("Enter the name=")
n=-1
for i in range(0,len(tp)):
    if s==tp[i]:
        n=i
if n!=-1:
    print("The name is found.")    
    l=list(tp)
    k=input("Enter the new name for changing=")    
    l[n]=k
    tp=tuple(l)
    print(tp)
else:
    print("The name is not found in the list.")    
    