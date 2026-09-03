dis={}
for i in range(1,5):
    key=input("Enter the key=")
    value=input("Enter the value of the key=")
    dis[key]=value
print("\n")

for i in dis.keys():  # You can also use only dis instead of dis.keys()
    print(f"{i}:{dis[i]}")    