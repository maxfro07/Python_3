# 1. Поработайте с переменными, создайте несколько, выведите на экран,
# запросите у пользователя несколько чисел и строк и сохраните в переменные,
# выведите на экран.

name = 'Максим'
surname = 'Фролов'
age = 26

print('Привет!', name, surname, age, 'лет')
print('#' * 30)
name = input("Введите Ваше имя: ")
surname = input("Введите Вашу фамилию: ")
age = int(input("Введите Ваш возраст: "))
print('Привет!', name, surname, age, 'лет')
print('#' * 30)

number_1 = int(input("Введите любое число: "))
number_2 = int(input("Введите другое любое число: "))
number_3 = int(input("Введите еще одно другое любое число: "))
sum = number_1 + number_2 + number_3
print("Сумма чисел равна: ", sum)
print('#' * 30)

text = input("Введите текст")
another_text = input("Введите другой текст")
print(text)
print(another_text)