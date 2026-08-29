# create two tuple with prime and composite number,one tuple contain only prime numbers and another tuple will contain only composite numbers
tp1=(45,34,43,65,23,54,23,56)
tp2=(23,45,56,43,45,91,56,31,73)
ls1=[]
ls2=[]
tp3=tp1+tp2
for i in tp3:
    count=0
    x=i
    for j in range(1,x+1):
        if x%j==0:
            count+=1
    if count==2:
        ls1.append(x) 
    else:
        ls2.append(x)   
tp1=tuple(ls1)    
tp2=tuple(ls2)    
print("All Prime numbers in the tuple1",tp1)
print("All composite numbers in the tuple2",tp2)