def intersection(l1,l2):
    l3=l1+l2
    return(sorted(list(set(l3))))
l=list(intersection(["pushkar","harshil","teerth"],["pushkar","teerth","pushkar","yesha"]))
print(l)