vyr = int(input("Введите выручку компании в руб.: "))
izd = int(input("Введите издержки компании в руб.: "))
fin_result = vyr - izd
if fin_result > 0:
	print("Компания получит следующую прибыль: ", fin_result)
	rent = float(((vyr / izd) - 1) * 100)
	print("Рентабельность в процентах: ", rent)
elif fin_result == 0:
	print("Компания работает безубыточно")
else:
	print("Компания несет следующий убыток: ", fin_result)
	
chisl = int(input("Введите численность компании в количестве сотрудников: "))
fin_result_chisl = int(fin_result / chisl)
print("Прибыль на одного сотрудника в руб.: ", fin_result_chisl)