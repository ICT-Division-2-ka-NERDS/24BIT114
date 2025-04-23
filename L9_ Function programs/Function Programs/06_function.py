def squarecube(a):
    l1=[]
    for i in range(1,a+1):
        l1.append((i,i*i,i*i*i))
    return(l1)
l=squarecube(6)
print(l)
