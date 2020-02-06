"""
2. Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.
"""
from os import path

file_name = path.join(path.dirname(__file__), "HomeWork2.txt")

file = open(file_name, 'r', encoding='UTF-8')
line = 0
for i in file:
    line += 1

    flag = 0
    word = 0
    for j in i:
        if j != ' ' and flag == 0:
            word += 1
            flag = 1
        elif j == ' ':
            flag = 0

    print(i, len(i), 'символов', word, 'сл.')

print(line, 'стр.')
file.close()
