# Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов
# (не менее 10 строк). Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
# Выполнить подсчет средней величины дохода сотрудников.
# Пример файла:
# Иванов 23543.12
# Петров 13749.32

staff = []
payroll = 0

with open("task02-03.txt", "r", encoding='utf-8') as f_obj:
    number_of_lines = len(f_obj.readlines())
    f_obj.seek(0)
    for i in range(number_of_lines):
        line = f_obj.readline().replace('\n', '').split(' ')
        if float(line[1]) < 20000.00:
            staff.append(line[0])
        payroll += float(line[1])

print(f'Сотрудники, которые имееют оклад менее 20 тыс.: {staff}')
print(f'Средняя величина дохода сотрудников: {payroll / number_of_lines}')
