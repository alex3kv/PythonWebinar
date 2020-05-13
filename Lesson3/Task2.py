# 2.  Реализовать функцию, принимающую несколько параметров, описывающих данные
# пользователя: имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы.  Реализовать
# вывод данных о пользователе одной строкой.
#
#
def print_user_info(first_name, last_name, year_of_birth, city, email, phone):
    print(f"{first_name} {last_name} {year_of_birth} года рождения, проживает в г. {city}, email: {email}, тел. {phone}")


print_user_info(first_name="Иван", last_name="Иванов", year_of_birth=1990, city="Москва", email="email@amail.ru", phone="+7 123 456 7890")
