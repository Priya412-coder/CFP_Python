import random
def employee_wage():
    is_present = 1
    is_parttime = 2
    salary_per_hour = 20
    check = random.randrange(0,3)
    if is_present == check:
        working_hour = 8
        print("Employee has worked for fullday")
    elif is_parttime == check:
        working_hour = 4
        print("Employee has worked for halfday")
    else:
        working_hour = 0
        print("Employee is absent")
    employee_salary = salary_per_hour * working_hour
    print("Employee will get salary of ",employee_salary)
employee_wage()