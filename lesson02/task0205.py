# Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
# У пользователя необходимо запрашивать новый элемент рейтинга.
# Если в рейтинге существуют элементы с одинаковыми значениями,
# то новый элемент с тем же значением должен разместиться после них.
#
# Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2.
# Пользователь ввел число 3. Результат: 7, 5, 3, 3, 3, 2.
# Пользователь ввел число 8. Результат: 8, 7, 5, 3, 3, 2.
# Пользователь ввел число 1. Результат: 7, 5, 3, 3, 2, 1.
#
# Набор натуральных чисел можно задать непосредственно в коде, например, my_list = [7, 5, 3, 3, 2].


rating_list = [7, 5, 3, 3, 2]
game = 'Y'
list_length = len(rating_list)

while game == 'Y' or game == 'y':
    while True:
        try:
            new_rating = int(input('Введите новый рейтинг: '))
            if new_rating < 0:
                raise ValueError
        except ValueError:
            print('Нужно ввести целое не отрицательное число.')
        else:
            list_length = len(rating_list)
            if new_rating < rating_list[list_length - 1]:
                rating_list.insert(list_length, new_rating)
            for index_rating, rating in enumerate(rating_list):
                if rating < new_rating:
                    rating_list.insert(index_rating, new_rating)
                    break
        print(rating_list)
        game = (input('Если играем введите Y: '))
        break
