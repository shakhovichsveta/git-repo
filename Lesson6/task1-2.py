# Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах в рамках первых трех уроков.
# Проанализировать результат и определить программы с наиболее эффективным использованием памяти.
# Примечание: Для анализа возьмите любые 1-3 ваших программы или несколько вариантов кода для одной и той же задачи.
# Результаты анализа вставьте в виде комментариев к коду. Также укажите в комментариях версию Python и разрядность
# вашей ОС.
# Задание 1 Урок 2:
# Написать программу, которая будет складывать, вычитать, умножать или делить два числа.
# Числа и знак операции вводятся пользователем. После выполнения вычисления программа не должна завершаться,
# а должна запрашивать новые данные для вычислений.
# Завершение программы должно выполняться при вводе символа '0' в качестве знака операции.
# Если пользователь вводит неверный знак (не '0', '+', '-', '*', '/'), то программа должна сообщать ему об ошибке
# и снова запрашивать знак операции.
# Также сообщать пользователю о невозможности деления на ноль, если он ввел 0 в качестве делителя.
# Версия Python - 3.7
# Разрядность ОС - x64
from memory_def import total_size
set_n = {'+', '-', '*', '/'}
tuple_n = ('+', '-', '*', '/')
while True:
    z = input("Введите знак: ")
    if z != '0':
        if z in tuple_n:  # or tuple_n
            a = float(input("Введите первое число: "))
            b = float(input("Введите второе число: "))
            if z == '+':
                print(f'{a}+{b}={a+b}')
            elif z == '-':
                print(f'{a}-{b}={a-b}')
            elif z == '*':
                print(f'{a}*{b}={a*b}')
            elif z == '/':
                if b == 0:
                    print("На ноль делить нельзя!")
                else:
                    print(f'{a}/{b}={a/b}')
        else:
            print("Неверный знак")
    else:
        break

#print(total_size(set_n, verbose=True))
print(total_size(tuple_n, verbose=True))
# 424 байт - множество
# 224 <class 'set'> {'+', '-', '/', '*'}
# 50 <class 'str'> '+'
# 50 <class 'str'> '-'
# 50 <class 'str'> '/'
# 50 <class 'str'> '*'

# 280 байт - кортеж
# 80 <class 'tuple'> ('+', '-', '*', '/')
# 50 <class 'str'> '+'
# 50 <class 'str'> '-'
# 50 <class 'str'> '*'
# 50 <class 'str'> '/'