import random

def line():
    print("------------------------------------------------------------------------------------------------------------------")

act = 0
lt = list()
lt1 = list()

while act != 20:
    num = random.randint(0, 25)
    lt.append(num)

    num1 = random.randint(0, 25)
    lt1.append(num1)

    act = act + 1

print("Начальная версия первого списка:", lt)
line()
print("Второй список:", lt1)

for recurring in lt1:
    while recurring in lt:
        lt.remove(recurring)

line()
print("Конечная версия первого списка:", lt)