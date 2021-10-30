number = int(input("Введите целое положительное число: "))
max_figure = number % 10
number = number // 10
while number > 0:
    if number % 10 > max_figure:
        max_figure = number % 10
    number = number // 10
print("Наибольшая цифра в данном числе: ", max_figure)