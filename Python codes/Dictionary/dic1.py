dis={"name":"Anil","age":21,"NRI":False}
for k in dis.keys():
    print(k)
print("\n")    

for v in dis.values():
    print(v)    
print("\n")    

for k,v in dis.items():
    print(k,":",v)
print("\n")

#same as before.......
for k in dis.keys():
    print(f"{k}:{dis[k]}")
print("\n")    