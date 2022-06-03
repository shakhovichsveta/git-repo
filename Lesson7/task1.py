# Задание №1
# Отсортировать по убыванию методом «пузырька» одномерный целочисленный массив,
# заданный случайными числами на промежутке [-100; 100). Вывести на экран исходный и отсортированный массивы.
import random


def sort_to_min(origin_list):  # функция сортировки массива по убыванию методом "пузырька"
    n = 1
    while n < len(origin_list):
        for i in range(len(origin_list) - n):
            if origin_list[i] < origin_list[i + 1]:
                origin_list[i], origin_list[i + 1] = origin_list[i + 1], origin_list[i]
        n += 1
    return (origin_list)


list_n = []
for i in range(15):
    list_n.append(random.randrange(-100, 100))

print(f'Исходный массив: {list_n}')
print(f'Отсортированный массив: {sort_to_min(list_n)}')