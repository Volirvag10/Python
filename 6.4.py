class Car:
    
    def __init__(self, name, speed, color, is_police = False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
    
    def go(self):
        return f'Вы едете за рулем автомобиля {self.name} цвета {self.color} металлик.'

    def stop(self):
        return f'\nАвтомобиль {self.name} остановился.'

    def turn(self, direction):
        return f'\nАвтомобиль {self.name} повернул {direction}'

    def show_speed(self):
        return f'\nСкорость автомобиля в км/ч: {self.speed}'
    
class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            return f'\nВаша скорость выше позволенной и составляет {self.speed} км/ч'
        else:
            return f'Ваша скорость в пределах нормы и составляет {self.speed} км/ч'

class SportCar(Car):
    pass

class PoliceCar(Car):
    pass
        
class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            return f'\nВаша скорость выше позволенной и составляет {self.speed} км/ч'
        else:
            return f'Ваша скорость в пределах нормы и составляет {self.speed} км/ч'  

town = TownCar('BMW', 70, 'White', False)
print('1:\n' + town.go(), town.show_speed(), town.turn('налево'), town.turn('направо'), town.stop())

sport = SportCar('lamborghini', 250, 'Yellow', False)
print('2:\n' + sport.go(), sport.show_speed(), sport.turn('налево'), sport.turn('налево'), sport.turn('налево'), sport.stop())

work = WorkCar('KIA', 35, 'Black', False)
print('3:\n' + work.go(), work.show_speed(), work.turn('направо'), work.stop())

police = PoliceCar('Ford', 100, 'Black/White', True)
print('4:\n' + police.go(), police.show_speed(), police.turn('налево'), police.stop())