# Создать вручную и заполнить несколькими строками текстовый файл,
# в котором каждая строка должна содержать данные о фирме: название, форма собственности, выручка, издержки.
# Пример строки файла: firm_1   ООО   10000   5000.
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
# Если фирма получила убытки, в расчет средней прибыли ее не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
# Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
# Подсказка: использовать менеджер контекста.

import json

with open("task07.txt", "r", encoding='utf-8') as f_obj:
    number_of_lines = len(f_obj.readlines())
    f_obj.seek(0)
    company_profit = {}
    total_profit = 0
    number_profitable_firms = 0
    for i in range(number_of_lines):
        line = f_obj.readline().replace('\n', '').split(' ')
        profit = int(line[2]) - int(line[3])
        company_profit.update({line[0]: profit})
        if profit >= 0:
            total_profit += profit
            number_profitable_firms += 1

average_profit = {'average_profit': (total_profit / number_profitable_firms)}

with open("task07-json.txt", "w", encoding='utf-8') as f_objson:
    json.dump([company_profit, average_profit], f_objson, sort_keys=True, indent=4, separators=(',', ': '))
