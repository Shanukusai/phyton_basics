# Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк,
# количества слов в каждой строке.


with open("task02-03.txt", "r", encoding='utf-8') as f_obj:
    count_line = len(f_obj.readlines())
    print(count_line)
    f_obj.seek(0)
    count_w = sum(len(f_obj.readline().split(' ')) for line in range(count_line))
    print(count_w)
