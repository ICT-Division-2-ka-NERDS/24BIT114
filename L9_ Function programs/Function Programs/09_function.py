def alphanum(str1):
    print("String is:",str1)
    dict={}
    numbers=0
    alpha=0
    for i in range(len(str1)):
        if str1[i].isnumeric():
            numbers=numbers+1
            dict["Numerics"]=numbers
        elif str1[i].isalpha():
            alpha=alpha+1
            dict["Alphabets"]=alpha
    return(dict)
dict1=alphanum("My name is Robot1111")   
print(dict1)