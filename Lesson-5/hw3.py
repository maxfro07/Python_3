"""
+3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
Выполнить подсчет средней величины дохода сотрудников.
"""
from os import path

# Определяю путь к файлу
file_name = path.join(path.dirname(__file__), "HomeWork3.txt")

# Записываю в файл данные
f = open(file_name, 'w', encoding='UTF-8')

while True:
    s = input("Введите текст в файл, как закончите, оставьте пустую строку: ")
    if s == '':
        break
    f.write(s+'\n')

# Нахожу фамилии сотрудников с ЗП менее 20 тыс.
with open(file_name, 'r', encoding='utf-8') as f:
    for line in f.readlines():
        name, value = line.split()
        if float(value) < 20000:
            print(f"Фамилии сотрудников с зп меньше 20000: {name}")


# Выполняю подсчет средней величины дохода сотрудников
with open(file_name, 'r', encoding='utf-8') as f:
    money = 0
    count = 0
    for line in f:
        work = line.split()
        money += float(work[1])
        count += 1
    # svd = money / count
    print(f'Средняя величина дохода сотрудников: {money / count}')
