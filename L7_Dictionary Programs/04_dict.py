str1=str(input("Enter a string:"))
char_freq={}
for char in str1:
    char_freq[char]=char_freq.get(char,0)+1
print(char_freq)
