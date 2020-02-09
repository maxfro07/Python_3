"""
5. Реализовать класс Stationery (канцелярская принадлежность).
Определить в нем атрибут title (название) и метод draw (отрисовка).
Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер)
В каждом из классов реализовать переопределение метода draw.
Для каждого из классов методы должен выводить уникальное сообщение.
Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.
"""


class Stationery:
    title = None

    def draw(self):
        return "Запуск отрисовки."


class Pen(Stationery):
    title = 'Клас ручка'

    def draw(self):
        return self.title


class Pencil(Stationery):
    title = 'Клас карандаш'

    def draw(self):
        return self.title


class Handle(Stationery):
    title = 'Клас маркер'

    def draw(self):
        return self.title


pen = Pen()
pencil = Pencil()
handle = Handle()
stationery = Stationery()

print(stationery.draw())
print(pen.draw())
print(pencil.draw())
print(handle.draw())