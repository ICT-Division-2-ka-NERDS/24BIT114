def get_grade(marks):
    if marks==-1:
        return "NA"
    elif 0<=marks<=39:
        return "F"
    elif 40<=marks<=44:
        return "P"
    elif 45<=marks<=49:
        return "C"
    elif 50<=marks<=54:
        return "B"
    elif 55<=marks<=59:
        return "B+"
    elif 60<=marks<=69:
        return "A"
    elif 70<=marks<=79:
        return "A+"
    elif 80<=marks<=100:
        return "O"
    else:
        return "Invalid"

def is_fail(marks):
    for m in marks:
        if m==-1 or m<=39:
            return True
    return False

marks=[]
for i in range(1, 4):
    entry=input(f"Enter marks for subject {i} (enter -1 if absent): ")
    marks.append(int(entry))

grades=[get_grade(m) for m in marks]
total=sum(m for m in marks if m != -1)
count=sum(1 for m in marks if m != -1)
average=total / count if count != 0 else 0
status="Fail" if is_fail(marks) else "Pass"

print("\nSubject-wise Grades:")
for i in range(3):
    print(f"Subject{i+1}:{grades[i]}")

print(f"\nTotal: {total}")
print(f"Average: {average:.2f}")
print(f"Result: {status}")
