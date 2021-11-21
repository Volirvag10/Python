with open('File_5.3.txt', 'r', encoding = 'utf-8') as my_file:
    file_lines = my_file.readlines()
    employees = {}
    sum_salary = 0
    for line in file_lines:
        emp_info = line.split()
        employees.update({emp_info[0]: float(emp_info[1])})
        sum_salary += float(emp_info[1])

average_sal = sum_salary / len(employees)
print(f'Среднее значение: {average_sal}')

for k, v in employees.items():
    if v < 20000:
        print(f'{k}: {v}')