for i in range(1,11):
    x=int(input("Enter the 10 numbers="))
    count=0
    for j in range(1,x+1):
        if x%j==0:
            count+=1
    if count==2:
        print("Prime No ",x)        
