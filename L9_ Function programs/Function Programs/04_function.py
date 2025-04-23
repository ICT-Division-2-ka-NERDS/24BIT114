def sum_avg(list):
    sum1=0
    for i in range (len(list)):
        sum1=sum1+list[i]
    avg1=sum1/len(list)
    return(sum1,avg1)
sum,avg=sum_avg([13,15,13,15])
print("Sum is:",sum)
print("Average is:",avg)