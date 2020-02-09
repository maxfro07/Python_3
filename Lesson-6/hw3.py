"""
3. Реализовать базовый класс Worker (работник), в котором определить атрибуты:
name, surname, position (должность), income (доход).
Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы:
 оклад и премия, например, {"wage": wage, "bonus": bonus}.
 Создать класс Position (должность) на базе класса Worker.
 В классе Position реализовать методы получения полного имени сотрудника
 (get_full_name) и дохода с учетом премии (get_total_income).
 Проверить работу примера на реальных данных
 (создать экземпляры класса Position, передать данные, проверить значения атрибутов, вызвать методы экземпляров).
"""


class Worker:

    name = None

    surname = None

    position = None

    _income = {
        'wage': 'wage',
        'bonus': 'bonus'
    }


class Position(Worker):

    def __init__(self, name: str, surname: str, wage: float, bonus: float):
        self.name = name
        self.surname = surname
        self._income['wage'] = wage
        self._income['bonus'] = bonus

    def get_full_name(self):
        return self.name + " " + self.surname

    def get_total_income(self):
        return str(self._income['wage'] + self._income['bonus']) + ' руб.'


position = Position("Максим", "Фролов", 15000, 40000)
print(position.name)
print(position.surname)
print(position._income['wage'])         # так делать не хорошо
print(position._income['bonus'])        # так делать не хорошо
print(position.get_full_name())
print(position.get_total_income())