def crypt(text, mode, key):
    res = ''
   
    if mode == 1:
        key = key + text
        for i in range(len(text)):
        #Находим на какой поизиции стоит буква в алфавите
            ind = big_alphabit.find(text[i])
            dif = big_alphabit.find(key[i])
        #Если мы находим букву в алфавите со строчными буквами, то работаем с ними, иначе работаем по алфавиту прописных букв.
            if ind != -1:
                res += big_alphabit[(ind+dif) % length_of_alph]
                continue
        #Для случая, если буква не найдена 
            else:
                res += text[i]
# расшифрование аналогично шифрованию
    elif mode == 2:
        res += key
       
        for i in text:
            ind = big_alphabit.find(i)
            dif = big_alphabit.find(res[-1])
            if ind != -1:
                res += big_alphabit[(ind-dif) % length_of_alph]
                continue
            else:
                res += i
        res = res[1:]
    return res



mode = int(input("Выберите режим (1 - шифрование; 2 - расшифрование): "))
type_text = int(input("Выберите с каким текстом вы будете пработать (0 - поговорка, 1 - текст > 1000 символов): "))
big_alphabit = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'

if type_text == 1:
    big_alphabit = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ@#!%^?&*()-+.:;,'
length_of_alph = len(big_alphabit)
open_text = input("Введите текст для работы: ")

key = input("Введите ключ (один символ): ")
print('Результат: \n')
print(crypt(open_text, mode, key))
