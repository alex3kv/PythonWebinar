# 1.  Реализовать функцию, принимающую два числа (позиционные аргументы) и
# выполняющую их деление.  Числа запрашивать у пользователя, предусмотреть
# обработку ситуации деления на ноль.
#
#
def division(dividend, divider):
    
    if divider == 0:
        return None

    return dividend / divider

d_1_1, d_1_2 = "5", "3"
print(division(int(d_1_1), int(d_1_2)))

d_2_1, d_2_2 = "3", "5"
print(division(int(d_2_1), int(d_2_2)))

d_3_1, d_3_2 = "0", "1"
print(division(int(d_3_1), int(d_3_2)))

d_4_1, d_4_2 = "1", "0"
print(division(int(d_4_1), int(d_4_2)))
