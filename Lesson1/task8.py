# Определить, является ли год, который ввел пользователем, високосным или невисокосным.

y = int(input("Введите год: "))
if y % 4 != 0:
    print("Не високосный")
elif y % 100 == 0:
    if y % 400 == 0:
        print("Високосный")
    else:
        print("Не високосный")
else:
    print("Високосный")