"""
Задание 1

Напишите программу. Есть две переменные, salary и bonus. Salary - int, bonus - bool.
Спросите у пользователя salary. А bonus пусть назначается рандомом.

Если bonus - true, то к salary должен быть добавлен рандомный бонус.

Примеры результатов:

10000, True - '$10255'
25000, False - '$25000'
600, True - '$3785'

"""

import random

salary = int(input("Введите зарплату: "))
bonus = random.choice([True, False])

if bonus:
    bonus_amount = random.randint(1, 5000)
    total_salary = salary + bonus_amount
    print(f'${total_salary}')
else:
    print(f'${salary}')
