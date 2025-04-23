marks=[]
print("Enter marks of 3 subjects out of 100:")
average=0
for i in range(3):
    marks.append(int(input()))
    average+=(marks[i]/3)
print("Average marks are:",average)
