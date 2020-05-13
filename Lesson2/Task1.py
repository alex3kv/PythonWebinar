# 1.  Создать список и заполнить его элементами различных типов данных.
# Реализовать скрипт проверки типа данных каждого элемента.  Использовать
# функцию type() для проверки типа.  Элементы списка можно не запрашивать у
# пользователя, а указать явно, в программе.
#
list_all_types = []

#int_1_input = input("Введите любе значение типа int: ")
int_1_input = "5"
int_1 = int(int_1_input)
list_all_types.append(int_1)

#float_1_input = input("Введите любе значение типа float: ")
float_1_input = "1.5"
float_1 = float(float_1_input)
list_all_types.append(float_1)

complex_1 = complex(5, 6)
list_all_types.append(complex_1)

#str_1 = input("Введите любе значение типа str: ")
str_1 = "строка 1"
list_all_types.append(str_1)

list_1 = ["список 1", 1]
list_all_types.append(list_1)

tuple_1 = ("кортеж 1", 1)
list_all_types.append(tuple_1)

set_1 = {"множество 1", 1}
list_all_types.append(set_1)

frozenset_1 = frozenset({"неизменяемое множество 1", 1})
list_all_types.append(frozenset_1)

dict_1 = {"ключ 1": "значение 1", 1: 2}
list_all_types.append(dict_1)

bool_1 = True
list_all_types.append(bool_1)

bytes_1 = b'bytes'
list_all_types.append(bytes_1)

bytearray_1 = bytearray (b'bytearray')
list_all_types.append(bytearray_1)

none_1 = None
list_all_types.append(none_1)

#print(list_all_types)
for item in list_all_types:
    print(f"{item} {type(item)}")
