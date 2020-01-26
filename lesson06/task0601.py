# Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
# Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора в режимы: красный, желтый,
# зеленый. Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды, третьего
# (зеленый) — на ваше усмотрение.  Переключение между режимами должно осуществляться только в указанном порядке
# (красный, желтый, зеленый). Проверить работу примера, создав экземпляр и вызвав описанный метод.
# Задачу можно усложнить, реализовав проверку порядка режимов,
# и при его нарушении выводить соответствующее сообщение и завершать скрипт.

import itertools
import time
from tkinter import Tk, Canvas


# class TrafficLight:
#     __color = {'red': 7, 'yellow': 2, 'green': 5, 'yеllow': 2}
#
#     def running(self):
#         while True:
#             for k, v in self.__color.items():
#                 print(k)
#                 time.sleep(v)
#
#
# tl = TrafficLight()
# tl.running()


class TrafficLight:
    __color = ['red', 'yellow', 'green', 'yellow']

    def running(self):

        size = 300
        root = Tk()
        canvas = Canvas(root, width=size, height=size)
        canvas.pack()
        diapason = 0

        canvas.create_oval(10, 10, 60, 60, outline="gray", fill="gray", width=2)
        canvas.create_oval(10, 70, 60, 120, outline="gray", fill="gray", width=2)
        canvas.create_oval(10, 130, 60, 180, outline="gray", fill="gray", width=2)

        for color in itertools.cycle(self.__color):
            if color == 'red':
                canvas.create_oval(10, 10, 60, 60, outline=color, fill=color, width=2, tag='red_circle')
                for i in range(7):
                    canvas.create_text(35, 35, font="Purisa", fill='white', text=(7 - i), tag='red_text')
                    root.update()
                    time.sleep(1)
                    canvas.delete('red_text')
                canvas.delete('red_circle')
                canvas.create_oval(10, 10, 60, 60, outline="gray", fill="gray", width=2)
                root.update()
            elif color == 'yellow':
                canvas.create_oval(10, 70, 60, 120, outline=color, fill=color, width=2, tag='yellow_circle')
                for i in range(2):
                    canvas.create_text(35, 95, font="Purisa", fill='black', text=(2 - i), tag='yellow_text')
                    root.update()
                    time.sleep(1)
                    canvas.delete('yellow_text')
                canvas.delete('yellow_circle')
                canvas.create_oval(10, 70, 60, 120, outline="gray", fill="gray", width=2)
                root.update()
            else:
                canvas.create_oval(10, 130, 60, 180, outline=color, fill=color, width=2, tag='green_circle')
                for i in range(5):
                    canvas.create_text(35, 155, font="Purisa", fill='black', text=(5 - i), tag='green_text')
                    root.update()
                    time.sleep(1)
                    canvas.delete('green_text')
                canvas.delete('green_circle')
                canvas.create_oval(10, 130, 60, 180, outline="gray", fill="gray", width=2)
                root.update()


tl = TrafficLight()
tl.running()
