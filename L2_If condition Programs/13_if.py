def number_to_word(n):
    words = ["zero","one","two","three","four","five","six","seven","eight","nine","ten","eleven","twelve","thirteen","fourteen","fifteen",
                "sixteen","seventeen","eighteen","nineteen"]
    if 0<=n<=19:
        print(words[n])
number=int(input("Enter a number:"))
number_to_word(number)
                