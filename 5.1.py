with open ("C:\\Users\\Валентина\\Desktop\\Глеб\\Программирование\\Основы языка Python\\Урок 5\\File_5.1.txt", "x") as f_obj:
    line = input('Введите строку: \n')
    while line:
        f_obj.writelines(line)
        line = input('Введите текст \n')
        if not line:
            break

with open ("Lesson_5.1.txt", "r") as f_obj:
    content = f_obj.readlines()
    print(content)