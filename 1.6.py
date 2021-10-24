km_nach = float(input("Введите начальное количество километров: "))
km_treb = float(input("Введите требуемое количество километров: "))
day = 1
while km_treb - km_nach > 0:
    km_nach = km_nach + (km_nach * 0.1)
    day += 1
print("Порядковый номер дня: ", day)