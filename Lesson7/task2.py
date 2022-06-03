# Задание №2
# Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
# заданный случайными числами на промежутке [0; 50). Выведите на экран исходный и отсортированный массивы.

import random


def merge(left, right):
    list = []
    while left and right:
        if left[0] < right[0]:
            list.append(left.pop(0))
        else:
            list.append(right.pop(0))
    if left:
        list.extend(left)
    if right:
        list.extend(right)
    return list


def mergesort(list):
    length = len(list)
    if length >= 2:
        middle = int(length / 2)
        list = merge(mergesort(list[:middle]), mergesort(list[middle:]))
    return list


list_n = []
for i in range(15):
    list_n.append(random.random() * 50)

print(f'Исходный массив: {list_n}')
print(f'Отсортированный массив: {mergesort(list_n)}')