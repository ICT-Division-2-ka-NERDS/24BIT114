names=["siri","alexa",("john","grok"),"gemeni"]
girls_count=0
boys_count=0

for item in names:
    if isinstance(item,(tuple)):
        boys_count=boys_count+len(item)
    else:
        girls_count=girls_count+1
print(girls_count)
print(boys_count)


