source_list = [9, 9, 9, 8, 75, 2, 66, 66, 5, 4, 12, 35, 88, 39]
print(source_list)

new_list = [el for el in source_list if source_list.count(el) == 1]
print(new_list)