# Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же,
# но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.
# Продолжить работу над заданием. В программу должна попадать строка из слов, разделенных пробелом.
# Каждое слово состоит из латинских букв в нижнем регистре. Сделать вывод исходной строки,
# но каждое слово должно начинаться с заглавной буквы. Необходимо использовать написанную ранее функцию int_func().


# Так
# def int_func(string_line):
#     print(string_line.title())

# Или так
# import string
# def int_func(string_line):
#     print(string.capwords(string_line))

# Или вот так
# def int_func(string_line):
#     return print(' '.join(w.capitalize() for w in string_line.split(' ')))


# Или возможно вот так
def int_func(string_l):
    return print(' '.join(w[0].upper() + w[1:] for w in string_l.split()))


string_line = input('Введите предложение: ')
int_func(string_line)
