# a=input("Enter any name ")
# b=int(input("Enter any number"))
# print(a,b)


# x=int(input("Enter any number "))
# y=int(input("Enter any number "))
# s=x+y
# print(x,end="+")
# print(y,end="=")
# print(s)
# print(x,-"+",y,"=",s)


# x=int(input("Enter any number "))
# y=int(input("Enter any number "))
# print("Answer=",x/y)
# print("Answer=",x//y)



# if x%2==0 :
#     print("even no.",x)
# else:
#     print("odd no.",x)
# print("out of if")    



# n=int(input("Enter any number "))
# d=int(input("Enter any number "))
# if d==0:
#     print("wrong input")
# elif d==1 or d==n :
#     print("Not fraction")
# elif d>n:
#     print("Proper fraction")
# else:
#     print("Improper fraction")
    
    
    
a=int(input("Enter any number="))
b=int(input("Enter any number="))
c=input("Select operator(+,-,*,/)=")
if c=='+' :
    print("Answer=",a+b)
elif c=='-' :
    print("Answer=",a-b)
elif c=='*':
    print("Answer=",a*b)
elif c=='/' :
    if b==0:
        print("Wrong Input")
    else:    
        print("Answer=",a/b)
        print("Answer=",a//b)
else:
    print("Wrong Input")
