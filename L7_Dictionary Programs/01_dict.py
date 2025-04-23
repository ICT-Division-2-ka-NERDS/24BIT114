dict1={"key1":"value1","key2":"value2","key3":"value3"}
dict2={"num1":1,"num2":2,"num3":3}
dict3={"subject1":"cp","subject2":"maths","subject3":"EEE"}

dict4={**dict1,**dict2,**dict3}
print("Concatenated dictionary:",dict4)