t = (10,20,30,40)
print("Original tuple:",t)
temp=list(t)
temp[2]=99
t=tuple(temp)
print("Modified tuple:",t)

