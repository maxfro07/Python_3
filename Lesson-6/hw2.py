"""
2. Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина).
Значения данных атрибутов должны передаваться при создании экземпляра класса.
Атрибуты сделать защищенными. (_length, _width)
Определить метод расчета массы асфальта, необходимого для покрытия всего дорожного полотна.
Использовать формулу: длина*ширина*масса асфальта для покрытия одного кв метра дороги асфальтом,
толщиной в 1 см*число см толщины полотна. Проверить работу метода.
Например: 20м*5000м*25кг*5см = 12500 т
"""


class Road:
    _length = None
    _width = None
    asphalt = 25
    depth = 5

    def __init__(self, length, width):
        self._width = width
        self._length = length

    def mass_asphalt(self):
        return (self._length * self._width * self.asphalt * self.depth) / 1000


road = Road(length=10000, width=20)
print(road.mass_asphalt())