# dis={"name":["ARPAN","DINESH","ROHAN","SUMAN"]}
# for k in dis.keys():
#     for x in dis[k]:
#         print(x)

#with using input
dis={}
ls=[]
key=input("Enter key=")
for x in range(1,5):
    st=input("Enter Name=")
    ls.append(st)
dis[key]=ls
for k in dis.keys():
    for x in dis[k]:
        print(f"{k}:{x}")

