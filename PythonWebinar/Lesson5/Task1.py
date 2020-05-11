# Создать программно файл в текстовом формате, записать в него построчно
# данные, вводимые пользователем.  Об окончании ввода данных свидетельствует
# пустая строка.
#
FILE_NAME = "Task1UserText.txt"


def file_create(file):
    with open(file, "w", encoding="utf-8"): pass

def file_write_text(file, user_string):
    try:
        with open(file, "a", encoding="utf-8") as f_obj:
            f_obj.write(f"{user_string}\n")
    except IOError:
        print("Произошла ошибка ввода-вывода!")


file_create(FILE_NAME)

while True:
    user_string = input("Введите строку: ")
    
    if user_string == "":
        break

    file_write_text(FILE_NAME, user_string)
