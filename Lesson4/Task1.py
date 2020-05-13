# 1.  Реализовать скрипт, в котором должна быть предусмотрена функция расчета
# заработной платы сотрудника.  В расчете необходимо использовать формулу:
# (выработка в часах * ставка в час) + премия.  Для выполнения расчета для
# конкретных значений необходимо запускать скрипт с параметрами.
#
# python Task1.py 160 10 50
from sys import argv

#input_args = argv[1:]
input_args = ["160", "10", "50"]

def calculate_employee_salary(hours, rate, bonus):
    return hours * rate + bonus


hours = float(input_args[0])
rate = int(input_args[1])
bonus = int(input_args[2])

salary = calculate_employee_salary(hours, rate, bonus)
print(salary)
