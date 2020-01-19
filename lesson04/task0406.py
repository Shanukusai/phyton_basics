# Реализовать два небольших скрипта:
# а) бесконечный итератор, генерирующий целые числа, начиная с указанного,
# б) бесконечный итератор, повторяющий элементы некоторого списка, определенного заранее.
# Подсказка: использовать функцию count() и cycle() модуля itertools.

import itertools

# Это если решать задание в методичке

i = 0
for el in itertools.count(int(10)):
    if i < 11:
        print(el)
        i += 1
    else:
        break

my_list = [2, 3, 4]
i = 0

for el in itertools.cycle(my_list):
    if i < 11:
        print(el)
        i += 1
    else:
        break

# Это если решать задание по ссылке https://geekbrains.ru/lessons/56773/homework

# for el in itertools.count(int(start)):
#     print(el)
#
# my_list = [2, 3, 4]
#
# for el in itertools.cycle(my_list):
#     print(el)

# Это задание на звездочку, вроде

# def cycle_count_func(start_number, stop_number, iteration):
#     my_list = []
#     for el in itertools.count(start_number):
#         if el > stop_number:
#             break
#         else:
#             print(el)
#             my_list.append(el)
#     i = 0
#     for el in itertools.cycle(my_list):
#         if i < iteration:
#             print(el)
#             i += 1
#         else:
#             break
#
#
# cycle_count_func(start_number=int(input("enter start number: ")), stop_number=int(input("enter stop number: ")),
#                  iteration=int(input("enter iteration: ")))
