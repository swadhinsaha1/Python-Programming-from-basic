# : Creating a Dictionary with Multiple Keys and List Values Using User Input      
dis={}
for i in range(1,3):
    key=input("Enter key=")
    ls=[]
    for x in range(1,4):
        st=input("Enter Value of Key : ")
        ls.append(st)
    dis[key]=ls
for k in dis.keys():
        for x in dis[k]:
            print(k,"=",x,end=" ")
        print()    
