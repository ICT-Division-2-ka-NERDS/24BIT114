import math

n=int(input("Enter n:"))
r=int(input("Enter r:"))

if r>n:
    print("r should be less than or equal to n")
else:
    print("nCr=",math.comb(n, r))
    print("nPr=",math.perm(n, r))
