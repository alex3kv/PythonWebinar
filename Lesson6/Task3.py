# Реализовать базовый класс Worker (работник), в котором определить атрибуты:
# name, surname, position (должность), income (доход).  Последний атрибут
# должен быть защищенным и ссылаться на словарь, содержащий элементы: оклад и
# премия, например, {"wage": wage, "bonus": bonus}.  Создать класс Position
# (должность) на базе класса Worker.  В классе Position реализовать методы
# получения полного имени сотрудника (get_full_name) и дохода с учетом премии
# (get_total_income).  Проверить работу примера на реальных данных (создать
# экземпляры класса Position, передать данные, проверить значения атрибутов,
# вызвать методы экземпляров).
#
class Worker:
    def __init__(self, name, surname, position, wage, bonus=0):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}

class Position(Worker):
    def get_full_name(self):
        return f"{self.name} {self.surname}"

    def get_total_income(self):
        return self._income.get("wage", 0) + self._income.get("bonus", 0)


position1 = Position("Иван", "Иванов", "специалист", 100)
full_name1 = position1.get_full_name()
total_income1 = position1.get_total_income()
print(position1.name, position1.surname, position1.position, full_name1, total_income1)

position2 = Position("Василий", "Смирнов", "главный специалист", 100, 30)
full_name2 = position2.get_full_name()
total_income2 = position2.get_total_income()
print(position2.name, position2.surname, position2.position, full_name2, total_income2)
