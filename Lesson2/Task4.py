# 4.  Пользователь вводит строку из нескольких слов, разделённых пробелами.
# Вывести каждое слово с новой строки.  Строки необходимо пронумеровать.  Если
# в слово длинное, выводить только первые 10 букв в слове.
#
#string_input = input("Введите строку из нескольких слов, разделённых пробелами:")
string_input = "раз два три четыре пять шесть семь 1234567890123456789"
words = string_input.split()

for i, word in enumerate(words):
    print(f"{i}. {word[:10]}")
