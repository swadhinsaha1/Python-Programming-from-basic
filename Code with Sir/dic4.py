dis={}
for x in range(1,4):
    key=input("Enter Key=")
    value=input("Enter value of key=")
    dis[key]=value
print("\n")
for k in dis.keys():
    print(f"{k}:{dis[k]}")