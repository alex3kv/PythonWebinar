# Необходимо создать (не программно) текстовый файл, где каждая строка
# описывает учебный предмет и наличие лекционных, практических и лабораторных
# занятий по этому предмету и их количество.  Важно, чтобы для каждого предмета
# не обязательно были все типы занятий.  Сформировать словарь, содержащий
# название предмета и общее количество занятий по нему.  Вывести словарь на
# экран.

# Примеры строк файла:
# Информатика: 100(л) 50(пр) 20(лаб).
# Физика: 30(л) — 10(лаб)
# Физкультура: — 30(пр) —
#
# Пример словаря:
# {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}
#
FILE_NAME = "Task6UserFile.txt"


def file_readlines(file):
    try:
        with open(file, encoding="utf-8") as f_obj:
            return f_obj.readlines()
    except IOError:
        print("Произошла ошибка ввода-вывода!")

    return None


def get_info_sum(row):
    row = row.replace("-", "")
    row = row.replace("(л)", "")
    row = row.replace("(пр)", "")
    row = row.replace("(лаб)", "")
    return sum(map(int, row.split()))


def get_info(row):
    arr = row.split(":")
    
    key = arr[0]
    val = get_info_sum(arr[1])

    return key, val


result = {}

items = file_readlines(FILE_NAME)
for item in items:
    key, val = get_info(item)
    result[key] = val

print(result)
