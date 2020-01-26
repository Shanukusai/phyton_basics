# Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула
# (куда). Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
# Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
# Для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar)
# должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
# Выполните вызов методов и также покажите результат.


class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print('The car drove off.')

    def stop(self):
        print('The car stopped.')

    def turn(self, direction):
        print(f'Turned {direction}')

    def show_speed(self, current_speed):
        print(f'Current speed {current_speed}')


class TownCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, False)

    def show_speed(self, current_speed):
        if current_speed > 60:
            print('You are speeding!')
        else:
            print(f'Current speed {current_speed}')


class SportCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, False)


class WorkCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, False)

    def show_speed(self, current_speed):
        if current_speed > 60:
            print('You are speeding!')
        else:
            print(f'Current speed {current_speed}')


class PoliceCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, True)


tc1 = TownCar(70, 'red', 'lada')
print(tc1.speed)
print(tc1.color)
print(tc1.name)
print(tc1.is_police)

tc1.go()
tc1.stop()
tc1.turn('left')
tc1.show_speed(65)
tc1.show_speed(55)

print()

pc1 = PoliceCar(120, 'white', 'Toyota')
print(pc1.speed)
print(pc1.color)
print(pc1.name)
print(pc1.is_police)

pc1.go()
pc1.stop()
pc1.turn('right')
pc1.show_speed(30)
pc1.show_speed(115)
