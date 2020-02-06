"""
1. Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
 Об окончании ввода данных свидетельствует пустая строка.
"""
import os

dir_name = os.path.dirname(__file__)
name = input('Введите имя файла: ')
file_name = os.path.join(dir_name, name)

f = open(name, 'w', encoding='UTF-8')
while True:
    s = input("Введите текст в файл: ")
    if s == '':
        break
    f.write(s+'\n')
f.close()
