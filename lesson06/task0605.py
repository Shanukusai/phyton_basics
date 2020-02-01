# Реализовать класс Stationery (канцелярская принадлежность). Определить в нем атрибут title (название) и
# метод draw (отрисовка). Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса Pen (ручка),
# Pencil (карандаш), Handle (маркер). В каждом из классов реализовать переопределение метода draw.
# Для каждого из классов метод должен выводить уникальное сообщение. Создать экземпляры классов и проверить,
# что выведет описанный метод для каждого экземпляра.


class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки.')


class Pen:
    def draw(self):
        print('Запуск отрисовки ручкой.')


class Pencil:
    def draw(self):
        print('Запуск отрисовки карандашом.')


class Handle:
    def draw(self):
        print('Запуск отрисовки маркером.')


pen1 = Pen()
pen1.draw()
print()
pencil1 = Pencil()
pencil1.draw()
print()
handle1 = Handle()
handle1.draw()
print()
