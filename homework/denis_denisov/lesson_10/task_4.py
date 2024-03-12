"""
Задание 4

Дан такой кусок прайс-листа:

(Копируйте эту переменную (константу) в код прямо как есть)

PRICE_LIST = '''тетрадь 50р
книга 200р
ручка 100р
карандаш 70р
альбом 120р
пенал 300р
рюкзак 500р'''
При помощи генераторов превратите этот текст в словарь такого вида:

{'тетрадь': 50, 'книга': 200, 'ручка': 100, 'карандаш': 70, 'альбом': 120, 'пенал': 300, 'рюкзак': 500}
Обратите внимание, что цены в словаре имеют тип int (они не в кавычках)

"""

price_list = '''тетрадь 50р
книга 200р
ручка 100р
карандаш 70р
альбом 120р
пенал 300р
рюкзак 500р'''

price_dict = {item.split()[0]: int(item.split()[1][:-1]) for item in price_list.splitlines()}
print(price_dict)
