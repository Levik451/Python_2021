"""
Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.
"""

with open("file_task_2.txt", "r", encoding='utf-8') as f:
    orig_data = f.read()
    print(f"{orig_data} \n")

with open("file_task_2.txt", "r", encoding='utf-8') as f:
    data = f.read().splitlines()
    number_of_chars = len(data)
    print(f"Количество строк в тексте файла =  {number_of_chars}")

    for i, value in enumerate(data):
        num_of_words = len(value.split())
        string_len = len(value)
        print(f"В строке {data.index(value) + 1} количетсво слов = {num_of_words} и количетво символов = {string_len}")
