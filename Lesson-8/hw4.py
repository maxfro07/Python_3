"""
4. Начните работу над проектом «Склад оргтехники».
Создайте класс, описывающий склад. А также класс «Оргтехника», который будет базовым для классов-наследников.
Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
В базовом классе определить параметры, общие для приведенных типов.
В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.
"""


class Store:
    def __init__(self, name, size):
        self.name = name
        self.size = size


class Appliances:
    def __init__(self, name, color, quantity):
        self.name = name
        self.color = color
        self.quantity = quantity


class Printer(Appliances):
    def __init__(self, name, color, quantity, performance, permission):
        super().__init__(name, color, quantity)
        self.print_speed = performance
        self.permission = permission


class Scanner(Appliances):
    def __init__(self, name, color, quantity, interface):
        super ().__init__(name, color, quantity)
        self.interface = interface


class Xerox (Appliances):
    def __init__(self, name, color, quantity, copying_speed):
        super().__init__(name, color, quantity)
        self.copying_speed = copying_speed


printer = Printer('Kyocera', 'White', 15, '35 л/мин', '1 200 точек на дюйм')
scanner = Scanner('Canon', 'Black', 20, 'Hi-Speed USB 2.0 ')
xerox = Xerox('Xerox', 'White', 10, '28 стр/мин')
