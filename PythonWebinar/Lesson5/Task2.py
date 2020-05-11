# Создать текстовый файл (не программно), сохранить в нем несколько строк,
# выполнить подсчет количества строк, количества слов в каждой строке.
#
FILE_NAME = "Task2UserText.txt"


def file_readlines(file):
    try:
        with open(file) as f_obj:
            return f_obj.readlines()
    except IOError:
        print("Произошла ошибка ввода-вывода!")

    return None


items = file_readlines(FILE_NAME)
line_count = len(items)
print(f"В файле определно следующее количество строк - {line_count}")

print()
for i, item in enumerate(items):
    word_count = len(item.split())
    print(f"В строке {i+1} определно следующее количество слов - {word_count}")
