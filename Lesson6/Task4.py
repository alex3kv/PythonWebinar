# Реализуйте базовый класс Car.  У данного класса должны быть следующие
# атрибуты: speed, color, name, is_police (булево).  А также методы: go, stop,
# turn(direction), которые должны сообщать, что машина поехала, остановилась,
# повернула (куда).  Опишите несколько дочерних классов: TownCar, SportCar,
# WorkCar, PoliceCar.  Добавьте в базовый класс метод show_speed, который
# должен показывать текущую скорость автомобиля.  Для классов TownCar и WorkCar
# переопределите метод show_speed.  При значении скорости свыше 60 (TownCar) и
# 40 (WorkCar) должно выводиться сообщение о превышении скорости.
#
# Создайте экземпляры классов, передайте значения атрибутов.  Выполните доступ
# к атрибутам, выведите результат.  Выполните вызов методов и также покажите
# результат.
#
class Car:
    def __init__(self, speed, color, name):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = False

    def go(self):
        message = "Полицейский автомобиль" if self.is_police else "Автомобиль"
        print(f"{message} {self.name}, {self.color} цвета - начал движение")

    def stop(self):
        message = "Полицейский автомобиль" if self.is_police else "Автомобиль"
        print(f"{message} {self.name}, {self.color} цвета - остановился")

    def turn(self, direction):
        message = "Полицейский автомобиль" if self.is_police else "Автомобиль"
        print(f"{message} {self.name}, {self.color} цвета - повернул {direction}")

    def show_speed(self):
        message = "Полицейский автомобиль" if self.is_police else "Автомобиль"
        print(f"{message} {self.name}, {self.color} цвета - движется со скоростью {self.speed}")

class TownCar(Car):
    def show_speed(self):
        message = f"Автомобиль {self.name}, {self.color} цвета -"
        if self.speed > 60:
            print(f"{message} движется c превышением скорости {self.speed}")
        else:
            print(f"{message} движется со скоростью {self.speed}")

class SportCar(Car):
    def show_speed(self):        
        print(f"Автомобиль {self.name}, {self.color} цвета - движется со скоростью {self.speed}")        

class WorkCar(Car):
    def show_speed(self):
        message = f"Автомобиль {self.name}, {self.color} цвета -"
        if self.speed > 40:
            print(f"{message} движется c превышением скорости {self.speed}")
        else:
            print(f"{message} движется со скоростью {self.speed}")

class PoliceCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)
        self.is_police = True

    def show_speed(self):
        message = "Полицейский автомобиль" if self.is_police else "Автомобиль"
        print(f"{message} {self.name}, {self.color} цвета - движется со скоростью {self.speed}")

town_car = TownCar(50, "зеленого", "жигули")
town_car.go()
town_car.turn("налево")
town_car.show_speed()
town_car.speed = 80
town_car.show_speed()
town_car.stop()

sport_car = SportCar(100, "красного", "феррари")
sport_car.go()
sport_car.turn("направо")
sport_car.show_speed()
sport_car.speed = 200
sport_car.show_speed()
sport_car.stop()

work_car = WorkCar(60, "белого", "форд")
work_car.go()
work_car.turn("обратно")
work_car.show_speed()
work_car.speed = 30
work_car.show_speed()
work_car.stop()

police_car = PoliceCar(180, "черного", "ламборгини")
police_car.go()
police_car.turn("на север")
police_car.show_speed()
police_car.speed = 100
police_car.show_speed()
police_car.stop()
