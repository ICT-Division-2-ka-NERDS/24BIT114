def check_string(str1,str2):
    if str2 in str1:
        return True
    else:
        return False
bool1=check_string("Hello World","World!")
bool2=check_string("Hello !World!","World")
bool3=check_string("Hello !World"," World")
print(bool1)
print(bool2)
print(bool3)
