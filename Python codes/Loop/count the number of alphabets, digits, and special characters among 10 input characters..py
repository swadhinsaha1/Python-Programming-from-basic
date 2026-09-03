
c=0
d=0
s=0
for i in range(11):
    x=input("Enter 10 characters=")
    a=ord(x)
    if 65<=a<=90 or 97<=a<=122:
        c+=1
    elif 48<=a<=57:
        d+=1  
    else:
         s+=1    
print("No of alphabet ",c)
print("No of digit ",d)
print("No of special character ",s)
print(a)