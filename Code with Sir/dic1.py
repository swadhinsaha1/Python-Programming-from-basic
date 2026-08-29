dis={"name":"Anil","age":21,"NRI":False}
for k in dis.keys():
    print(k)
for v in dis.values():
    print(v)    
for k,v in dis.items():
    print(k,":",v)

for k in dis.keys():
    print(f"{k}:{dis[k]}")