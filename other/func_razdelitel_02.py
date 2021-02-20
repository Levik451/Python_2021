# Функция красивый разделитель строк
def get_sep(sep, sep_len):
    return sep * sep_len

# Меняем знак и длину разделителя
print(get_sep('*', 100))
print(get_sep('+', 100))

# Возвращаемое значение функции
sep = get_sep('_', 45)
text = "Hello {} Func {}".format(sep, sep)
print(text)