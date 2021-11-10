from itertools import cycle

num_list = [20, 30, 40, 'none', 60, False, 80, 100, 'It`s list', 120]
с = 1
for el in cycle(num_list):
    if с > 7:
        break
    print(el)
    с += 1