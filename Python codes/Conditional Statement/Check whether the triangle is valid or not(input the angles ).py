a,b,c=map(int,input("Enter the the angles of the triangle=").split())
if ((a+b+c==180) and a>0 and b>0 and c>0):
    print("The triangle is valid")
else:
    print("The trianlge is not valid")    