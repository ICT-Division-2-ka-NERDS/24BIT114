data = {
    101:[(1,25000),(2,32000),(3,28000)],
    102:[(4,45000),(5,40000)],
    103:[(6,30000),(7,30000),(8,35000)]
}
for dept,employees in data.items():
    salaries=[salary for _,salary in employees]
    print(f"\nDepartment {dept}")
    print("Minimum Salary:",min(salaries))
    print("Maximum Salary:",max(salaries))
