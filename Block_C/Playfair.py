# print(len("АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ @#!%^&*()-+.:;абвгдежзийклмнопрстуфхцчшщъыьэюя"))

def split_and_adjust(string):
    substrings = []
    i = 0
    while i < len(string):
        if i == len(string) - 1:
            substrings.append([string[i], ""])  # Добавляем последний символ как подстроку
            break
        if string[i] == string[i+1]:  # Проверяем на повторение символов
            substrings.append([string[i], "ф"])  # Если повторяется, заменяем второй символ
            i += 1  # Переходим к следующему символу
        else:
            substrings.append([string[i], string[i+1]])  # Если нет повторения, добавляем оба символа
            i += 2  # Переходим к следующей паре символов
    if substrings[-1][1] == "":
        substrings[-1][1] = "ф"
    return substrings

def crypt(text, mode, task, table):
    res = ''
    if task == 1:
        size = 6
    elif task == 2:
        size = 9
    open_text = split_and_adjust(text)
    if mode == 1:
        for i in open_text:
            a = table.index(i[0])
            b = table.index(i[1])
            strokA, strokB = a//size, b//size
            if strokA == strokB:
                res += table[(a+1)%size + size*strokA]
                res += table[(b+1)%size + size*strokA]
            elif a%size == b%size:
                res += table[(a+size)%len(table)]
    return res


mode = int(input("Выберите режим (1 - шифрование; 2 - расшифрование): "))
task = int(input("Работа с карточкой - 1, работа с большим текстом - 2: "))
if task == 1:
    big_alphabit = 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЫЬЭЮЯ'
elif task == 2:
    big_alphabit = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ @#!%^&*()-+.:;абвгдежзийклмнопрстуфхцчшщъыьэюя'
key = input("Введите ключ:")
table = []

 
open_text = input("Введитек текст для работы: \n")
if task == 1:
    key = key.upper()
    open_text = open_text.upper()
    open_text.replace("Ъ","Ь")
    open_text.replace("Ё","Е")
    
for i in key:
    table.append(i)
for i  in big_alphabit:
    if i not in key:
        table.append(i)

print(table)
# print(crypt(open_text, mode, task, table))