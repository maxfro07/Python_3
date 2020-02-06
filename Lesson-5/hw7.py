"""
7. Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме:
 название, форма собственности, выручка, издержки.
Пример строки файла: firm_1 ООО 10000 5000.
Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
Если фирма получила убытки, в расчет средней прибыли ее не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
Подсказка: использовать менеджеры контекста.
"""

from os import  path
import json

# Определяю путь к файлу hw7.txt и hw7_json.txt
file_name = path.join(path.dirname(__file__), "HomeWork7.txt")
file_name2 = path.join(path.dirname(__file__), "HomeWork7_json.txt")

# Считаем прибыль, убытки, среднюю прибыль и средние убытки
with open(file_name, 'r', encoding='utf-8') as f:
    average_profit_sum = 0      # сумма прибыли
    average_loss_sum = 0        # сумма убытков
    count_profit = 0            # счетчик прибыльных компаний
    count_lost = 0              # счетчик убыточных компаний
    # result_list = []
    key_list = []
    value_list = []

    for line in f.readlines():
        firm, ownership, revenue, cost = line.split()       # Фирма, собственности, выручка, издержки
        profit = int(revenue) - int(cost)                   # Высчитываю прибыль
        print(f"Прибыль {firm} равна: {profit}")
        if profit > 0:                                      # Если прибыль, то добавляю значение фирмы и прибыли
            average_profit_sum += profit                    # в список прибыли
            key_list.append(firm)
            value_list.append(profit)
            """
            result_list.append(firm)
            result_list.append(profit)
            """
            count_profit += 1                               # Увеличиваю счетчик компаний с прибылью
        else:
            average_loss_sum += profit                      # Если убыток, то добавляю в список убытки
            count_lost += 1                                 # Увеличиваю счетчик компаний с убытками
    prof = average_profit_sum / count_profit                # Средняя прибыль
    lost = average_loss_sum / count_lost                    # Средние убытки
    average_profit = {"average_profit": prof}
    average_loss = {"average_lost": lost}

result_list = dict(zip(key_list, value_list))
final_list = [result_list, average_profit, average_loss]    # Финальный список

# Итоговый список сохраняю в виде json-объекта в соответствующий файл
with open(file_name2, 'w', encoding='utf-8') as f:
    json_file = json.dump(final_list, f)

