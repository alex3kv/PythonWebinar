# Реализовать класс «Дата», функция-конструктор которого должна принимать дату
# в виде строки формата «день-месяц-год».  В рамках класса реализовать два
# метода.  Первый, с декоратором @classmethod, должен извлекать число, месяц,
# год и преобразовывать их тип к типу «Число».  Второй, с декоратором
# @staticmethod, должен проводить валидацию числа, месяца и года (например,
# месяц — от 1 до 12).  Проверить работу полученной структуры на реальных
# данных.
class Date:
    def __init__(self, day, month, year):
        self._day = day
        self._month = month
        self._year = year

    @classmethod
    def from_string(cls, string_date):
        arr = string_date.split("-")
        day = int(arr[0])
        month = int(arr[1])
        year = int(arr[2])
        Date.validate(day, month, year)
        return cls(day, month, year)

    @staticmethod
    def validate(day, month, year):
        if day <= 0 or day > 31:
            raise ValueError("Значение дня вышло за пределы диапазона [1:31]")
        if month <= 0 or month > 12:
            raise ValueError("Значение месяца вышло за пределы диапазона [1:12]")
        if year <= 2000 or year > 2100:
            raise ValueError("Значение года вышло за пределы текущего века [2000:2100]")

    def __str__(self):
        return f"{self._day:02}.{self._month:02}.{self._year}"


date1 = Date.from_string("20-05-2020")
print(date1)

date2 = Date.from_string("01-05-2020")
print(date2)