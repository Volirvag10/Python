from itertools import count

num = int(input('Введите число, с которого начнется список: '))
for el in count(num):
    if el > 20:
        break
    else:
        print(el)