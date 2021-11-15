with open('File_5.2.txt', 'r', encoding = "utf-8") as file:
    my_list = file.readlines()
    for i in range(len(my_list)):
        new_l = my_list[i].split()
        print(f'Количество строк в файле {len(my_list)}. В {i + 1}-ой строке {len(new_l)} слов(а)')
