"""
5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""
import os
# Определяю путь к файлу
dir_name = os.path.dirname(__file__)
name = input('Введите имя файла: ')
file_name = os.path.join(dir_name, name)

# Записываю в файл данные
with open(file_name, 'w', encoding='UTF-8') as f:
    print(input("Введите текст в файл: "), file=f)

# Преобразую введенную строку к списку и суммирую значения
with open(file_name, 'r') as f:
    s = f.readline()
s = list(map(int, s.split()))
print(sum(s))
