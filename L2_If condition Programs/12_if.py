import math
def check_point_position(x,y,x1,y1,r):
    distance=math.sqrt(pow((x-x1),2)+ pow((y-y1),2))
    if distance>r:
        print("point outside the circle")
    elif distance<r:
        print("point inside the circle")
    else:
        print("Point on the circle")

a,b= map(int,input("Enter centre coordinates x y:").split())
a1,b1=map(int,input("Enter point x1 y1:").split())
radius=int(input("Enter radius:"))
check_point_position(a,b,a1,b1,radius)
