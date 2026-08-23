# #Distance between two points,x and y
# x=int(input("Enter the first point="))
# y=int(input("Enter the second point="))
# import math
# distance=math.sqrt((x**2)-(y**2))
# print("The distance b/w two points=",distance)


#Distance between two points,(x1,y1) and (x2,y2)
import math
x1,y1=map(int,input("Enter the first point=").split())
x2,y2=map(int,input("Enter the second point=").split())
distance=math.sqrt((x2-x1)**2+(y2-y1)**2)
print("The distance b/w two points=",distance)