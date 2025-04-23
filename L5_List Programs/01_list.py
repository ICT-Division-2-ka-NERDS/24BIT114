import random
even_list= random.sample(range(0, 100, 2), 5)
odd_list = random.sample(range(1, 100, 2), 5)
print("Even list:",even_list)
print("\nOdd list:",odd_list)
odd_list.insert(2,even_list)
flatenned_list=[]
for item in odd_list:
    if isinstance(item,list):
        flatenned_list.extend(item)
    else:
        flatenned_list.append(item)
print("\nFlattened list is:",flatenned_list)
print("Sorted list is:",sorted(flatenned_list))