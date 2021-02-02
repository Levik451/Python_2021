# Ветвление на примере команд if и else
# Проверяем в какой плоскости координат лежат точки Х и Y
# Логические операторы: and-И or-ИЛИ not-НЕ
# Если ввести 0 то программа обойдет все значения и не по падет в плокость

x = int(input())
y = int(input())

if x > 0 and y > 0:
    print(1)
else:
    if x < 0 and y > 0:
        print(2)
    else:
        if x < 0 and y < 0:
            print(3)
        else:
            if x > 0 and y < 0:
                print(4)
            else:
                print("Никогда не выполнится")