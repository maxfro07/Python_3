"""
6. Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие лекционных,
практических и лабораторных занятий по этому предмету и их количество.
Важно, чтобы для каждого предмета не обязательно были все типы занятий.
Сформировать словарь, содержащий название предмета и общее количество занятий по нему. Вывести словарь на экран.
Примеры строк файла:
Информатика: 100(л) 50(пр) 20(лаб).
Физика: 30(л) — 10(лаб)
Физкультура: — 30(пр) —
Пример словаря:
{“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}
"""

from os import path
from re import findall

file_name = path.join(path.dirname(__file__), "HomeWork6.txt")

with open(file_name, 'r', encoding='utf-8') as f:
    key_list = []
    value_list = []
    for line in f:
        work = line.split()
        subj, *hours = findall(r'^[\w]*|\d+', line)
        s = sum(list(map(int, hours)))
        key_list.append(subj)
        value_list.append(s)
result_list = dict(zip(key_list, value_list))
print(result_list)