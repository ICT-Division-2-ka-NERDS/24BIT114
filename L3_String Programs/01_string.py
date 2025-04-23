str1=str(input("Enter a string:"))
no_of_vowels=0
for i in range(len(str1)):
    if str1[i]=='a' or str1[i]=='e' or str1[i]=='i' or str1[i]=='o' or str1[i]=='u'  or str1[i]=='A' or str1[i]=='E' or str1[i]=='I' or str1[i]=='O' or str1[i]=='U':
        no_of_vowels=no_of_vowels+1
print(no_of_vowels)