def check_area_perimeter(a,b):
    area=a*b
    perimeter=(a+b)*2
    if max(area,perimeter)==area:
        print("Area greater than perimeter")
    elif max(area,perimeter)==perimeter:
        print("Area smaller than perimeter")
    else :
        print("Area equal to perimeter")

length=int(input("Enter length:"))
breadth=int(input("Enter breadth:"))
check_area_perimeter(length,breadth)
