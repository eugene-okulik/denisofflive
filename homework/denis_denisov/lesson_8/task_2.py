"""
Задание 2

Напишите функцию-генератор, которая генерирует список чисел фибоначчи
Распечатайте из этого списка пятое число, двухсотое число, тысячное число, стотысячное число

"""
import sys

sys.set_int_max_str_digits(0)


def fibonacci_generator():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


fibonacci = fibonacci_generator()

fifth_number = next(fibonacci)
for _ in range(4):
    fifth_number = next(fibonacci)

two_hundredth_number = next(fibonacci)
for _ in range(195):
    two_hundredth_number = next(fibonacci)

thousandth_number = next(fibonacci)
for _ in range(799):
    thousandth_number = next(fibonacci)

hundred_thousandth_number = next(fibonacci)
for _ in range(99999):
    hundred_thousandth_number = next(fibonacci)

print("Пятое число Фибоначчи:", fifth_number)
print("Двухсотое число Фибоначчи:", two_hundredth_number)
print("Тысячное число Фибоначчи:", thousandth_number)
print("Стотысячное число Фибоначчи:", hundred_thousandth_number)
