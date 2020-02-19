"""
5. Продолжить работу над первым заданием.
Разработать методы, отвечающие за приём оргтехники на склад и передачу в определенное подразделение компании.
Для хранения данных о наименовании и количестве единиц оргтехники, а также других данных,
можно использовать любую подходящую структуру, например словарь.
"""


class Store:

    def __init__(self, name):
        self.name = name
        self.__goods = []

    def add_app(self, tech):
        self.__goods.append(tech)

    def __getitem__(self, item):
        return self.__goods[item]

    def __str__(self):
        return


class Appliances(Store):
    def __init__(self, name, color, quantity):
        self.name = name
        self.color = color
        self.quantity = quantity

    def __str__(self):
        return f'{self.name}, цвет - {self.color}, количество -- {self.quantity}'


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


printer1 = Printer('Kyocera', 'White', 15, '35 л/мин', '1 200 точек на дюйм')
scanner1 = Scanner('Canon', 'Black', 20, 'Hi-Speed USB 2.0 ')
xerox1 = Xerox('Xerox', 'White', 10, '28 стр/мин')
printer2 = Printer('Samsung', 'Black', 20, '40 л/мин','1 200 точек на дюйм')
scanner2 = Scanner('Canon', 'Gray', 30, 'Hi-Speed USB 3.0 ')
xerox2 = Xerox('Xerox', 'Gray', 20, '28 стр/мин')
store = Store('Склад')
unit = Store('ДИТ')
store.add_app(printer1)
unit.add_app(printer2)
store.add_app(scanner1)
unit.add_app(scanner2)
store.add_app(xerox1)
unit.add_app(xerox2)
print(store[0])
print(unit[0])
