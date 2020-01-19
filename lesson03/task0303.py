# Реализовать функцию my_func(), которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.


"""
Первый вариант
def my_func(a, b, c):
    list_abc = [a, b, c]
    max_1 = max(list_abc)
    list_abc.remove(max_1)
    max_2 = max(list_abc)
    print(max_1 + max_2)
"""

"""Второй вариант"""


def my_func(a, b, c):
    list_abc = [a, b, c]
    list_abc.remove(min(list_abc))
    print(sum(list_abc))


my_func(3, 8, 10)

# Или можно так:
# try:
#     a = float(input("Введите первое число: "))
#     b = float(input("Введите второе число: "))
#     c = float(input("Введите третье число: "))
#     my_func(a, b, c)
# except ValueError:
#     print('Введите корректные данные.')
