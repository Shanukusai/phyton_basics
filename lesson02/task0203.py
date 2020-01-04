# Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень). Напишите решения через list и через dict.

# Решение через dict

while True:
    try:
        my_month = int(input('Введите номер месяца: '))
        if my_month > 12 or my_month < 1:
            raise ValueError
    except ValueError:
        print('Нужно ввести целое не отрицательное число от 1 до 12.')
    else:
        dict_seasons = dict(winter=[12, 1, 2], spring=[3, 4, 5], summer=[6, 7, 8], autumn=[9, 10, 11])
        for key in dict_seasons:
            for value in dict_seasons[key]:
                if value == my_month:
                    print(key)
        break

# Решение через list

while True:
    try:
        my_month = int(input('Введите номер месяца: '))
        if my_month > 12 or my_month < 1:
            raise ValueError
    except ValueError:
        print('Нужно ввести целое не отрицательное число от 1 до 12.')
    else:
        list_seasons_month = [[12, 1, 2], [3, 4, 5], [6, 7, 8], [9, 10, 11]]
        list_seasons = ['winter', 'spring', 'summer', 'autumn']
        for index_season, season in enumerate(list_seasons_month):
            for index_month, month in enumerate(season):
                if month == my_month:
                    print(list_seasons[index_season])
        break
