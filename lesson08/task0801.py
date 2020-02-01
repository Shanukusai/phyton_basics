# Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
# В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен извлекать число, месяц, год и
# преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod,
# должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
# Проверить работу полученной структуры на реальных данных.

import calendar


class Date:

    def __init__(self, user_data):
        self.user_data = user_data

    @classmethod
    def date_retrieval(cls, user_data):
        return [int(data) for data in user_data.split('-')]

    @staticmethod
    def date_validation(user_data):
        user_data_int = Date.date_retrieval(user_data)
        day_leap = {1: 31, 2: 29, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
        day_not_leap = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
        if 13 > user_data_int[1] > 0:
            if calendar.isleap(user_data_int[2]):
                if day_leap[user_data_int[1]] >= user_data_int[0] > 0:
                    return f'Ваша дата существует'
                else:
                    return f'Такого дня в високосном году не существует'
            else:
                if day_not_leap[user_data_int[1]] >= user_data_int[0] > 0:
                    return f'Ваша дата существует'
                else:
                    return f'Такого дня в не високосном году не существует'
        else:
            return f'Такого месяца не существует'


print(Date.date_retrieval('29-02-2021'))
print(Date.date_validation('29-02-2021'))
