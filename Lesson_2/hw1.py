'''1. Создать список и заполнить его элементами различных типов данных.
Реализовать скрипт проверки типа данных каждого элемента. Использовать функцию type() для проверки типа.
Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.
'''


lst_1 = [1, 'f', 'a', 10, 20.1, "строка", True, (2, 3), {25, 12, 14}, {'key1': 'value', 'key2': 'value2'}]

for itm in lst_1:
    print(type(itm))