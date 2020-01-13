# Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.


def division_f(my_numerator, my_denominator):
    try:
        division_result = round(my_numerator / my_denominator, 3)
    except ZeroDivisionError:
        return print('На ноль делить нельзя.')
    return division_result


try:
    a = float(input("Укажите числитель: "))
    b = float(input("Укажите знаменатель: "))
    print(division_f(a, b))
except ValueError:
    print('Введите корректные данные.')
