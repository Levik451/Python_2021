'''
Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка.
'''

with open("empty_file_01.txt", "a+", encoding='utf-8') as f:
    i = 1

    while True:
        user_text = input(f"Введи {i} строку текста: \n")
        if user_text == "":
            break
        else:
            f.writelines(f"{user_text} \n")
            i += 1

with open("empty_file_01.txt", "r", encoding='utf-8') as f:
    data = f.read()
    print(data)