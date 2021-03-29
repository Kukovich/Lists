import random

def line():
    print("------------------------------------------------------------------------------------------------")

print("""Инструкция:
Длина списка должна быть больше нуля и являться целым числом""")
line()

lt = list()
total = 0
act = 0
a = input("Введите длину списка: ")

if a.isdigit():
    if int(a) != 0:
        
        line()
        print("Первый способ:")

        while act != int(a):
            num = random.choice(range(0, 20001))
            lt.append(num)
            total = total + num
            act = act + 1

        print("Сумма значений списка =", total, """
Среднее арифметическое =""", int(total) / int(a))
        line()
        print("Второй способ:")

        act = 0
        total = 0
        lt.clear()

        for two in range(int(a)):
            num = random.choice(range(0, 20001))
            lt.append(num)
            total = total + num
            act = act + 1
        
        print("Сумма значений списка =", total, """
Среднее арифметическое =""", int(total) / int(a))
        line()

    else:
        print("Длина списка должна быть больше нуля")

else:
    print("Введите правильное значение")