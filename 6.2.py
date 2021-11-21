class Road:
    
    def __init__(self, _length, _width, mass_asph, thickness):
        self._length = _length
        self._width = _width
        self.mass_asph = mass_asph
        self.thickness = thickness
    
    def summ_mass(self):    
        summ_mass = self._length * self._width * self.mass_asph * self.thickness / 1000
        print(f'Для покрытия всего дорожного полотна неободимо {summ_mass} тонн(-ы) асфальта')

_length = int(input('Введите длину дороги, м: '))
_width = int(input('Введите ширину дороги, м: '))
mass_asph = int(input('Введите массу асфальта, необходимого для покрытия одного кв. метра дороги асфальтом, толщиной в 1 см, кг: '))
thickness = float(input('Введите толщину дорожного полотна, см: '))

r = Road(_length, _width, mass_asph, thickness)
r.summ_mass()