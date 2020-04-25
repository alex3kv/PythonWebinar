# 5.  Программа запрашивает у пользователя строку чисел, разделенных пробелом.
# При нажатии Enter должна выводиться сумма чисел.  Пользователь может
# продолжить ввод чисел, разделенных пробелом и снова нажать Enter.  Сумма
# вновь введенных чисел будет добавляться к уже подсчитанной сумме.  Но если
# вместо числа вводится специальный символ, выполнение программы завершается.
# Если специальный символ введен после нескольких чисел, то вначале нужно
# добавить сумму этих чисел к полученной ранее сумме и после этого завершить
# программу.
#
#
EXIT_SYMBOL = "~"


def sum_by_string_list(items):

    is_exit_symbol = False

    sum = 0

    for item in items:
    
        if item == EXIT_SYMBOL:
            is_exit_symbol = True
            break
    
        sum += int(item)

    return sum, is_exit_symbol


print(f"Введите строку чисел разделенных пробелом (для завершения подсчета введите символ {EXIT_SYMBOL})")

sum = 0
while True:
    #input_string = input("Введите строку: ")
    input_string = "10 20 30 40 5 1 ~"
    items = input_string.split()    
    
    sum_it, is_exit = sum_by_string_list(items)
    sum += sum_it
        
    print(f"Сумма введенных чисел: {sum}")

    if is_exit:
        break
