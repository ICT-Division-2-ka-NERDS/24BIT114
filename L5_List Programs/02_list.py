import random
random_list=[random.randint(1,30) for _ in range(20)]
print("Random list is:",random_list)
a=int(input("Enter a number:"))
print(f"The position of occourences of {a} in random list are:")
count=0
for i in range(len(random_list)):
    if random_list[i]==a:
        print(i+1)
        count=count+1
if count==0:
    print(f"There are no occourences of {a}")