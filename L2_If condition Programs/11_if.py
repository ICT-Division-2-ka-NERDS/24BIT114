def is_collinear(x1,y1,x2,y2,x3,y3):
    return (y2-y1) * (x3-x2)==(y3-y2) * (x2-x1)

x1, y1 = map(int, input("Enter x1 y1: ").split())
x2, y2 = map(int, input("Enter x2 y2: ").split())
x3, y3 = map(int, input("Enter x3 y3: ").split())

if is_collinear(x1,y1,x2,y2,x3,y3):
    print("Points are collinear")
else:
    print("Points are not collinear")