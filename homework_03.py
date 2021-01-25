'''
Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn.
Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.
'''

user_number = int(input('Введите цифру от 1 до 9: '))

if user_number >= 1 and user_number <= 9:
    number_01 = user_number * 11
    number_02 = user_number * 111

    print(f"Ваше число: {user_number} + {number_01} + {number_02} = {user_number + number_01 + number_02} ")
else:
    print('Вы ввели неверное число')