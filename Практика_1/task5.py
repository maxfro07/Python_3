# 5. Запросите у пользователя значения выручки и издержек фирмы.
# Определите, с каким финансовым результатом работает фирма (прибыль — выручка больше издержек, или убыток — издержки больше выручки).
# Выведите соответствующее сообщение. Если фирма отработала с прибылью, вычислите рентабельность выручки (соотношение прибыли к выручке).
# Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчете на одного сотрудника.

revenue = int(input("Введите значение выручки: "))
cost = int(input("Введите значение убытка: "))
profit = 0      # revenue > cost - Прибыль

if revenue > cost:
    print("Финансовый результат работы фирмы - прибыль")
    profit = revenue - cost
    return_on_revenue = profit / revenue * 100
    print(return_on_revenue, "%")
    number_of_staff = int(input("Введите количество сотрудников в компании: "))
    print("Прибыль фирмы в расчете на одного сотрудника равна: ", profit / number_of_staff)
else:
    print(" Финансовым результатом работы фирмы - убыток")