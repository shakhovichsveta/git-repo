# Проанализировать скорость и сложность одного любого алгоритма, разработанных в рамках домашнего задания
# первых трех уроков.
# Написать программу, которая будет складывать, вычитать, умножать или делить два числа.
# Числа и знак операции вводятся пользователем. После выполнения вычисления программа не должна завершаться,
# а должна запрашивать новые данные для вычислений.
# Завершение программы должно выполняться при вводе символа '0' в качестве знака операции.
# Если пользователь вводит неверный знак (не '0', '+', '-', '*', '/'), то программа должна сообщать ему об ошибке
# и снова запрашивать знак операции.
# Также сообщать пользователю о невозможности деления на ноль, если он ввел 0 в качестве делителя.
#
#Поправим код программы для чистоты измерения
#Пользователь в явном виде будет задавать знак, в данном случае "+", также добавим выход из программы
#при совпадении знака, во избежании зацикливания
# Вариант a) Выборку знаков будем делать из списка k_list = ['+','-','*','/']
# if z in k_list
import timeit
import cProfile
def s():
    while True:
        z = '+'
        k_list = ['+','-','*','/']
        if z != '0':
            if z in k_list:
                a = 9
                b = 9
                if z == '+':
                    print(f'{a}+{b}={a+b}')
                    break
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
print(timeit.timeit("s()", number=1000, globals=globals()))
cProfile.run('s()')
#timeit : 0.0003166
#cProfile
#4 function calls in 0.000 seconds

#Ordered by: standard name

#ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#       1    0.000    0.000    0.000    0.000 321.py:3(s)
#       1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#       1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#       1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


# b) Выборку знаков будем делать из множества k_set = set('+-*/')
# if z in k_set
def k():
    while True:
        z = '+'
        k_set = set('+-*/')
        if z != '0':
            if z in k_set:
                a = 9
                b = 9
                if z == '+':
                    print(f'{a}+{b}={a+b}')
                    break
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
print(timeit.timeit("k()", number=1000, globals=globals()))
cProfile.run('k()')
#timeit : 0.0005233000000000001
#cProfile
#4 function calls in 0.000 seconds

# Ordered by: standard name

# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#       1    0.000    0.000    0.000    0.000 321.py:3(k)
#       1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#       1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#       1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}