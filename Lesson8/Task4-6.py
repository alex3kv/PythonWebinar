# Начните работу над проектом «Склад оргтехники».  Создайте класс, описывающий
# склад.  А также класс «Оргтехника», который будет базовым для
# классов-наследников.  Эти классы — конкретные типы оргтехники (принтер,
# сканер, ксерокс).  В базовом классе определить параметры, общие для
# приведенных типов.  В классах-наследниках реализовать параметры, уникальные
# для каждого типа оргтехники.
#
# Продолжить работу над первым заданием.  Разработать методы, отвечающие за
# приём оргтехники на склад и передачу в определенное подразделение компании.
# Для хранения данных о наименовании и количестве единиц оргтехники, а также
# других данных, можно использовать любую подходящую структуру, например
# словарь.
#
# Продолжить работу над вторым заданием.  Реализуйте механизм валидации
# вводимых пользователем данных.  Например, для указания количества принтеров,
# отправленных на склад, нельзя использовать строковый тип данных.
#
# Подсказка: постарайтесь по возможности реализовать в проекте «Склад
# оргтехники» максимум возможностей, изученных на уроках по ООП.
from abc import ABC, abstractmethod


class Warehouse:
    def __init__(self):
        self._items = []
        self._branch_items = {}

    def take(self, item):
        if not isinstance(item, OfficeEquipment):
            raise TypeError("Объект не является типом OfficeEquipment")
        if not item._properties["count"] is not int:
            raise ValueError("Значение свойства количество не явялется числом")
        self._items.append(item)

    def transfer(self, item, branch):
        if not isinstance(item, OfficeEquipment):
            raise TypeError("Объект не является типом OfficeEquipment")
        if not item._properties["count"] is not int:
            raise ValueError("Значение свойства количество не явялется числом")
        self._branch_items[branch] = item

    def __len__(self):
        return len(self._items)

    @property
    def service_cost(self):
        result = 0
        for item in self._branch_items.values():
            result += item.calculate_service_cost()
        return result
        


class OfficeEquipment(ABC):
    def __init__(self, name, brand, count):
        self._name = name
        self._brand = brand
        self._properties = {"count": count}

    @abstractmethod
    def calculate_service_cost(self):
        pass

    def __str__(self):
        return f"{self._name} {self._brand} {self._properties}"

    def __len__(self):
        return self._properties["count"]


class Printer(OfficeEquipment):
    price = 10

    def __init__(self, name, brand, count, max_page):
        super().__init__(name, brand, count)
        self._properties["max_page"] = max_page

    def calculate_service_cost(self):
        return self.price * self._properties["max_page"] * self._properties["count"]



class Scanner(OfficeEquipment):
    price = 5

    def __init__(self, name, brand, count, resolution):
        super().__init__(name, brand, count)
        self._properties["resolution"] = resolution

    def calculate_service_cost(self):
        return self.price * self._properties["resolution"] * self._properties["count"]


class Copier(OfficeEquipment):
    price = 8

    def __init__(self, name, brand, count, format):
        super().__init__(name, brand, count)
        self._properties["format"] = format

    def calculate_service_cost(self):
        return self.price * self._properties["count"]


printers1 = Printer("L355", "Epson", 20, 10)
copiers1 = Copier("123", "Xerox", 10, "A3")

printers2 = Printer("L355", "Epson", 5, 10)
copiers2 = Copier("123", "Xerox", 3, "A3")

mainWarehouse = Warehouse()
try:    
    mainWarehouse.take(printers1)
    mainWarehouse.take(copiers1)

    mainWarehouse.transfer(printers2, "Main")
    mainWarehouse.transfer(copiers2, "Slave")
except Exception as ex:
    print(f"Возникла непредвиденная ошибка: {ex}")

print("Техника на складе:")
for el in mainWarehouse._items:
    print(el)

print()
print("Техника в подразделениях:")
for key, value in mainWarehouse._branch_items.items():
    print(key, value)

print()
print(f"Планируемые затраты на обслуживанеи техники в подразделениях: {mainWarehouse.service_cost}")