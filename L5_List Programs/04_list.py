import random
integer_list=[random.randint(-20,20) for _ in range(30)]
pos_list=[]
neg_list=[]
for i in range(len(integer_list)):
    if integer_list[i]<0:
        neg_list.append(integer_list[i])
    elif integer_list[i]>0:
        pos_list.append(integer_list[i])
print("Negative integer list is:",sorted(neg_list))
print("Positive integer list is:",sorted(pos_list))

