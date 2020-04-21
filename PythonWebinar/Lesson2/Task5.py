# 5.  Реализовать структуру «Рейтинг», представляющую собой не возрастающий
# набор натуральных чисел.  У пользователя необходимо запрашивать новый элемент
# рейтинга.  Если в рейтинге существуют элементы с одинаковыми значениями, то
# новый элемент с тем же значением должен разместиться после них.
#
# Подсказка.  Например, набор натуральных чисел: 7, 5, 3, 3, 2.
# Пользователь ввел число 3.  Результат: 7, 5, 3, 3, 3, 2.
# Пользователь ввел число 8.  Результат: 8, 7, 5, 3, 3, 2.
# Пользователь ввел число 1.  Результат: 7, 5, 3, 3, 2, 1.
# Набор натуральных чисел можно задать непосредственно в коде, например,
# my_list = [7, 5, 3, 3, 2].
#
rating = [7, 5, 3, 3, 2]

while True:    
    value_input = input("Введите новый элемент рейтинга: ")
    if value_input == "":
        break

    value = int(value_input)
    print()

    insert_index = None

    for i, item in enumerate(rating):        

        if value > item:
            insert_index = i
            break

        if value == item:
            continue        

    if insert_index == None:
        rating.append(value)
    else:
        rating.insert(insert_index, value)

    print(rating)
