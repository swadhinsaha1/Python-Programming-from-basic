# Search for a Name in a Tuple and Replace It with a New Name Using Its Index
tp=("Aryan","Pritam","Suman","Ranja","om","Rahul","Sourav")
s=input("Enter the name=")
# print("The position of the name in tuple",tp.index(s)+1)
# print(tp.index(s))
# for i in range(0,len(tp)):
#     tp.index(s)
if tp.index(s)>=0:
    p=tp.index(s)
    ls=list(tp)
    n=input("Enter the name for changing=")
    ls[p]=n
    tp=tuple(ls)
    print("The name is found")
    print(tp)
else:
    print("The name is not found")    