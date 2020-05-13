# 4.  Программа принимает действительное положительное число x и целое
# отрицательное число y.  Необходимо выполнить возведение числа x в степень y.
# Задание необходимо реализовать в виде функции my_func(x, y).  При решении
# задания необходимо обойтись без встроенной функции возведения числа в
# степень.
#
# Подсказка: попробуйте решить задачу двумя способами.  Первый —
# возведение в степень с помощью оператора **.  Второй — более сложная
# реализация без оператора **, предусматривающая использование цикла.
#
#
def my_func(x, y):
    return x ** y


def my_func_alternative(x, y):

    power = x
    for i in range(-y - 1):
        power *= x

    return 1 / power


print(my_func(10, -2), my_func_alternative(10, -2))

print(my_func(16, -3), my_func_alternative(16, -3))