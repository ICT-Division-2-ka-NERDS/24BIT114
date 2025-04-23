def check_valid_triangle(a,b,c):
    if a+b+c==180:
        print("It is a valid triangle")
    else:
        print("It is not a valis triangle")
angle1=int(input("Enter first Angle in degrees:"))
angle2=int(input("Enter second Angle in degrees:"))
angle3=int(input("Enter third Angle in degrees:"))
check_valid_triangle(angle1,angle2,angle3)
