def convert_string_to_lowercase(string):
    lower_string=""
    for char in string:
        if "A"<=char<="Z":
            lower_string+=chr(ord(char)+32)
        else:
            lower_string+=char
    return lower_string
def convert_string_to_uppercase(string):
    upper_string=""
    for char in string:
        if "a"<=char<="z":
            upper_string+=chr(ord(char)-32)
        else:
            upper_string+=char
    return upper_string
def alternate_string(string):
    alt_string=""
    for char in string:
        if "a"<=char<="z":
            alt_string+=chr(ord(char)-32)
        elif "A"<=char<="Z":
            alt_string+=chr(ord(char)+32)
        else:
            alt_string+=char
    return alt_string
str1="HeLLo WoRld This IS A string"

print("To lowercase:",convert_string_to_lowercase(str1))
print("To uppercase:",convert_string_to_uppercase(str1))
print("Toggle case:",alternate_string(str1))