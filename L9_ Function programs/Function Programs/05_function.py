def ispangram(str1):
    print(str1)
    str1=str1.lower()
    a=set(str1)
    count=0
    for i in range(97,123):
        if chr(i) in a:
            count=count+1
    if count==26:
        print("String is a pangram")
    else:
        print("It is not a pangram")
ispangram("The quick brown fox jumps over the lazy dog")
