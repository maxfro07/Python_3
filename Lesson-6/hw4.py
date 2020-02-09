"""
- 4. Реализуйте базовый класс Car.У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево)
 А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда)
  Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс метод show_speed,
  который должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar переопределите метод show_speed
  При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
  Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
  Выполните вызов методов и также покажите результат.
"""


class Car:
    def __init__(self, speed, color, name):
        self.speed = speed
        self.color = color
        self.name = name

    def car_go(self):
        print('Машина {} начала свое движение!'.format(self.name))

    def car_stop(self):
        print('Машина {} остановилась!'.format(self.name))

    def car_turn(self, direction):
        print('Машина {} повернула {}!'.format(self.name, direction))

    def show_speed(self):
        return print(self.speed)


class TownCar(Car):
    def __init__(self, speed, color, name, is_police=False):
        Car.__init__(self, speed, color, name)
        self.is_police = is_police
        if self.speed > 60:
            print('Превышение скорости!!')


class SportCar(Car):
    def __init__(self, speed, color, name, is_police=False):
        Car.__init__(self, speed, color, name)
        self.is_police = is_police
        if self.speed > 40:
            print('Превышение скорости! Но полиция не догонит)')


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police=False):
        Car.__init__(self, speed, color, name)
        self.is_police = is_police
        if self.speed > 40:
            print('Превышение скорости!!')


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police=True):
        Car.__init__(self, speed, color, name)
        self.is_police = is_police


my_car1 = PoliceCar(150, 'Red', 'Lamborghini Police')

my_car1.car_go()
my_car1.car_turn('Налево')
my_car1.car_stop()
my_car1.show_speed()
print('#' * 30 + "\n")

my_car2 = TownCar(100, "Black", 'Volkswagen Town')

my_car2.car_go()
my_car2.car_turn('Направо')
my_car2.car_stop()
my_car2.show_speed()
print('#' * 30 + "\n")

my_car3 = SportCar(200, "Blue", 'Ferrari Sport')

my_car3.car_go()
my_car3.car_turn('Направо')
my_car3.car_stop()
my_car3.show_speed()
print('#' * 30 + "\n")

my_car4 = WorkCar(50, "Grey", 'VAZ Work')

my_car4.car_go()
my_car4.car_turn('Налево')
my_car4.car_stop()
my_car4.show_speed()
print('#' * 30 + "\n")
