# Для списка реализовать обмен значений соседних элементов, т.е.
# Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
# При нечетном количестве элементов последний сохранить на своем месте.
# Для заполнения списка элементов необходимо использовать функцию input().


my_list = list(input('Введите свое имя: '))
print(my_list)

for index_element, element in enumerate(my_list):
    if index_element % 2 != 0:
        revers_element = element
        my_list.pop(index_element)
        my_list.insert(index_element - 1, revers_element)

print(my_list)
