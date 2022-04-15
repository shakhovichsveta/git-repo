# Написать программу, которая генерирует в указанных пользователем границах
# - случайное целое число
# - случайное вещественное число
# - случайный символ.
# Для каждого из трех случаев пользователь задает свои границы диапазона.
# Например, если надо получить случайный символ от 'a' до 'f', то вводятся эти символы. Программа должна вывести на экран любой символ алфавита от 'a' до 'f' включительно.

import random

min_a = int(input('Введите нижнюю границу диапазона целого числа: '))
max_a = int(input('Введите нижнюю границу диапазона целого числа: '))
print(f'Случайное целое число из диапазона: {random.randint(min_a, max_a)}')

min_b = float(input('Введите нижнюю границу диапазона вещественного числа: '))
max_b = float(input('Введите нижнюю границу диапазона вещественного числа: '))
print(f'Случайное вещественное число из диапазона: {random.uniform(min_b, max_b)}')

min_c = ord(input('Введите нижнюю границу диапазона символов: '))
max_c = ord(input('Введите нижнюю границу диапазона символов: '))
print(f'Случайный символ из диапазона: {chr(random.randint(min_c, max_c))}')