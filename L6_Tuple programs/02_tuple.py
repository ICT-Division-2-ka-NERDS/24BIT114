details_students=[("24bit114","Pushkar Shah",18),("Harshil amin","24bit116",12)]
names=[]
roll=[]
age=[]

for item in details_students:
    for ele in item:
        if isinstance(ele,int):
            age.append(ele)
        elif isinstance(ele,str) and "24bit" in ele:
            roll.append(ele)
        else:
            names.append(ele)

print(age)
print(names)
print(roll)