list_of_tuples=[("alina",),(),(12,34),(True,),("samson",),(55,)]
filtered_list=[]
for ele in list_of_tuples:
    if ele:  
        filtered_list.append(ele)
print(filtered_list)