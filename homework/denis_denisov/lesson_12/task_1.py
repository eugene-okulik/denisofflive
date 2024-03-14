"""
Задание

Создать классы цветов: общий класс для всех цветов и классы для нескольких видов.
Создать экземпляры (объекты) цветов разных видов.
Собрать букет (букет - еще один класс) с определением его стоимости.
В букете цветы пусть хранятся в списке. Это будет список объектов.

Для букета создать метод, который определяет время его увядания по среднему времени жизни всех цветов в букете.

Позволить сортировку цветов в букете на основе различных параметров (свежесть/цвет/длина стебля/стоимость)
(это тоже методы)

Реализовать поиск цветов в букете по каким-нибудь параметрам (например, по среднему времени жизни) (и это тоже метод).

"""

class Flower:
    def __init__(self, color, freshness, stem_length, cost):
        self.color = color
        self.freshness = freshness
        self.stem_length = stem_length
        self.cost = cost


class Rose(Flower):
    def __init__(self, color, freshness, stem_length, cost):
        super().__init__("Роза: " + color, freshness, stem_length, cost)


class Lily(Flower):
    def __init__(self, color, freshness, stem_length, cost):
        super().__init__("Лилия: " + color, freshness, stem_length, cost)


class Tulip(Flower):
    def __init__(self, color, freshness, stem_length, cost):
        super().__init__("Тюльпан: " + color, freshness, stem_length, cost)


class Bouquet:
    def __init__(self):
        self.flowers = []

    def add_flower(self, flower):
        self.flowers.append(flower)

    def calculate_cost(self):
        total_costs = 0
        for flower in self.flowers:
            total_costs += flower.cost
        return total_costs

    def calculate_average_freshness(self):
        total_freshness = 0
        for flower in self.flowers:
            total_freshness += flower.freshness
        return total_freshness / len(self.flowers)

    def sort_flowers(self, key):
        self.flowers.sort(key=key)

    def search_flowers(self, key, value):
        return [flower for flower in self.flowers if key(flower) == value]


# Пример использования

# Создание объектов цветов разных видов
rose1 = Rose("Красная", 8, 30, 10)
rose2 = Rose("Белая", 9, 35, 12)
lily1 = Lily("Жёлтая", 7, 25, 8)
lily2 = Lily("Розовая", 6, 27, 9)
tulip1 = Tulip("Пурпурный", 9, 20, 7)
tulip2 = Tulip("Оранжевый", 8, 22, 6)

# Создание букета и добавление цветов в список
bouquet = Bouquet()
bouquet.add_flower(rose1)
bouquet.add_flower(rose2)
bouquet.add_flower(lily1)
bouquet.add_flower(lily2)
bouquet.add_flower(tulip1)
bouquet.add_flower(tulip2)

# Подсчет стоимости букета
total_cost = bouquet.calculate_cost()
print("Общая стоимость букета:", total_cost)

# Подсчет средней свежести букета
average_freshness = bouquet.calculate_average_freshness()
print("Средняя свежесть букета:", average_freshness)

# Сортировка цветов в букете по свежести
bouquet.sort_flowers(key=lambda flower: flower.freshness)
print("Сортированный букет по свежести:", [flower.color for flower in bouquet.flowers])

# Поиск цветов в букете по свежести
search_result = bouquet.search_flowers(key=lambda flower: flower.freshness, value=8)
print("Найдены цветы, свежесть которых равна 8:", [flower.color for flower in search_result])
