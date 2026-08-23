#type-1(using the nested if-else)
a=int(input("Enter the first side of the triangle="))
b=int(input("Enter the second side of the triangle="))
c=int(input("Enter the third side of the triangle="))
if ((a+b)>c):
    if ((b+c)>a):
        if ((c+a)>b):
            print("The triangle is valid")
        else:
            print("the triangle is not valid")
    else:        
        print("the triangle is not valid")
else:
    print("the trianlgle is not valid")

# #type-2(without using the nested if-else)   
# a,b,c=map(int,input("Enter the three sides of the triangle=").split())
# if ((a+b)>c and (b+c)>a and (c+a)>b):
#     print("the triangle is valid")
# else:
#     print("the triangle is not valid")    
