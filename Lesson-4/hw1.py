"""
Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
В расчете необходимо использовать формулу: (выработка в часах*ставка в час) + премия.
 Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.
"""
from sys import argv
# Вводим названия в argv
name, production, rate, prize = argv
# Приводим переменные к типу Float
production = float(production)
rate = float(rate)
prize = float(prize)
result = (production * rate) + prize
print("Заработная плата сотрудника составляет: {:.2f} рублей".format(result))
