import random
random_list=[random.randint(1,31) for _ in range(50)]
print("Random list is:",random_list)
print("New list without duplicates:",list(set(random_list)))
