# n=int(input("Enter the length of the list="))
# for i in range(0,n):
#     x=int(input("Enter the number for the list="))
#     l.append(x)
l=[23,34,23,432,345,654,324,32]
print(l)
l.pop()#wiothout any inofrmation deleted from the back of the list 
print(l)    
m=[23,34,23,432,345,654,324,32]
m.pop(2)
#with index deleted from the list 
print(m) 
n=[23,34,23,432,345,654,324,32]
n.remove(432)
#with element deleted fromthe list 
print(n)   