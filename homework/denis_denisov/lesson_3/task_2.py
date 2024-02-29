"""
Задача 2: Даны числа x и y. Получить x − y / 1 + xy
"""

x = float(input("Введите значение x: "))
y = float(input("Введите значение y: "))

result = x - y / (1 + x * y)
print("Результат: ", result)
