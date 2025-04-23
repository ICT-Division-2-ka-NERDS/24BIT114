food_items=[("burger",50),("pizza",100),("pasta",150),("macroni",170),("icecream",100),("hotdog",20)]
for i in range(len(food_items)):
    for j in range(0, len(food_items) - i - 1):
        if food_items[j][1]<food_items[j + 1][1]:  
            food_items[j],food_items[j + 1]=food_items[j + 1],food_items[j]
print(food_items)