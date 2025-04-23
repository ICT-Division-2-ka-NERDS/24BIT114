import random
set1={random.randint(15,45) for _ in range (10)}
print("Original set:",set1)
count_less_30=sum(1 for num in set1 if num<30)
print("Numbers less than 30 are:",count_less_30)
set2={i for i in set1 if i>=35}
print("Updated set:",set2)