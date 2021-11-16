def personal_data():
	name = str(input('Введите имя: '))
	surname = str(input('Введите фамилию: '))
	year = str(input('Введите год рождения: '))
	city = str(input('Введите город проживания: '))
	email = str(input('Введите e-mail: '))
	tel = str(input('Введите телефон: '))
	data = f'{name} {surname} {year} {city} {email} {tel}'
	return data

full_data = personal_data()
print(full_data)