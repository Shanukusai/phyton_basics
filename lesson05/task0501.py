# Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных свидетельствует пустая строка.

with open("task01.txt", "w", encoding='utf-8') as f_obj:
    string = input('Enter to write to the file. To finish, the line must be empty. ')
    while string != '':
        f_obj.write(string + '\n')
        string = input('Enter to write to the file. To finish, the line must be empty. ')
