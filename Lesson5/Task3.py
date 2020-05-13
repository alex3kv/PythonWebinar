# Создать текстовый файл (не программно), построчно записать фамилии
# сотрудников и величину их окладов (не менее 10 строк).  Определить, кто из
# сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
# Выполнить подсчет средней величины дохода сотрудников.
#
# Пример файла:
# Иванов 23543.12
# Петров 13749.32
#
FILE_NAME = "Task3UserFile.txt"


def file_readlines(file):
    try:
        with open(file, encoding="utf-8") as f_obj:
            return f_obj.readlines()
    except IOError:
        print("Произошла ошибка ввода-вывода!")

    return None


low_paid_workers = []
salary_sum = 0

items = file_readlines(FILE_NAME)
for item in items:
    arr = item.split()
    worker_name = arr[0]
    worker_salary = float(arr[1])

    if(worker_salary < 20000):
        low_paid_workers.append(worker_name)

    salary_sum += worker_salary

average_salary = salary_sum / len(items)

print(f"Сотрудники с окладом менее 20 тыс.: {', '.join(low_paid_workers)}")
print(f"Средний оклад сотрудника: {average_salary:.2f}")
