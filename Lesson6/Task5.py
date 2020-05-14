# Реализовать класс Stationery (канцелярская принадлежность).  Определить в нем
# атрибут title (название) и метод draw (отрисовка).  Метод выводит сообщение
# “Запуск отрисовки.” Создать три дочерних класса Pen (ручка), Pencil
# (карандаш), Handle (маркер).  В каждом из классов реализовать переопределение
# метода draw.  Для каждого из классов метод должен выводить уникальное
# сообщение.  Создать экземпляры классов и проверить, что выведет описанный
# метод для каждого экземпляра.
#
class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print(f"Запуск отрисовки. При помощи {self.title}")

class Pen(Stationery):
    def draw(self):
        print(f"Запуск отрисовки ручкой. При помощи {self.title}")

class Pencil(Stationery):
    def draw(self):
        print(f"Запуск отрисовки карандашем. При помощи {self.title}")

class Handle(Stationery):
    def draw(self):
        print(f"Запуск отрисовки маркером. При помощи {self.title}")

stationery = Stationery("моя принадлежность")
stationery.draw()

pen = Pen("моя ручка")
pen.draw()

pencil = Pencil("мой карандаш")
pencil.draw()

handle = Handle("мой маркер")
handle.draw()