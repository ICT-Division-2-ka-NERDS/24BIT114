import random
celsius=[random.randint(30,40) for _ in range (10)]
print("Celsuis temperatures:",celsius)
farenheit=[]
for i in range(len(celsius)):
    farenheit.append((celsius[i]*9/5)-32)
print("farenheit temperatures:",farenheit)