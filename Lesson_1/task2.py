# 2. Пользователь вводит время в секундах.
# Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
# Используйте форматирование строк.


time_in_seconds = int(input("Введите время в секундах: "))
hour = time_in_seconds // 3600
minutes = (time_in_seconds % 3600) // 60
seconds = (time_in_seconds % 3600) % 60

print(f"{hour:02}:{minutes:02}:{seconds:02}")