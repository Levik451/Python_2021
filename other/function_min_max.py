number_01 = int(input('Введите первое число: '))
number_02 = int(input('Введите второе число: '))
number_03 = int(input('Введите третье число: '))

min_number = min(number_01, number_02, number_03)
max_number = max(number_01, number_02, number_03)
sum_number = min_number + max_number

print(f'Минимальное число: {min_number}')
print(f'Макcимальное число: {max_number}')
print(f'Сумма чисел равна: {sum_number}')