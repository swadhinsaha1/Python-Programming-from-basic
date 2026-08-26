# Separate Tuple Elements into Single-Occurrence and Multi-Occurrence Lists
# without using count() (only nested loops)
tp = (45, 12, 78, 23, 45, 0, -12, 67, 34, 89,
      12, 56, 23, -5, 90, 34, 7, 100, 67, 15,
      -8, 34, 56, 99, 23, -15, 76, 45, 90, 5)
l1=[]
l2=[]

for i in range(0,len(tp)):
    count=0
    for j in range(0,len(tp)):
        if tp[i]==tp[j]:
            count+=1
    if count==1:
        l1.append(tp[i])
    else:
        if tp[i] not in l2:
            l2.append(tp[i])    
print("The all teh single occurance numbers in list1 are=>",l1)            
print("The all teh multi occurance numbers in list2 are=>",l2)    


# #using count()
# tp = (45, 12, 78, 23, 45, 0, -12, 67, 34, 89,
#       12, 56, 23, -5, 90, 34, 7, 100, 67, 15,
#       -8, 34, 56, 99, 23, -15, 76, 45, 90, 5)
# print(tp)

# l1=[]
# l2=[]

# for i in tp:
#     if tp.count(i)==1:
#         l1.append(i)
#     else:
#         if i not in l2:
#             l2.append(i)    
# print("The all teh single occurance numbers in list1 are=>",l1)            
# print("The all teh multi occurance numbers in list2 are=>",l2)   