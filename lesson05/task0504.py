# Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.

rus_nam = {1: 'Один', 2: 'Два', 3: 'Три', 4: 'Четыре'}

with open("task04-r.txt", "r", encoding='utf-8') as f_obj:
    number_of_lines = len(f_obj.readlines())
    f_obj.seek(0)
    with open("task04-w.txt", "w", encoding='utf-8') as f_obj_w:
        for i in range(number_of_lines):
            line = f_obj.readline().replace('\n', '').split(' ')
            rus_line = rus_nam[int(line[2])] + ' — ' + line[2]
            f_obj_w.write(rus_line + '\n')
