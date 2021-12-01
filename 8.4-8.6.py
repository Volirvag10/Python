class Warehouse:
    
    def __init__(self, name, price, quantity, *args):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.my_warehouse_full = []
        self.my_warehouse = []
        self.my_unit = {'Модель устройства': self.name, 'Стоимость за ед.': self.price, 'Количество': self.quantity}
        
    def __str__(self):
        return f'{self.name}, стоимость за ед.: {self.price} руб., количество: {self.quantity} шт.'
        
    def reception(self):
        try:
            unit = input(f'Введите модель устройства: ')
            unit_p = int(input(f'Введите стоимость за ед.: '))
            unit_q = int(input(f'Введите количество: '))
            unique = {'Модель устройства': unit, 'Стоимость за ед': unit_p, 'Количество': unit_q}
            self.my_unit.update(unique)
            self.my_warehouse.append(self.my_unit)
            print(f'Текущий список -\n {self.my_warehouse}')
        except:
            return f'Ошибка ввода данных'
            
        print(f'Для выхода нажмите "Q", для продолжения - "Enter"')
        q = input(f'---> ')
        if q == 'Q' or q == 'q':
            self.my_warehouse_full.append(self.my_warehouse)
            print(f'Весь склад: \n {self.my_warehouse_full}')
            return f'Выход'
        else:
            return Warehouse.reception(self)
            
class Printer(Warehouse):
    def to_print(self):
        return f'Принтер печатает.'


class Scanner(Warehouse):
    def to_scan(self):
        return f'Сканер сканирует.'


class Copier(Warehouse):
    def to_copier(self):
        return f'Копир копирует.'


unit_1 = Printer('hp', 2000, 5, 10)
unit_2 = Scanner('Canon', 1200, 5, 10)
unit_3 = Copier('Xerox', 1500, 1, 15)
print(unit_1.reception())
print(unit_2.reception())
print(unit_3.reception())
print(unit_1.to_print())
print(unit_3.to_copier())