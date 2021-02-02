'''
Пользователь вводит время в секундах.
Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
Используйте форматирование строк.
'''

user_time = int(input('Введите время в секундах: '))

hour_convert = user_time // 3600
minutes_convert = (user_time % 3600) // 60
sec_convert = (user_time % 3600) % 60

print(f"Время равно: {hour_convert}:{minutes_convert}:{sec_convert}")

# #Отладка
# print(hour_convert)
# print(minutes_convert)
# print(sec_convert)