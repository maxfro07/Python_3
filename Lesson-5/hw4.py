"""
4. Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл.
"""

from os import path

# Определяю путь к файлам
file_name = path.join(path.dirname(__file__), "HomeWork4.txt")
file_name2 = path.join(path.dirname(__file__), "HomeWork4_program.txt")

# Сосздаю
replace = {'Один': 'One',
           'Два': 'Two',
           'Три': 'Three',
           'Четыре': 'Four',
           'Пять': 'Five',
           'Шесть': 'Six',
           'Семь': 'Seven',
           'Восемь': 'Eight',
           'Девять': 'Nine',
           'Десять': 'Ten'}

with open(file_name, "r", encoding="utf-8") as f_in, open(file_name2, 'w', encoding="utf-8") as f_out:
    for line in f_in.readlines():
        eng_number, separator, number = line.split()
        for key, value in replace.items():
            if value == eng_number:
                res_numeral = key
                line = res_numeral, separator, number, "\n"
                new_line = ' '.join(line)
                f_out.write(new_line)
