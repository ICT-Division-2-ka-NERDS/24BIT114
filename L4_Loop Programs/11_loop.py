import math
x_deg=float(input("Enter x in degrees:"))
x_rad=x_deg*(math.pi/180)
sinx=0
for i in range(1,10,2):
    sinx=sinx+ ((x_rad**i)*((-1)**((i-1)//2)))/math.factorial(i)

print("sin(x)=",sinx)