# Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...Количество элементов (n) вводится с клавиатуры.

n = int(input("Введите число элементов n = ")) - 1
s = 0
y = 1
while n > 0:
    s += y
    x = y * (-0.5)
    y = x
    n -= 1
print(s+y)