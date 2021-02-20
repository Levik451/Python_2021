print('Проверка работы функции умножения двух чисел')
def multiply(var_01, var_02):
    return var_01 * var_02
number_01 = int(input('Введите первое число: '))
number_02 = int(input('Введите второе число: '))
multiply(number_01, number_01)

print(f"Итого: {number_01} * {number_02} = {multiply(number_01, number_02)}")
