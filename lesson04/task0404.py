# Представлен список чисел. Определить элементы списка, не имеющие повторений.
# Сформировать итоговый массив чисел, соответствующих требованию.
# Элементы вывести в порядке их следования в исходном списке. Для выполнения задания обязательно использовать генератор.

from random import randint

size = 25
random_arr = [randint(1, 15) for _ in range(size)]
print(random_arr)

result_set = [random_arr[i] for i in range(size - 1) if random_arr.count(random_arr[i]) == 1]
print(result_set)

# Вариант №2

# result_set = set(random_arr) - set([random_arr[i] for i in range(size - 1) for j in range(i+1, size) if random_arr[i] == random_arr[j]])
# print(result_set)

# Вариант №3

# for i in range(size - 1):
#     replay = 1
#     for j in range(i+1, size):
#         if random_arr[i] == random_arr[j]:
#             replay += 1
#             random_arr.pop(j)
#             random_arr.insert(j, None)
#     counter_list.update({random_arr[i]: replay})
#
# result_set = [k for k, v in counter_list.items() if v == 1]

# Вариант №4

# for i in range(size - 1):
#     replay = 0
#     for j in range(size - 1):
#         if random_arr[i] == random_arr[j] and i != j:
#             replay = 1
#             break
#     if replay == 0:
#         result_set.append(random_arr[i])

# Вариант №5

# for i in range(size - 1):
#     for j in range(i+1, size):
#         if random_arr[i] == random_arr[j]:
#             counter_list.add(random_arr[i])
#
# result_set = set(random_arr) - counter_list
