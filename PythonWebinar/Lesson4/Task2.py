# 2.  Представлен список чисел.  Необходимо вывести элементы исходного списка,
# значения которых больше предыдущего элемента.
#
# Подсказка: элементы, удовлетворяющие условию, оформить в виде списка.  Для
# формирования списка использовать генератор
#
#
def build_user_list(items):
    for i in range(1, len(items)):
        if items[i] > items[i - 1]:
            yield items[i]


input_list = [1, 4, 7, 2, 4, 5, 9, 3, 0, 10]
#result_list = [input_list[i] for i in range(1, len(input_list)) if input_list[i] > input_list[i - 1]]
result_list = list(build_user_list(input_list))

print(result_list)
