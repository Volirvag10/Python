def function(n):
    x = 1
    for el in range(1, n + 1):
        x *= el
        yield x
        
n = int(input("Факториал какого числа Вы хотели бы узнать: ")) 
for n in function(n):
    print(n)