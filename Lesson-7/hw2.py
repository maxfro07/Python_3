"""
2. Реализовать проект расчета суммарного расхода ткани на производство одежды.
Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
К типам одежды в этом проекте относятся пальто и костюм.
У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма).
Это могут быть обычные числа: V и H, соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5),
для костюма (2 * H + 0.3). Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания:
реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.
"""

from abc import ABC, abstractmethod


class Dress (ABC):

    @abstractmethod
    def fabric_consumption(self):
        pass


class Coat(Dress):
    def __init__(self, name='Пальто'):
        self.name = name

    @property
    def fabric_consumption(self):
        while True:
            try:
                v = float(input('Введите размер пальто.\n'))
            except ValueError:
                print('Неправильный ввод, попробуйте еще раз. Размер нужно вводить в цифрах')
            else:
                fabric_cons = (v / 6.5) + 0.5
                break
        return fabric_cons.__round__(2)


class Suit(Dress):
    def __init__(self, name='Костюм'):
        self.name = name

    @property
    def fabric_consumption(self):
        while True:
            try:
                h = float(input('Введите рост в метрах.\n'))
            except ValueError:
                print('Неправильный ввод, попробуйте еще раз. Рост нужно вводить в цифрах')
            else:
                fabric_cons = (2 * h) + 0.3
                break
        return fabric_cons.__round__(2)


if __name__ == '__main__':
    coat = Coat()
    suit = Suit()
    cons1 = coat.fabric_consumption
    print(f'Расход ткани для пальто: {cons1} м.')
    cons2 = suit.fabric_consumption
    print(f'Расход ткани для костюма: {cons2} м.')
    print("*" * 20)
    print(f'Общий расход ткани равен: {(cons1 + cons2).__round__(2)} м.')
