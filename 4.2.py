source_list = [200, 4, 15, 24, 2, 2, 7, 19, 8, 1, 98, 145, 77]
print(source_list)

new_list = []
for el in range(len(source_list) - 1):
    if source_list[el] < source_list[el + 1]:
        new_list.append(source_list[el + 1])
        
print(new_list)