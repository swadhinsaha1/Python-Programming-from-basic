#checking the given character is alphabet,digit or special character
#without using ascii value
x=input("Enter the character=")
if(("a"<=x<="z") or ("A"<=x<="Z")):
    print("the character is alphabet")
elif("0"<=x<="9"):
    print("the character is a digit")  
else:
    print("the character is special character")      




# #using the ascii value
# x=input("Enter the character=")
# a=ord(x)
# if((65<=a<=90) or (97<=a<=122)):
#     print("the character is alphabet")
# elif(48<=a<=57):
#     print("the character is a digit")  
# else:
#     print("the character is special character")      



# #using predefined (built-in) string methods
# x=input("Enter the character=")
# if(x.isalpha()):
#     print("the character is alphabet")
# elif(x.isdigit()):
#     print("the character is a digit")  
# elif(x.isspace()):
#     print("the character is a white sapce character")   
# else:
#     print("the character is special character")      
