# Реализовать генератор с помощью функции с ключевым словом yield, создающим
# очередное значение.  При вызове функции должен создаваться объект-генератор.
# Функция должна вызываться следующим образом: for el in fact(n).  Функция
# отвечает за получение факториала числа, а в цикле необходимо выводить только
# первые n чисел, начиная с 1!  и до n!.
#
# Подсказка: факториал числа n — произведение чисел от 1 до n.  Например,
# факториал четырёх 4!  = 1 * 2 * 3 * 4 = 24.
#
# по дз 7 уточнение: "Реализовать генератор с помощью функции с ключевым словом
# yield" - задача.  " в цикле необходимо выводить только первые n чисел,
# начиная с 1!  и до n!" - все четко.  пусть n=4
#
def fact(n):
    result = 1
    for el in range(1, n + 1):
        result *= el
        yield result       


n = 4
for el in fact(n):
    print(el)
