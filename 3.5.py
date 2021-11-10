def my_func():
    my_list = input("Введите числа, разделенные пробелом: ").split()
    sum = 0
    sum_res = 0
    i = 0
    while my_list[i] != '#':
        for i in range(len(my_list)):
            if i == '#':
                break
            else:
                sum = sum + int(my_list[i])
        return sum
    
full_func = my_func()
print('Сумма: ', full_func)