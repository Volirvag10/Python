from abc import ABC, abstractmethod

class Textil(ABC):
    @abstractmethod
    def consumption(self):
        pass

class Coat(Textil):
    def __init__(self, width):
        self.width = width
        
    @property
    def consumption(self):
        return self.width / 6.5 + 0.5

class Jacket(Textil):
    def __init__(self, height):
        self.height = height
        
    @property
    def consumption(self):
        return self.height * 2 + 0.3
        
    def sum_consumption(self, list_jackets):
        a = 0
        for jacket in list_jackets:
            a += jacket.consumption
        return a


coat = Coat(52)
jacket = Jacket(182)
jacket_1 = Jacket(176)
jacket_2 = Jacket(154)
jacket_3 = Jacket(202)
list_jackets = [jacket, jacket_1, jacket_2, jacket_3]
print(coat.consumption)
print(jacket.consumption)
print(jacket.sum_consumption(list_jackets))