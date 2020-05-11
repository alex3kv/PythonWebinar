# Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую
# построчно данные.  При этом английские числительные должны заменяться на
# русские.  Новый блок строк должен записываться в новый текстовый файл.
#
FILE_NAME = "Task4UserFile.txt"
FILE_NAME_RESULT = "Task4UserFileResult.txt"
VOCABULARY = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре", "Five": "Пять"}


def file_create(file):
    with open(file, "w", encoding="utf-8"): pass


def file_readlines(file):
    try:
        with open(file) as f_obj:
            return f_obj.readlines()
    except IOError:
        print("Произошла ошибка ввода-вывода!")

    return None


def file_write_text(file, user_string):
    try:
        with open(file, "a", encoding="utf-8") as f_obj:
            f_obj.write(user_string)
    except IOError:
        print("Произошла ошибка ввода-вывода!")


def translate_numeral(row):
    arr = row.split()
    numeral = arr[0]
    return row.replace(numeral, VOCABULARY[numeral])


file_create(FILE_NAME_RESULT)

items = file_readlines(FILE_NAME)
for item in items:
    row = translate_numeral(item)
    file_write_text(FILE_NAME_RESULT, row)
