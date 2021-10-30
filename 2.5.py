my_list = [7, 5, 3, 3, 2]
print(f"Рейтинг - {my_list}")
chislo = int(input("Введите новое значение (111 - выход) "))
while chislo != 111:
    for el in range(len(my_list)):
        if my_list[el] == chislo:
            my_list.insert(el + 1, chislo)
            break
        elif my_list[0] < chislo:
            my_list.insert(0, chislo)
        elif my_list[-1] > chislo:
            my_list.append(chislo)
        elif my_list[el] > chislo and my_list[el + 1] < chislo:
            my_list.insert(el + 1, chislo)
    print(f"Текущий Рейтинг - {my_list}")
    chislo = int(input("Введите число "))