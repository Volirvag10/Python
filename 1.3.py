n = int(input("Введите цифру: "))
n1 = int(f'{n}{n}')
n2 = int(f'{n}{n}{n}')
print('Сумма в формате "n + nn + nnn" = ', n+n1+n2)