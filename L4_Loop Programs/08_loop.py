num=int(input("Enter a number to calculate its factorial:"))
fact=1
for i in range(1,num+1):
    fact=fact*i
print("Factorial is :",fact)