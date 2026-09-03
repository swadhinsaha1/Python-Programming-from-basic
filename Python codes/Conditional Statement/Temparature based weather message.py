#type-1
x = int(input("Enter the temperature = "))

if x <= 0:
    print("It's freezing")
elif x <= 10:
    print("It's very cold")
elif x <= 20:
    print("It's cold")
elif x <= 30:
    print("It's normal")
elif x <= 40:
    print("It's hot")
else:
    print("It's very hot")


# #type-2(using ternary operator)
# x=int(input("Enter the temparature="))
# print("it's freezing" if x<=0 else "")
# print("it's very cold" if 0<x<=10 else "")
# print("it's cold" if 10<x<=20 else "")
# print("it's normal" if 20<x<=30 else "")
# print("it's hot" if 30<x<=40 else "")
# print("it's very hot" if x>=40 else"")