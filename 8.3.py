class Error:
    def __init__(self, *args):
        self.my_list = []

    def my_input(self):
        while True:
            try:
                val = int(input('Введите значения и нажимайте Enter: '))
                self.my_list.append(val)
                print(f'Текущий список - {self.my_list} \n ')
            except:
                print(f'Введено недопустимое значение')
                question = input(f'Попробовать еще раз? Y/N ')

                if question == 'Y' or question == 'y':
                    print(try_except.my_input())
                elif question == 'N' or question == 'n':
                    return f'Вы вышли'
                else:
                    return f'Вы вышли'
                
try_except = Error(1)
print(try_except.my_input())