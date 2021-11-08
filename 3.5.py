def my_func(nums_str, stop):
    nums_list = nums_str.split(' ')
    sum = 0
    for i in nums_list:
        if i == stop:
            break
        sum += int(i)
    return sum
    

stopper = '#'
finished = False
s = 0
while not finished:
    my_list_nums = input("Введите числа, разделенные пробелом: ")
    s += my_func(my_list_nums, stopper)
    finished = stopper in my_list_nums
    print(f'Сумма: {s}')
