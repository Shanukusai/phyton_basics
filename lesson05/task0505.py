# Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

with open("task05.txt", "w", encoding='utf-8') as f_obj:
    f_obj.write('1 2 3 4 5 6')

with open("task05.txt", "r", encoding='utf-8') as f_obj:
    line = f_obj.readline().split(' ')
    sum_nam = 0
    for i in range(len(line)):
        sum_nam += int(line[i])
    print(sum_nam)
