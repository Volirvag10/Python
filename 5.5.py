with open ('Lesson_5.5.txt', 'w') as f_obj:
    line = input('Введите строку из чисел, разделенных пробелом: \n')
    f_obj.writelines(line)
    str = line.split()
    print('Сумма чисел в файле: ', sum(map(int, str)))