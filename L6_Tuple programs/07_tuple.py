t = (10,20,30,40)
print("Original tuple:",t)
temp=list(t)
del temp[1]
t=tuple(temp)
print("Tuple after deletion:", t)

