def count_digits(number):
    if number == 0:
        return 1 
    count=0
    number=abs(number)
    while number>0:
        number=number// 10
        count=count+1
    return count
num=int(input("Enter a number:"))
digits = count_digits(num)
print("Number of digits:", digits)
