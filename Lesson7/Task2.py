# Реализовать проект расчета суммарного расхода ткани на производство одежды.
# Основная сущность (класс) этого проекта — одежда, которая может иметь
# определенное название.  К типам одежды в этом проекте относятся пальто и
# костюм.  У этих типов одежды существуют параметры: размер (для пальто) и рост
# (для костюма).  Это могут быть обычные числа: V и H, соответственно.
#
# Для определения расхода ткани по каждому типу одежды использовать формулы:
# для пальто (V/6.5 + 0.5), для костюма (2*H + 0.3).  Проверить работу этих
# методов на реальных данных.
#
# Реализовать общий подсчет расхода ткани.  Проверить на практике полученные на
# этом уроке знания: реализовать абстрактные классы для основных классов
# проекта, проверить на практике работу декоратора @property.
#
from abc import ABC, abstractmethod


class Apparel(ABC):
    def __init__(self, name):
        self._name = name

    @abstractmethod
    def calculate_flow():
        pass


class Coat(Apparel):
    def __init__(self, name, size):
        super().__init__(name)
        self._size = size

    def calculate_flow(self):
        return self._size / 6.5 + 0.5


class Suit(Apparel):
    def __init__(self, name, height):
        super().__init__(name)
        self._height = height

    def calculate_flow(self):
        return 2 * self._height + 0.3


class ApparelCalculate:
    def __init__(self):
        self._apparels = []

    def add(self, apparel):
        if not isinstance(apparel, Apparel):
            print("Ошибка")
            return
        self._apparels.append(apparel)

    def __len__(self):
        return len(self._apparels)

    @property
    def all_flow(self):
        result = 0
        for apparel in self._apparels:
            result += apparel.calculate_flow()
        return result


coat_1 = Coat("Пальто кашемировое", 50)
print(coat_1.calculate_flow())

coat_2 = Coat("Пальто шерстяное", 60)
print(coat_2.calculate_flow())

suit_1 = Coat("Костюм кашемировый", 170)
print(suit_1.calculate_flow())

suit_2 = Coat("Костюм шерстяной", 180)
print(suit_2.calculate_flow())
print()

apparelCalculate = ApparelCalculate()
apparelCalculate.add(coat_1)
apparelCalculate.add(coat_2)
apparelCalculate.add(suit_1)
apparelCalculate.add(suit_2)

print(f"Общий расход ткани - {apparelCalculate.all_flow:.2f}")
