# #without using ascii value
# x=input("Enter the character=")
# if ("a"<=x<="z"):
#     print("the alphabet is lower case")
# elif("A"<=x<="Z"):
#     print("the alphabet is higer case")
# else:
#     print("the character is a special character")    


#using ascii value
x=input("Enter the character=")
a=ord(x)
if (65<=a<=90):
    print("the alphabet is higer case")
elif(97<=a<=122):
    print("the aplhabet is lower case")
else:
    print("the character is a special character")    

