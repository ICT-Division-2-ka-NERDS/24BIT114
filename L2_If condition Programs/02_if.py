def greatest(a,b,c):
    return max(a,b,c)
def lowest(a,b,c):
    print(f"Numbers are {a}, {b} & {c}")
    return min(a,b,c)
smallest=lowest(12,-1,13)
print("Smallest number is:",smallest)
largest=greatest(12,-1,13)
print("Largest number is:",largest)