tp=(34,67,43,74,34,65,34,8,9,65)
c=0
ls1=[]
ls2=[]

for i in range(0,len(tp)):
    c=0
    for j in range(0,len(tp)):
        if tp[i]==tp[j]:
            c+=1
    if c==1:
        ls1.append(tp[i])
    else:
        if tp[i] not in ls2:
            ls2.append(tp[i])    
        
print(tp)
print("All the single occurance numbers are---",ls1)
print("Rest of the numbers are---",ls2)
# tp=(34,67,43,74,34,65,34,8,9,65)
# count=0
# ls1=[]
# ls2=[]

# for i in tp:
#     if tp.count(i)>1:
#         ls2.append(i)
#     else:
#         ls1.append(i)    
# print(tp)
# print("All the single occurance numbers are---",ls1)
# print("Rest of the numbers are---",ls2)