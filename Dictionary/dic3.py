# Creating a Dictionary from User Input and Displaying Key-Value Pairs
dis={}
for i in range(1,5):
    s=input("Enter the name=")
    dis[i]=s
for i in dis.keys():    
    print(f"{i}:{dis[i]}")    