# Создать вручную и заполнить несколькими строками текстовый файл, в котором
# каждая строка должна содержать данные о фирме: название, форма собственности,
# выручка, издержки.
#
# Пример строки файла: firm_1 ООО 10000 5000.
#
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а
# также среднюю прибыль.  Если фирма получила убытки, в расчет средней прибыли
# ее не включать.
#
# Далее реализовать список.  Он должен содержать словарь с фирмами и их
# прибылями, а также словарь со средней прибылью.  Если фирма получила убытки,
# также добавить ее в словарь (со значением убытков).
#
# Пример списка:
# [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
#
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
#
# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
#
# Подсказка: использовать менеджер контекста.
#
import json

FILE_NAME = "Task7UserFile.txt"
FILE_NAME_JSON = "Task7UserFile.json"


def file_write_json(file, data):
    try:
        with open(file, "w", encoding="utf-8") as f_obj:
            json.dump(data, f_obj)
    except IOError:
        print("Произошла ошибка ввода-вывода!")


def get_firm_info(row):
    arr = row.split()

    key = arr[0]
    val = int(arr[2]) - int(arr[3])

    return key, val


firms = {}
average_profit_sum = 0
average_profit_count = 0
try:
    with open(FILE_NAME, encoding="utf-8") as f_obj:
        for line in f_obj:
            key, val = get_firm_info(line)

            if(val > 0):
                average_profit_sum += val
                average_profit_count +=1

            firms[key] = val
except IOError:
    print("Произошла ошибка ввода-вывода!")

average_profit = average_profit_sum / average_profit_count
result = [firms, {"average_profit": average_profit}]

file_write_json(FILE_NAME_JSON, result)