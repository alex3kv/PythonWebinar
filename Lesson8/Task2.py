# Создайте собственный класс-исключение, обрабатывающий ситуацию деления на
# нуль.  Проверьте его работу на данных, вводимых пользователем.  При вводе
# пользователем нуля в качестве делителя программа должна корректно обработать
# эту ситуацию и не завершиться с ошибкой.
class ZeroDivisionException(Exception):
    pass

inp_data = input("Введите делитель: ")

try:
    inp_data = int(inp_data)
    if inp_data == 0:
        raise ZeroDivisionException("Делить на нуль нельзя!")
except ValueError:
    print("Вы ввели не число")
except ZeroDivisionException as err:
    print(err)
else:
    print(f"Все хорошо. Ваше значение деления 100 на {inp_data} = {100/inp_data}")
