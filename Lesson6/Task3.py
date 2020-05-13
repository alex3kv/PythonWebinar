# 3.  Реализовать функцию my_func(), которая принимает три позиционных
# аргумента, и возвращает сумму наибольших двух аргументов.
#
#
def my_func(a, b, c):
    items = sorted([a, b, c], reverse = True)
    return items[0] + items[1]


print(my_func(10, 6, 1))
    