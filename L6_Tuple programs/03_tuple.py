from datetime import date
date1=(23,11,2005)
date2=(6,3,2007)
d1=date(date1[2], date1[1], date1[0])
d2=date(date2[2], date2[1], date2[0])
if d2>d1:
    print("Days between are:",d2-d1)
elif d1>d2:
    print("Days between are:",d1-d2)