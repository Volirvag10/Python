import json
companies = {}
pos_count, pos_sum = 0, 0
with open('File_5.7.txt', 'r', encoding = 'utf-8') as file:
    file_lines = file.readlines()
    for line in file_lines:
        data = line.split()
        profit = float(data[2]) - float(data[3])
        companies.update({data[0]: profit})
        if profit > 0:
            pos_count += 1
            pos_sum += profit

average_profit = pos_sum / pos_count
result = [companies, {'Средняя прибыль: ', average_profit}]

with open('Result_json.txt', 'w', encoding = 'utf-8') as file:
    json.dump(result, file)