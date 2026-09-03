#checking the given character is vowel or consonant or special character
x=input("Enter the character=")
if (x=="a" or x=="e" or x=="i" or x=="o" or x=="u" or x=="A" or x=="E" or x=="I" or x=="O" or x=="U"):
    print("the character is vowel")
elif(("a"<=x<="z") or ("A"<=x<="Z")):
    print("the character is consonant")
else:
    print("the character is a special character")    