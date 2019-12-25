# Запросите у пользователя значения выручки и издержек фирмы.
# Определите, с каким финансовым результатом работает фирма
# (прибыль — выручка больше издержек, или убыток — издержки больше выручки).
# Выведите соответствующее сообщение.
# Если фирма отработала с прибылью, вычислите рентабельность выручки (соотношение прибыли к выручке).
# Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчете на одного сотрудника.

print('Данная программа делает расчеты некоторых финансовых показателей.')
revenue = int(input('Внесите значние выручки: '))
costs = int(input('Внесите значние издержек: '))

profit_or_loss = revenue - costs

if profit_or_loss > 0:
    print(f'Поздравляю! Ваша прибыль составила: {profit_or_loss}')
    print(f'Ваша рентабельность: {profit_or_loss / revenue:.2%}')
    number_of_employees = int(
        input('Введите численность сотрудников для растча размера прибыли на одного сотрудника: '))
    print(f'Прибыль на одного сотрудика: {profit_or_loss / number_of_employees:.2f}')
elif profit_or_loss == 0:
    print(f'Вы ничего не заработали, но и не потеряли. Ваша прибыль равна {profit_or_loss}')
else:
    print(f'Сочувствую! Ваш убыток составил: {profit_or_loss}')