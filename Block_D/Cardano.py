import copy
from random import choice
ran = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
rows, cols = 6, 10
default_key = ['0100000000', '1000101100', '0100010001',
               '0001000100', '0100000000', '0010011001']

def encrypt(text, key):
    res = [['']*10 for _ in range(6)]  # Создаем пустую матрицу для результата
    counter = 0
    new_key = copy.deepcopy(default_key)  # Создаем копию ключа для изменений
    for i in range(4):
        for j in range(6):
            for q in range(10):
                if new_key[j][q] == '1':
                    if counter < len(text):
                        res[j][q] = text[counter]
                        counter += 1
                    else:
                        res[j][q] = choice(ran)
        if i == 3:
            break
        if key[i] == '1':
            new_key.reverse()  # Переворачиваем строки в новом ключе
        elif key[i] == '2':
            new_key = [x[::-1] for x in new_key]  # Переворачиваем каждую строку в новом ключе
    # print(res)
    
    return res

def decrypt(text, key):
    res = ''  #пустая строка для результата
    new_key = copy.deepcopy(default_key)  # Создаем копию ключа для изменений
    # for i in key:
    #     if i == '1':
    #         new_key.reverse()  # Переворачиваем строки в новом ключе
    #     elif i == '2':
    #         new_key = [x[::-1] for x in new_key]  # Переворачиваем каждую строку в новом ключе
    for i in range(4):
        for j in range(6):
            for q in range(10):
                if new_key[j][q] == '1':
                    res += text[j][q]
        if i == 3:
            break         
        if key[i] == '1':
            new_key.reverse()  # Переворачиваем строки в новом ключе
        elif key[i] == '2':
            new_key = [x[::-1] for x in new_key]  # Переворачиваем каждую строку в новом ключе
    return res

def split_string(string):
    length = len(string)
    return [string[i:i+60] for i in range(0, length, 60)]


text = input("Введите текст:")
key = input("Введите ключ вида 121, где 1 - переворот решёлтки по вертикали, а 2 - по горизонтали: ")
while True:
    if key == '121' or key == '212':
        break
    else:
        key = input("Некорректный ключ, введите другой: ")
res_enc = []
res_decrypt = ''
text_in_mas = split_string(text)
for i in text_in_mas:
    res_enc.append(encrypt(i, key))

for_print = []
for i in res_enc:
    for j in i:
        for_print.append("".join(j))
    res_decrypt += decrypt(i, key)
print("".join(for_print))
print('\n')
print(res_decrypt)


 