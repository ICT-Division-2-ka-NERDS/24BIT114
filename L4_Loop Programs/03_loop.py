str1=str(input("Enter a string:"))
alphabets=0
digits=0
for i in range(len(str1)):
    if str1[i].isalpha():
        alphabets=alphabets+1
    elif str1[i].isdigit():
        digits=digits+1
print("Total Alphabets in string are:",alphabets)
print("Total Digits in string are:",digits)