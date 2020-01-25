# 4. Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.
user_number = int(input("Введите целое положительное число: "))
big_number = 0
while user_number != 0:
    last_number = user_number % 10
    if last_number > big_number:
        big_number = last_number
    user_number //= 10
print("Самая большая цифра в числе: ", big_number)