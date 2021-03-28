import random

lt = list()
total = 0
act = 0
a = input("Введите длину списка: ")

if a.isdigit():
    if a != 0:

        while act != int(a):
            num = random.choice(range(0, 20001))
            lt.append(num)
            total = total + num
            act = act + 1
            print(1)

        print("Сумма значений списка = ", total)
        print("Среднее арифметическое = ", int(total) / int(a))
        print("Второй способ")

        act = 0
        total = 0
        lt.clear()

        for two in range(int(a)):
            num = random.choice(range(0, 20001))
            lt.append(num)
            total = total + num
            act = act + 1
            print(1)
        
        print("Сумма значений списка = ", total)
        print("Среднее арифметическое = ", int(total) / int(a))
