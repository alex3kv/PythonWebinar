# 6.  Реализовать функцию int_func(), принимающую слово из маленьких латинских
# букв и возвращающую его же, но с прописной первой буквой.  Например,
# print(int_func(‘text’)) -> Text.
#
# Продолжить работу над заданием.  В программу должна попадать строка из слов,
# разделенных пробелом.  Каждое слово состоит из латинских букв в нижнем
# регистре.  Сделать вывод исходной строки, но каждое слово должно начинаться с
# заглавной буквы.  Необходимо использовать написанную ранее функцию
# int_func().
#
#
def to_upper(symbol):
    code = ord(symbol) - 32
    return chr(code)

def int_func(word):    
    first_letter = to_upper(word[0])
    return first_letter + word[1:]

def string_to_upper(value):
    items = value.split()

    result = int_func(items[0])

    for item in items[1:]:
        result += " " + int_func(item)

    return result


print(int_func("text"))

input_string = "слова в нижнем регистре разделенные пробелом"
print(string_to_upper(input_string))
