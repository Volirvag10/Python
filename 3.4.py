def my_func():
    x = float(input('Введите действительное положительное число: '))
    y = int(input('Введите целое отрицательное число: '))
    res = 1
    for i in range(abs(y)):
        res *= x
    if y != 0:
        return 1 / res
    else:
        return 1

full_func = my_func()
print(full_func)