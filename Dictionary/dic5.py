## Creating a Dictionary with User-Defined Key and List Values
# dis={"name":["Swadhin","Pritam","Rik","Prodip"]}
# for i in dis.keys():
#     for x in dis[i]:
#         print(x,"",end="")


## Creating a Dictionary with Multiple Values for a Key and Displaying Them
dis={}
l=[]
key=input("Enter the key=")
for i in range(1,5):
    value=input("Enter the value of the list=")
    l.append(value)
print(l)

dis[key]=l #store the list ls as the value of the dictionary under the key key.
for i in dis.keys():
    for j in dis[i]:
        print(f"{i}:{j}")