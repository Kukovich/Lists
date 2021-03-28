import random

def line():
    print("------------------------------------------------------------------------------------------------")

act1 = 0
act = 0
lt = list()
lt1 = list()

while act != 20:
    num = random.randint(0, 25)
    lt.append(num)
    act = act + 1

print("Начальный список 1:", lt)
line()

while act1 != 20:
    num1 = random.randint(0, 25)
    lt1.append(num1)
    while num1 in lt:
        lt.remove(num1)
    act1 = act1 + 1

print("Список 2:", lt1)
line()
print("Конечный список 1:", lt)