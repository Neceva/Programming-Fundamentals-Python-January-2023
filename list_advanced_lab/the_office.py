def happy_employee_count(empl_list):
    happy_counter = 0
    for employee in double_employees_happiness:
        if employee >= average_happiness:
            happy_counter += 1
    return happy_counter


employees_happiness = list(map(int, input().split()))
factor = int(input())

double_employees_happiness = list(map(lambda x: x * factor, employees_happiness))
average_happiness = sum(double_employees_happiness) / len(double_employees_happiness)

happy_count = happy_employee_count(double_employees_happiness)
if happy_count >= len(double_employees_happiness) / 2:
    print(f"Score: {happy_count}/{len(double_employees_happiness)}. Employees are happy!")
else:
    print(f"Score: {happy_count}/{len(double_employees_happiness)}. Employees are not happy!")
