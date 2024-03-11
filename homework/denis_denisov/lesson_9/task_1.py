"""
Задание 1

Обработка даты
Дана такая дата: "Jan 15, 2023 - 12:05:33"

Преобразуйте эту дату в питоновский формат, после этого:

1. Распечатайте полное название месяца из этой даты

2. Распечатайте дату в таком формате: "15.01.2023, 12:05"

"""

from datetime import datetime

# Дата
date_str = "Jan 15, 2023 - 12:05:33"

# Преобразование строки в объект datetime
date_obj = datetime.strptime(date_str, '%b %d, %Y - %H:%M:%S')

# Распечатать полное название месяца
month_name = date_obj.strftime('%B')
print(month_name)

# Распечатать дату в нужном формате
new_date_format = date_obj.strftime('%d.%m.%Y, %H:%M')
print(new_date_format)
