"""
Задача 3: Даны два числа. Найти среднее арифметическое и среднее геометрическое этих чисел
"""

num1 = float(input("Введите первое число: "))
num2 = float(input("Введите второе число: "))

average_arithmetic = (num1 + num2) / 2
average_geometric = (num1 * num2) ** 0.5

print(f"Среднее арифметическое: {average_arithmetic}")
print(f"Среднее геометрическое: {average_geometric}")
