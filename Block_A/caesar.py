#Выбираем режим работы с карточкой или с текстом
task = int(input("Работа с карточкой - 1, работа с большим текстом - 2: "))
if task == 1:
    big_alphabit = 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
    small_alphabit = big_alphabit.lower()
else:
    big_alphabit = 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ @#!%^&*()-+.:;'
    small_alphabit = big_alphabit.lower()

length_of_alph = len(big_alphabit)
# режим шифрования
mode = int(input("Выберите режим (1 - шифрование; 2 - расшифрование): "))
# ввод ключа
key = 0
while True:
    key = int(input('Введите ключ (сдвиг, не кратный мощности алфавита): '))
    if key % length_of_alph != 0:
        break
    print(f"Ошибка! Длина сдвига не должна быть кратна {length_of_alph}")

open_text = input("Введите сообщение: ")
cipher_text = ""
# шифрование
if mode == 1:
    for i in open_text:
        #Находим на какой поизиции стоит буква в алфавите
        ind = small_alphabit.find(i)
        #Если мы находим букву в алфавите со строчными буквами, то работаем с ними, иначе работаем по алфавиту прописных букв.
        if ind != -1:
            cipher_text += small_alphabit[(ind+key) % length_of_alph]
            continue
        ind = big_alphabit.find(i)
        if ind != -1:
            cipher_text += big_alphabit[(ind+key) % length_of_alph]
            continue
        #Для случая, если буква не найдена ни в одном из алфавитов
        else:
            cipher_text += i
# расшифрование аналогично шифрованию
elif mode == 2:
    for i in open_text:
        ind = small_alphabit.find(i)
        if ind != -1:
            cipher_text += small_alphabit[(ind-key) % length_of_alph]
            continue
        ind = big_alphabit.find(i)
        if ind != -1:
            cipher_text += big_alphabit[(ind-key) % length_of_alph]
            continue
        else:
            cipher_text += i
#Выводим результат работы программы
print(cipher_text)