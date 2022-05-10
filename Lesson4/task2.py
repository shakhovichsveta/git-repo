# Написать два алгоритма нахождения i-го по счёту простого числа.

import timeit
import random
import cProfile
# Без использования «Решета Эратосфена»
def k():
    a = random.randint(10, 100)
    oth = []
    for i in range(2, a + 1):
        for j in oth:
            if i % j == 0:
                break
        else:
            oth.append(i)
print(timeit.timeit("k()", number=1000, globals=globals()))
cProfile.run('k()')

#timeit : 0.0256657
#cProfile
#21 function calls in 0.000 seconds
# Ordered by: standard name
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#       1    0.000    0.000    0.000    0.000 321.py:4(k)
#       1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#       1    0.000    0.000    0.000    0.000 random.py:173(randrange)
#       1    0.000    0.000    0.000    0.000 random.py:217(randint)
#       1    0.000    0.000    0.000    0.000 random.py:223(_randbelow)
#       1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#      11    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#       1    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
#       1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#       2    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}

# Используя алгоритм «Решето Эратосфена»
def s():
    n = random.randint(10, 100)
    a = []
    for i in range(n + 1):
        a.append(i)
    a[1] = 0
    i = 2
    while i <= n:
        if a[i] != 0:
            j = i + i
            while j <= n:
                a[j] = 0
                j = j + i
        i += 1
    a = set(a)
    a.remove(0)
print(timeit.timeit("s()", number=1000, globals=globals()))
cProfile.run('s()')
# timeit : 0.0281707
# cProfile
# 63 function calls in 0.000 seconds

#  Ordered by: standard name
#  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#       1    0.000    0.000    0.000    0.000 321.py:4(s)
#       1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#       1    0.000    0.000    0.000    0.000 random.py:173(randrange)
#       1    0.000    0.000    0.000    0.000 random.py:217(randint)
#       1    0.000    0.000    0.000    0.000 random.py:223(_randbelow)
#       1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#      52    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#       1    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
#       1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#       2    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}
#       1    0.000    0.000    0.000    0.000 {method 'remove' of 'set' objects}
