# Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
# имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы. Реализовать вывод данных о пользователе одной строкой.


# Это универсальненько
# def user_data(**kwargs):
#     return print(kwargs)

# А это красивишно
def user_data(name, surname, date_of_birth, current_city, email, phone):
    print(f'{name} {surname} родился/родилась {date_of_birth} проживает в городе {current_city}. '
          f'Контактные данные: тел. {phone}, e-mail {email}')


user_data(name=input("Ведите свое имя: "), surname=input("Ведите свою фамилию: "),
          date_of_birth=input("Ведите свою дату рождения: "), current_city=input("Ведите свой город проживания: "),
          email=input("Ведите свой e-mail: "), phone=input("Ведите свой телефон: "))
