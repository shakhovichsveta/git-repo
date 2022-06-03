# Задание №3
# Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом. Найти в массиве медиану.
# Медианой называется элемент ряда, делящий его на две равные части:
# в одной находятся элементы, которые не меньше медианы, в другой – не больше ее.

import random
from alg_str_puthon.hw2_7 import mergesort


def mediana(data):
    data = mergesort(data)
    if len(data) % 2 != 0:
        return data[len(data) // 2]
    else:
        a = len(data) // 2 - 1
        b = len(data) // 2
        i = (data[a] + data[b]) / 2
        return i


m = 10
list_n = []
for i in range(2 * m + 1):
    list_n.append(random.randint(1, 100))

print(f'Исходный массив: {list_n}')
print(f'Отсортированный массив: {mergesort(list_n)}')
print(f'Медиана: {mediana(list_n)}')