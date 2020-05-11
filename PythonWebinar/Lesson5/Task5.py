# Создать (программно) текстовый файл, записать в него программно набор чисел,
# разделенных пробелами.  Программа должна подсчитывать сумму чисел в файле и
# выводить ее на экран.
#
FILE_NAME = "Task5UserFile.txt"


def file_create(file):
    with open(file, "w", encoding="utf-8"): pass

def file_read(file):
    try:
        with open(file) as f_obj:
            return f_obj.read()
    except IOError:
        print("Произошла ошибка ввода-вывода!")

    return None

def file_write_text(file, user_string):
    try:
        with open(file, "a", encoding="utf-8") as f_obj:
            f_obj.write(user_string)
    except IOError:
        print("Произошла ошибка ввода-вывода!")


file_create(FILE_NAME)
file_write_text(FILE_NAME, "12 54 63 2 58 45 63 58 95")

data = file_read(FILE_NAME)
items = data.split()
sum_numbers = sum(map(int,items))
print(f"Сумма чисел в файле - {sum_numbers}")
