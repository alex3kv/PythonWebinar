# 2.  Для списка реализовать обмен значений соседних элементов, т.е.
# Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.  При
# нечетном количестве элементов последний сохранить на своем месте.  Для
# заполнения списка элементов необходимо использовать функцию input().
#
items = []

#items_count_input = input("Введите количество элементов списка: ")
#items_count_input = "5"
#items_count = int(items_count_input)

#i = items_count
#while i > 0:
#    i-=1
#    item = input("Введите элемент списка: ")
#    items.append(item)

#string_input = input("Введите элементы списка разделенные символом '|':");
string_input = "раз|два|три|четыре|пять|шесть|семь"
items = string_input.split("|")

for i in range(0, len(items) - 1, 2):
    items[i], items[i + 1] = items[i + 1], items[i]

print(items)