def remove_string(onestring,removestring):
    return onestring.replace(removestring,"")
str1="abcdef"
str2="bc"
str_new=remove_string(str1,str2)
print(str_new)
