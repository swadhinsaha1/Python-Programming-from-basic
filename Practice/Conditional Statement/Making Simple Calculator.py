a=int(input("Enter the first number="))
b=int(input("Enter the second number="))
c=input("Enter operator(+,-,*,/)=")
if c=="+":
    print("Answer=",a+b)
elif c=="-":
    print("Answer=",a-b)
elif c=="*":
    print("Answer=",a*b)
elif c=="/":
    if b==0:
        print("Invalid number~change the second number")
    else:
        print("Answer(without decimal)=",a//b)  
        print("Answer(with decimal)=",a/b)  
else:
    print("Invalid operation.")        
    