# 6.  *Реализовать структуру данных «Товары».  Она должна представлять собой
# список кортежей.  Каждый кортеж хранит информацию об отдельном товаре.  В
# кортеже должно быть два элемента — номер товара и словарь с параметрами
# (характеристиками товара: название, цена, количество, единица измерения).
# Структуру нужно сформировать программно, т.е.  запрашивать все данные у
# пользователя.
#
# Пример готовой структуры:
# [
# (1, {“название”: “компьютер”, “цена”: 20000, “количество”: 5, “eд”: “шт.”}),
# (2, {“название”: “принтер”, “цена”: 6000, “количество”: 2, “eд”: “шт.”}),
# (3, {“название”: “сканер”, “цена”: 2000, “количество”: 7, “eд”: “шт.”})
# ]
#
# Необходимо собрать аналитику о товарах.  Реализовать словарь, в котором
# каждый ключ — характеристика товара, например название, а значение — список
# значений-характеристик, например список названий товаров.
#
# Пример:
# {
# “название”: [“компьютер”, “принтер”, “сканер”],
# “цена”: [20000, 6000, 2000],
# “количество”: [5, 2, 7],
# “ед”: [“шт.”]
# }
#
goods = []
template_characteristics = {"название": "", "цена": 0, "количество": 0, "ед": ""}

items_count_input = input("Введите количество вводимых товаров: ")
#items_count_input = "3"
items_count = int(items_count_input)

i = items_count
while i > 0:
    i-=1
    
    print()
    good_number_input = input("Введите номер товара: ")
    good_number = int(good_number_input)    

    characteristics = template_characteristics.copy()

    for key in characteristics.keys():        
        value_input = input(f"Введите значение характеристики {key}: ")
        if(type(characteristics[key]) is int):
            characteristics[key] = int(value_input)
        else:
            characteristics[key] = value_input

    good = (good_number, characteristics)
    goods.append(good)

print()
print("Введенные торвары:")
print(goods)

goods = [
(1, {"название": "компьютер", "цена": 20000, "количество": 5, "eд": "шт."}),
(2, {"название": "принтер", "цена": 6000, "количество": 2, "eд": "шт."}),
(3, {"название": "сканер", "цена": 2000, "количество": 7, "eд": "шт."})
]

analytics = dict()

for good in goods:
    characteristics = good[1]
    for key, value in characteristics.items():
        
        if analytics.setdefault(key, None) == None:
            analytics[key] = list()

        if value not in analytics[key]:
            analytics[key].append(value)

print()
print("Анализ:")
print(analytics)
