"""
Задание

Нужно прочитать файл, который лежит в репозитории в моей папке. Здесь: homework/eugene_okulik/hw_13/data.txt

Файл не копируйте и никуда не переносите. Напишите программу, которая читает этот файл,
находит в нём даты и делает с этими датами то, что после них написано. Опирайтесь на то,
что структура каждой строки одинакова: сначала идет номер, потом дата, потом дефис и после него текст.
У вас должен получиться код, который находит даты и для даты под номером один в коде должно быть реализовано,
то действие, которое написано в файле после этой даты. Ну и так далее для каждой даты.

"""
import os
import datetime

base_path = os.path.dirname(__file__)
homework_path = os.path.dirname(os.path.dirname(base_path))
hw_13_path = os.path.join(homework_path, 'eugene_okulik', 'hw_13', 'data.txt')


def read_file(file_path):
    # Чтение файла и обработка каждой строки
    with open(file_path) as hw_13:
        for line in hw_13.readlines():
            yield line


for data_line in read_file(hw_13_path):
    try:
        # Разделяем строку на номер, дату и текст
        date_time = data_line.split(' - ')
        line_number, full_date_time = date_time[0].split('. ')
        # Преобразуем дату из строки в объект datetime
        date = datetime.datetime.strptime(full_date_time, "%Y-%m-%d %H:%M:%S.%f")
        if line_number == '1':
            # Добавляем 7 дней к дате и выводим ее в нужном формате
            print(date + datetime.timedelta(days=7))
        elif line_number == '2':
            # Выводим день недели для заданной даты
            print(date.strftime('%A'))
        elif line_number == '3':
            # Рассчитываем количество дней между заданной датой и текущей датой
            print((datetime.datetime.now() - date).days)
    except ValueError:
        print('Задание выполнено')
