x,y=map(int,input("Enter the point=").split())
if x>0 and y>0 :
    print("the point is in first quadrant")
elif x<0 and y>0 :
    print("the point is in second quadrant")
elif x<0 and y<0 :
    print("the point is in third quadrant")
elif x>0 and y<0 :
    print("the point is in fourth quadrant")
elif x==0 and y==0:
    print("the point is on origin")
elif x==0:
    print("the point is on Y-axis")
elif y==0:
    print("the point is on X-axis")
        