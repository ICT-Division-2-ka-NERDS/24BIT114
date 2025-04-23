def count_upper_lower(s):
    upper_count=0
    lower_count=0
    for i in range (len(s)):
        if s[i].isupper():
            upper_count +=1
        elif s[i].islower():
            lower_count +=1
    return(lower_count,upper_count)
lower,upper=count_upper_lower("HELLO i Am in PDeU ")
print("Lower count:",lower)
print("Upper count:",upper)


