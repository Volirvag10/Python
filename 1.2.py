time_vvod = int(input("Введите время в секундах: "))
time_hour = time_vvod // 3600
time_minute = time_vvod % 3600 // 60
time_sec = time_vvod % 3600 % 60
clock = (
    f"{time_hour:02}:"
    f"{time_minute:02}:"
    f"{time_sec:02}"
    )
print(clock)