"""
Задание 2
Допустим, какая-то программа возвращает результат своей работы в таком виде:

результат операции: 42

результат операции: 514

результат работы программы: 9

С помощью срезов и метода index получите из каждой строки с результатом число,
прибавьте к полученному числу 10, результат сложения распечатайте.
"""

# Задание 2

result1 = "результат операции: 42"
result2 = "результат операции: 514"
result3 = "результат работы программы: 9"

num1 = int(result1[result1.index(":") + 2:]) + 10
num2 = int(result2[result2.index(":") + 2:]) + 10
num3 = int(result3[result3.index(":") + 2:]) + 10

print(num1)
print(num2)
print(num3)
