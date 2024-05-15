print("Выберите алогритм для работы:\n1 - Атбаш\n2 - Шифр Цезаря\n3 - Квадрат Полибия")
print("4 - Белазо\n5 - S-block\n6 - Тритемий\n7 - Шифр Виженера\n8 - Матричный шифр")
print("9 - Шифр Плэйфера\n10 - Решётка Кардано\n11 - Вертикальная перстановка")
print("12 - Сеть Фейстеля\n13 - Блокнот Шенона\n14 - Гаммирование")
print("15 - A5/1\n16 - A5/2\n17 - Кузнечик\n18 - Магма\n19 - ECC")
print("20 - Elgamal\n21 - RSA\n22 - ЦП RSA\n23 - ЦП Elgamal\n24 - ЦП ГОСТ 2012")
print("25 - ЦП ГОСТ 94\n26 - Обмен ключами по алгоритму Диффи-Хелмана")
choice = int(input("Выбор: "))
if choice == 1:
    def crypt(text):
        res = ''
        for i in text:
            #Находим на какой поизиции стоит буква в алфавите
            ind = small_alphabit.find(i)
            #Если мы находим букву в алфавите со строчными буквами, то работаем с ними, иначе работаем по алфавиту прописных букв.
            if ind != -1:
                res += small_alphabit[-ind-1]
                continue
            ind = big_alphabit.find(i)
            if ind != -1:
                res += big_alphabit[-ind-1]
                continue
            #Для случая, если буква не найдена ни в одном из алфавитов
            else:
                res += i
        return res

    # mode = int(input("Выберите режим (1 - шифрование; 2 - расшифрование): "))
    task = int(input("Работа с карточкой - 1, работа с большим текстом - 2: "))
    if task == 1:
        big_alphabit = 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
        small_alphabit = big_alphabit.lower()
    else:
        big_alphabit = 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ @#!%^&*()-+.:;'
        small_alphabit = big_alphabit.lower()
    open_text = input("Введитек текст для работы: \n")
    print(crypt(open_text))
elif choice == 2:
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
elif choice == 3:
    letters = {"А": "11", "Б": "12", "В": "13", "Г": "14", "Д": "15", "Е": "16", "Ё": "21",
               "Ж": "22", "З": "23", "И": "24", "Й": "25", "К": "26", "Л": "31", "М": "32",
               "Н": "33", "О": "34", "П": "35", "Р": "36", "С": "41", "Т": "42", "У": "43",
               "Ф": "44", "Х": "45", "Ц": "46", "Ч": "51", "Ш": "52", "Щ": "53", "Ъ": "54",
               "Ы": "55", "Ь": "56", "Э": "61", "Ю": "62", "Я": "63",
               "а": "64", "б": "65", "в": "66", "г": "67", "д": "68", "е": "69", "ё": "70",
               "ж": "71", "з": "72", "и": "73", "й": "74", "к": "75", "л": "76", "м": "77",
               "н": "78", "о": "79", "п": "80", "р": "81", "с": "82", "т": "83", "у": "84",
               "ф": "85", "х": "86", "ц": "87", "ч": "88", "ш": "89", "щ": "90", "ъ": "91",
               "ы": "92", "ь": "93", "э": "94", "ю": "95", "я": "96", "!": "97", "@": "98",
                ".": "99", ",": "100", "%": "101", "^": "102", "&": "103", "*": "104",
                 "(": "105", ")": "106", "-": "107", "_": "108", "=": "109", "+": "110",
               " ": "111", "]": "112", "{": "113", "}": "114"}


    alp = {"А": "11", "Б": "12", "В": "13", "Г": "14", "Д": "15", "Е": "16",
               "Ж": "21", "З": "22", "И": "23", "Й": "24", "К": "25", "Л": "26", "М": "31",
               "Н": "32", "О": "33", "П": "34", "Р": "35", "С": "36", "Т": "41", "У": "42",
               "Ф": "43", "Х": "44", "Ц": "45", "Ч": "46", "Ш": "51", "Щ": "52", "Ъ": "53",
               "Ы": "54", "Ь": "55", "Э": "56", "Ю": "61", "Я": "62"}

    def encrypt(text, task):
        res = []
        if task == 2:
            for x in text:
                res.append(letters.get(x))
        elif task == 1:
            for x in text:
                res.append(alp.get(x))

        return res

    def decrypt(text, task):
        res = ""
        if task == 2:
            for i in text:
                for key, val in letters.items():
                    if val == i:
                        res += key
        elif task == 1:
            for i in text:
                for key, val in alp.items():
                    if val == i:
                        res += key
        return res

    text = input("Введите фразу: ")
    task = int(input("Выберите режим работы (1 - карточка, 2 - текст > 1000 cимволов): "))
    result = encrypt(text, task)
    print("Зашифрованный текст: " + ''.join(result))

    print("Текст для расшифровки : " + ''.join(result))
    print("Результат : " + decrypt(result, task))
elif choice == 4:
    def decrypt(text, key):
        res = ''  
        alphabet = "абвгдежзийклмнопрстуфхцчшщъыьэюя" + "абвгдежзийклмнопрстуфхцчшщъыьэюя".upper() + " !\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"
        offset = 0  
        
        for ix in range(len(text)):  # Проходим по каждому символу в сообщении
            if text[ix] not in alphabet:  # Если символ не находится в алфавите, то оставляем его без изменений
                output = text[ix]
                offset += -1  # Уменьшаем смещение, чтобы правильно сопоставить символы
            else:
                # Расшифровываем символ с помощью ключа и алфавита с учетом смещения
                output = alphabet[(alphabet.find(text[ix]) - (alphabet.find(key[((ix + offset) % len(key))]))) % len(alphabet)]
            res += output  # Добавляем расшифрованный символ к результату
        return res  # Возвращаем расшифрованный текст
    
    def encrypt(text, key):
        encrypted_text = ''  
        alphabet = "абвгдежзийклмнопрстуфхцчшщъыьэюя" + "абвгдежзийклмнопрстуфхцчшщъыьэюя".upper() + " !\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"
        offset = 0  # Смещение для коррекции индексов шифрованного текста
        
        for ix in range(len(text)):  # Проходим по каждому символу в сообщении
            if text[ix] not in alphabet:  # Если символ не находится в алфавите, то оставляем его без изменений
                output = text[ix]
                offset += -1  # Уменьшаем смещение, чтобы правильно сопоставить символы
            else:
                # Шифруем символ с помощью ключа и алфавита с учетом смещения
                output = alphabet[(alphabet.find(text[ix]) + (alphabet.find(key[((ix + offset) % len(key))]))) % len(alphabet)]
            encrypted_text += output 
        return encrypted_text  
        
    text = input("введите текст:")
    key = input("вввдеите ключ: ")
    encrypted_result = encrypt(text=text, key=key)
    print("Зашифрованный текст:", encrypted_result)
    print("Расшифрованный текст:", decrypt(text=encrypted_result, key=key))
elif choice == 5:
    simbs = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ.,-+/!&%? "
    hex_val = "00 01 02 03 04 05 06 07 08 09 0A 0B 0C 0D 0E 0F 10 11 12 13 14 15 16 17 18 19 1A 1B 1C 1D 1E 1F 20 21 22 23 24 25 26 27 28 29 2A 2B 2C 2D 2E 2F 30 31 32 33 34 35 36 37 38 39 3A 3B 3C 3D 3E 3F 40"

    translate = dict(zip(simbs, hex_val.split()))

    hexnum = '0123456789abcdef'
    s_blocks = [
    	[1,7,14,13,0,5,8,3,4,15,10,6,9,12,11,2], 
        [8,14,2,5,6,9,1,12,15,4,11,0,13,10,3,7], 
        [5,13,15,6,9,2,12,10,11,7,8,1,4,3,14,0], 
        [7,15,5,10,8,1,6,13,0,9,3,14,11,4,2,12], 
        [12,8,2,1,13,4,15,6,7,0,10,5,3,14,9,11], 
        [11,3,5,8,2,15,10,13,14,1,7,4,12,9,6,0], 
        [6,8,2,3,9,10,5,12,1,14,4,7,11,13,0,15], 
        [12,4,6,2,10,5,11,9,14,8,13,7,0,3,15,1]]

    def func_t(text):
        res = ''
        for i in range(len(text)):
           ind = hexnum.index(text[i])
           res += hexnum[s_blocks[i][ind]]
        return res

    def func_t_decrypt(text):
        res = ''
        for i in range(len(text)):
           ind = hexnum.index(text[i])
        #    print(s_blocks[7-i])
           res += hexnum[s_blocks[i].index(ind)]
        return res 
    text = input("Введите текст для работы: ")
    res_enc = func_t(text)
    res_decr = func_t_decrypt(res_enc)
    print(res_enc)
    print(res_decr)
    # print(translate["щ"])
    #fdb97531
elif choice == 6:
    def cypr(opentext,alp):
        result = ""
        n=len(alp) #Длина алфавита
        for j in range(0,len(opentext)):
            i=alp.find(opentext[j])
            Y=(i+j)%n #индекс буквы
            result+=alp[Y]
        return result
    def tritemiy_decypr(result,alp):
        decypr= ""
        n = len(alp)
        for j in range(0, len(result)):
            i = alp.find(result[j])
            Y = (i - j) % n #  индекс буквы
            decypr += alp[Y]
        return decypr

    task = int(input("Введите тип текста (1- поговорка, 2 - текст 1000 символов) "))
    if task == 1:
        alp = "абвгдежзийклмнопрстуфхцчшщъыьэюя"
        text = input("Введите текст для работы алгоритма: ")
        text = text.replace('.', "тчк").replace(',', "зпт").replace(" ", "").lower()
        cypr=cypr(text,alp)
        print(cypr)
        decypr=tritemiy_decypr(cypr,alp)
        print(decypr)
        # err=caesar(1,text,card_alp,card_alp_len) Ввел в качестве ключа длинну алфавита для проверки на ошибку
    elif task == 2:
        alp = "абвгдежзийклмнопрстуфхцчшщъыьэюя" + "абвгдежзийклмнопрстуфхцчшщъыьэюя".upper() + ".,-!?– "

        text = input("Введите текст: ")
        cypr = cypr(text,alp)
        decypr = tritemiy_decypr(cypr,alp)
        n = 500
        print("Результат шифрования")
        for i in range(0, len(cypr), n):
            print(cypr[i:i + n])
        print()
        print("Результат расшифрования")
        for i in range(0, len(decypr), n):
            print(decypr[i:i + n])
elif choice == 7:
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
    if len(key) > 1:
        key = key[0]
        print("В качестве ключа установлена буква "+ key)
    print('Результат: \n')
    print(crypt(open_text, mode, key))
elif choice == 8:
    import numpy as np

    def multi_matr(matr, vector):
        #В случае, если последний блок не полный, заполняем нулями
        if len(vector) == 1:
            vector.append(0)
            vector.append(0)
        elif len(vector) == 2:
            vector.append(0)
        res = []
        for i in matr:
            a = 0
            for j in range(len(i)):
                a += i[j] * vector[j]
            res.append(a)
        return(res)

    def inv_matr(matr):
        try:
            # Преобразование двумерного списка в массив numpy
            numpy_matrix = np.array(matr)

            # Нахождение обратной матрицы
            inverse = np.linalg.inv(numpy_matrix)

            return inverse.tolist()  # Преобразование обратной матрицы обратно в двумерный список
        except np.linalg.LinAlgError:
            # Если матрица вырожденная, обратной матрицы не существует
            return "Матрица вырожденная, обратной матрицы не существует"

    def crypt(text,  matr):
        blocks = []
        res = []
        nums = []

        for i in text:
            #Переводим буквы в их номера в алфавите
            nums.append(alp.index(i)+1)
        for i in range(0, len(text), size):
            #Делим на блоки, равные по длине размеру матрицы
            blocks.append(nums[i:i+size])
        for i in blocks:
            new_vector = multi_matr(matr, i)
            #получем новый вектор и добавляем его значения к результирующему массиву
            for j in new_vector:
                res.append(j)
                # print(j)
        return res

    def decrypt(text, matr):
        new_matr = inv_matr(matr)
        res = [] #массив для хранения результата в виде чисел
        blocks = []
        otv = "" #результат в виду символов
        for i in range(0, len(text), size):
            blocks.append(text[i:i+size])
        for i in blocks:
            new_vector = multi_matr(new_matr, i)
            for j in new_vector:
                res.append(int(j+0.5))
                # print(j)
        for i in res:
            otv += alp[i-1]
        return otv
    matr = []
    while True:
        size = int(input("Введите размер КВАДРАТНОЙ матрицы: "))
        for i in range(size):
            l = list(map(int, input(f'Введите {i+1} строку матрицы: ').split()))
            if len(l) != size:
                print("Неверный ввод!")
            else:
                matr.append(l)

        if type(inv_matr(matr)) == str:
            print("Неверная матрица")
            matr = []
        else:
            break

    task = int(input("Выберите режим (1- карточка, 2 - текст > 1000 символов):"))
    if task == 1:
        alp = 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
    elif task == 2:
        alp = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ #!^*()?-–+.,:;абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    text = input("Введите текст: ")
    ciphertext = crypt(text,  matr)
    print("".join(list(map(str, ciphertext))))
    print(decrypt(ciphertext, matr))
    # print(inv_matr(matr))
elif choice == 9:

    # print(len("АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ @#!%^&*()-+.:;абвгдежзийклмнопрстуфхцчшщъыьэюя"))

    def split_and_adjust(string):
        substrings = []
        i = 0
        while i < len(string):
            if i == len(string) - 1:
                substrings.append([string[i], ""])  # Добавляем последний символ как подстроку
                break
            if string[i] == string[i+1]:  # Проверяем на повторение символов
                substrings.append([string[i], "Ф"])  # Если повторяется, заменяем второй символ
                i += 1  # Переходим к следующему символу
            else:
                substrings.append([string[i], string[i+1]])  # Если нет повторения, добавляем оба символа
                i += 2  # Переходим к следующей паре символов
        if substrings[-1][1] == "":
            substrings[-1][1] = "Я"
        return substrings

    def crypt(text, mode, task, table):
        res = ''
        #определяем размер таблицы
        if task == 1:
            size = 6
        elif task == 2:
            size = 9
        #делим строку на пары
        open_text = split_and_adjust(text)
        # print(open_text)
        if mode == 1:
            for i in open_text:
                a = table.index(i[0])
                b = table.index(i[1])
                strokA, strokB = a//size, b//size
                # print(a, strokA, b, strokB)
                #Случай, если буквы в одной строке
                if strokA == strokB:
                    res += table[(a+1)%size + size*strokA]
                    res += table[(b+1)%size + size*strokA]
                #Если буквы в одном столбце
                elif a%size == b%size:
                    res += table[(a+size)%(len(table))]
                    res += table[(b+size)%(len(table))]
                #Если буквы в разных строках и разных столбцах
                else:
                    str_a, col_a = strokA, a%size
                    str_b, col_b = strokB, b%size
                    res += table[str_a*size + col_b]
                    res += table[str_b*size + col_a]
        elif mode == 2:
            for i in open_text:
                a = table.index(i[0])
                b = table.index(i[1])
                strokA, strokB = a//size, b//size
                # print(a, strokA, b, strokB)
                #Случай, если буквы в одной строке
                if strokA == strokB:
                    res += table[(a-1)%size + size*strokA]
                    res += table[(b-1)%size + size*strokA]
                #Если буквы в одном столбце
                elif a%size == b%size:
                    res += table[(a-size)%(len(table))]
                    res += table[(b-size)%(len(table))]
                #Если буквы в разных строках и разных столбцах
                else:
                    str_a, col_a = strokA, a%size
                    str_b, col_b = strokB, b%size
                    res += table[str_a*size + col_b]
                    res += table[str_b*size + col_a]
            i = 1
            while i < len(res) - 1:
                if res[i-1] == res[i+1] and res[i] == 'Ф':
                    res = res[:i] + res[i+1:]
                else:
                    i += 1
            res = res[:-1]
        return res


    mode = int(input("Выберите режим (1 - шифрование; 2 - расшифрование): "))
    task = int(input("Работа с карточкой - 1, работа с большим текстом - 2: "))
    if task == 1:
        big_alphabit = 'АБВГДЕЖЗИКЛМНОПРСТУФХЦЧШЩЫЬЭЮЯ'
    elif task == 2:
        big_alphabit = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ #!^*()?-–+.,:;абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    key = input("Введите ключ:")
    #Проверка ключа
    while True:
        if len(set(key)) == len(list(key)):
            break
        else:
            key = input("Введите в качестве ключа слово, в котором каждая буква встречается 1 раз: ")
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

    # print(table)
    print(crypt(open_text, mode, task, table))
elif choice == 10:
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
elif choice == 11:
    def encode(string: str, key: str):
        len_key = len(key)
        string += ' ' * (len_key - len(string) % len_key)
        matrix = [[] for _ in range(len_key)]#создание матрицы для текста
        for st in range(len(string) // len_key):
            for j, sub_key in enumerate(key):
                matrix[j].append(string[st * (len_key) + int(sub_key) - 1])#записаваем текст в матрицу используя ключ
        # for i in matrix:#Выводит матрицу текста по строкам
        #     print(*i)
        return (''.join(''.join(i) for i in matrix))


    def decode(string: str, key: str):
        len_key = len(key)
        matrix = [['' for _ in range(len_key)] for _ in range(len(string) // len_key)]#создание матрицы для текста
        st = iter(string)
        for sub_key in key:
            for i in range(len(string) // len_key):
                matrix[i][int(sub_key) - 1] = next(st)#записаваем текст в матрицу используя ключ
        # for i in matrix:#Выводит матрицу текста по строкам
        #     # print(*i)
        return (''.join(''.join(i) for i in matrix))

    # string = input()
    # key = input()
    # string = encode(string, key)
    # print(string)
    # print()
    # print(decode(string, key))

    flag=True
    while flag:
        keyarr=list(input("Введите ключ "))
        count=1
        ordarr=[]
        max_ind=0#Преобразование слова в числовой ключ
        for i in range(len(keyarr)):
            ordarr.append(ord(keyarr[i]))
            keyarr[i]=str(ord(keyarr[i]))
        ordarr.sort()
        key=[""]*len(keyarr)
        ordarr=[str(x) for x in ordarr]
        for i in ordarr:
            ind=keyarr.index(i)
            keyarr[ind]=0
            key[ind]=str(count)
            count += 1
        key=''.join(key)
        print(key)
    #декабрь
    #3451267
        type=int(input("Введите тип текста (1- поговорка, 2 - текст 1000 символов) "))
        if type==1:
            alphabet = "абвгдежзийклмнопрстуфхцчшщъыьэюя"
            text = input("Введите текст для шифрования: ")
            text = text.replace('.',"тчк").replace(',',"зпт").replace(" ","").upper()
            cipr=encode(text,key)
            print(cipr.replace(" ",''))
            decipr = decode(cipr,key)
            decipr = decipr.replace("зпт",',').replace("тчк",'.')
            print(decipr)
        elif type == 2:

            text=input("Введите текст: ")
            cipr=encode(text,key)
            decipr = decode(cipr,key)
            n = 150
            for i in range(0, len(cipr), n):
                print(cipr[i:i + n].replace(" ",''))
            print()
            for i in range(0, len(decipr), n):
                print(decipr[i:i + n])
        else:
            print("неправильный тип")
            flag=False
elif choice == 12:
    def GOST_Magma_Add_32(a, b, c):
        internal = 0
        for i in range(3, -1, -1):
            internal = a[i] + b[i] + (internal >> 8)
            c[i] = internal & 0xff

    Pi = [
        [1, 7, 14, 13, 0, 5, 8, 3, 4, 15, 10, 6, 9, 12, 11, 2],
        [8, 14, 2, 5, 6, 9, 1, 12, 15, 4, 11, 0, 13, 10, 3, 7],
        [5, 13, 15, 6, 9, 2, 12, 10, 11, 7, 8, 1, 4, 3, 14, 0],
        [7, 15, 5, 10, 8, 1, 6, 13, 0, 9, 3, 14, 11, 4, 2, 12],
        [12, 8, 2, 1, 13, 4, 15, 6, 7, 0, 10, 5, 3, 14, 9, 11],
        [11, 3, 5, 8, 2, 15, 10, 13, 14, 1, 7, 4, 12, 9, 6, 0],
        [6, 8, 2, 3, 9, 10, 5, 12, 1, 14, 4, 7, 11, 13, 0, 15],
        [12, 4, 6, 2, 10, 5, 11, 9, 14, 8, 13, 7, 0, 3, 15, 1]
    ]

    def GOST_Magma_T(in_data, out_data):
        for i in range(4):
            first_part_byte = (in_data[i] & 0xf0) >> 4
            sec_part_byte = (in_data[i] & 0x0f)
            first_part_byte = Pi[i * 2][first_part_byte]
            sec_part_byte = Pi[i * 2 + 1][sec_part_byte]
            out_data[i] = (first_part_byte << 4) | sec_part_byte

    def GOST_Magma_g(k, a, out_data):
        internal = [0] * 4
        out_data_32 = 0

        GOST_Magma_Add_32(a, k, internal)
        GOST_Magma_T(internal, internal)

        out_data_32 = (internal[0] << 24) + (internal[1] << 16) + (internal[2] << 8) + internal[3]
        out_data_32 = ((out_data_32 << 11) | (out_data_32 >> 21)) & 0xFFFFFFFF

        out_data[3] = out_data_32 & 0xFF
        out_data[2] = (out_data_32 >> 8) & 0xFF
        out_data[1] = (out_data_32 >> 16) & 0xFF
        out_data[0] = (out_data_32 >> 24) & 0xFF

    def GOST_Magma_Add(a, b, c):
        for i in range(len(a)):
            c[i] = a[i] ^ b[i]


    def GOST_Magma_G(k, a, out_data):
        a_0 = [0] * 4  # Правая часть блока
        a_1 = [0] * 4  # Левая часть блока
        G = [0] * 4

        # Разделить 64-битный входной блок на две части
        for i in range(4):
            a_0[i] = a[4 + i]
            a_1[i] = a[i]

        # Применить преобразование g
        GOST_Magma_g(k, a_0, G)

        # Применить XOR результата преобразования g к левой части блока
        GOST_Magma_Add(a_1, G, G)

        for i in range(4):
            # Скопировать значение из правой части в левую часть
            a_1[i] = a_0[i]
            # Скопировать результат сложения в правую часть блока
            a_0[i] = G[i]

        # Объединить правую и левую части в один блок
        for i in range(4):
            out_data[i] = a_1[i]
            out_data[4 + i] = a_0[i]


    def GOST_Magma_G_Fin(k, a, out_data):
        a_0 = [0] * 4  # Правая часть блока
        a_1 = [0] * 4  # Левая часть блока
        G = [0] * 4

        # Разделить 64-битный входной блок на две части
        for i in range(4):
            a_0[i] = a[4 + i]
            a_1[i] = a[i]

        # Применить преобразование g
        GOST_Magma_g(k, a_0, G)

        # Применить XOR результата преобразования g к левой части блока
        GOST_Magma_Add(a_1, G, G)

        # Скопировать результат сложения в левую часть блока
        for i in range(4):
            a_1[i] = G[i]

        # Объединить правую и левую части в один блок
        for i in range(4):
            out_data[i] = a_1[i]
            out_data[4 + i] = a_0[i]


    def GOST_Magma_Encrypt(blk, out_blk):
        # Первое преобразование G
        GOST_Magma_G(iter_key[0], blk, out_blk)

        # Последующие (со второго по тридцать первое) преобразования G
        for i in range(1, 31):
            GOST_Magma_G(iter_key[i], out_blk, out_blk)

        # Последнее (тридцать второе) преобразование G
        GOST_Magma_G_Fin(iter_key[31], out_blk, out_blk)


    def GOST_Magma_Decript(blk, out_blk):
        # Первое преобразование G с использованием
        # тридцать второго итерационного ключа
        GOST_Magma_G(iter_key[31], blk, out_blk)

        # Последующие (со второго по тридцать первое) преобразования G
        # (итерационные ключи идут в обратном порядке)
        for i in range(30, 0, -1):
            GOST_Magma_G(iter_key[i], out_blk, out_blk)

        # Последнее (тридцать второе) преобразование G
        # с использованием первого итерационного ключа
        GOST_Magma_G_Fin(iter_key[0], out_blk, out_blk)

    iter_key = [bytearray(4) for _ in range(32)]  # Инициализация ключевого расписания

    def GOST_Magma_Expand_Key(key):
        # Формирование 8-ми 32-битных подключей
        for i in range(8):
            iter_key[i][:] = key[i * 4: (i + 1) * 4]


        #повторяем прошлый блок ещё 2 раза
        for j in range(2):
            for i in range(8):
                iter_key[8 * (j + 1) + i][:] = key[i * 4: (i + 1) * 4]

        for i in range(8):
            iter_key[-(i+1)][:] = iter_key[i][:]

    # print("Transformation t")
    def t(input_data):
        result = bytearray(4)
        GOST_Magma_T(input_data, result)
        return result

    def add_xor(a,b):
        block_size=8
        c=[""]*block_size
        for i in range(block_size):
            c[i]=a[i]^b[i]
        return c


    # def gamma_cipher(data, key):
    #     size=16
    #     s = bytearray.fromhex("12345678")
    #     s_out = bytearray(8)
    #     GOST_Magma_Encrypt(s, s_out)
    #     print(s_out)
    #     # inc_gamma()
    #     out_data=bytearray(8)
    #     GOST_Magma_Add(s_out, data,out_data)
    #     print(out_data)
    #
    # def xor(block, data):
    #     res = bytearray(8)
    #     for i in range(8):
    #         res[i] = block[i] ^ data[i]
    #     return bytes(res)
    #
    # def inc_gamma():
    #     global s
    #     t = int.from_bytes(s, byteorder='little')
    #     t += 1
    #     s = t.to_bytes(8, byteorder='little')
    #
    # # Пример использования
    # s = b'\x00\x00\x00\x00\x00\x00\x00\x00'  # Начальное значение синхропосылки
    # key = b'your_key_here'
    # data = b'your_data_here'
    # encrypted_data = gamma_cipher(data, key)


    # print(gamma_cipher("92def06b3c130a59",""))
    # Example 1
    input_data_1 = bytearray.fromhex("fdb97531")
    output_1 = t(input_data_1)
    print("t(fdb97531) =", ''.join(format(x, '02x') for x in output_1))

    # Example 2
    input_data_2 = output_1
    output_2 = t(input_data_2)
    print("t(2a196f34) =", ''.join(format(x, '02x') for x in output_2))

    # Example 3
    input_data_3 = output_2
    output_3 = t(input_data_3)
    print("t(ebd9f03a) =", ''.join(format(x, '02x') for x in output_3))

    # Example 4
    input_data_4 = output_3
    output_4 = t(input_data_4)
    print("t(b039bb3d) =", ''.join(format(x, '02x') for x in output_4))


    print("Transformation g")
    # A.2.2 Transformation g
    def g(k, a):
        result = bytearray(4)
        GOST_Magma_g(bytearray.fromhex(k), bytearray.fromhex(a), result)
        return result

    # Example 1
    output_g_1 = g("87654321", "fedcba98")
    print("g[87654321](fedcba98) =", ''.join(format(x, '02x') for x in output_g_1))

    # Example 2
    output_g_2 = g("fdcbc20c", "87654321")
    print("g[fdcbc20c](87654321) =", ''.join(format(x, '02x') for x in output_g_2))

    # Example 3
    output_g_3 = g("7e791a4b", "fdcbc20c")
    print("g[7e791a4b](fdcbc20c) =", ''.join(format(x, '02x') for x in output_g_3))

    # Example 4
    output_g_4 = g("c76549ec", "7e791a4b")
    print("g[c76549ec](7e791a4b) =", ''.join(format(x, '02x') for x in output_g_4))


    print("Key Expansion Algorithm")
    # A.2.3 Key Expansion Algorithm
    key_example = bytearray.fromhex("ffeeddccbbaa99887766554433221100f0f1f2f3f4f5f6f7f8f9fafbfcfdfeff")
    GOST_Magma_Expand_Key(key_example)
    print("Key Schedule:", [''.join(format(x, '02x') for x in subkey) for subkey in iter_key])

    # A.2.4 Encryption Algorithm
    def GOST_Magma_Encrypt_Example():
        plaintext = bytearray.fromhex("92def06b3c130a59")
        encrypted_block = bytearray(8)

        GOST_Magma_Encrypt(plaintext, encrypted_block)

        print("Open text:", ''.join(format(x, '02x') for x in plaintext))
        print("Encrypted Block:", ''.join(format(x, '02x') for x in encrypted_block))

    # GOST_Magma_Encrypt_Example()

    def GOST_Magma_Decrypt_Example():
        # Шифртекст для расшифрования
        ciphertext = bytearray.fromhex("2b073f0494f372a0")
        decrypted_block = bytearray(8)

        GOST_Magma_Decript(ciphertext, decrypted_block)

        print("Ciphertext:", ''.join(format(x, '02x') for x in ciphertext))
        print("Decrypted Block:", ''.join(format(x, '02x') for x in decrypted_block))

    # Пример расшифрования
    # GOST_Magma_Decrypt_Example()
elif choice == 13:   
    alp = "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ".lower()
    for_big_text = "АБВГДЕёЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ".lower() + "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"  + " !\"#$%-'()*+,—–./:;<=>?@[\]^_`{|}"
    # print(alp.index("A"))
    def gamma(mes, a, c, T0, mode):
        if mode == 1:
            alp_arr = []
            for i in mes.lower():

                alp_arr.append(alp.index(i))
            arr = [T0]
            for i in range(len(mes)):
                t = (a*arr[-1]+c) % 32
                arr.append(t)
            arr.pop(0)

            return arr, alp_arr
        else:
            alp_arr = []
            for i in mes:
                alp_arr.append(for_big_text.index(i)+1)
            arr = [T0]
            for i in range(len(mes)):
                t = (a*arr[-1]+c) % 98
                arr.append(t)
            arr.pop(0)
            return arr, alp_arr

    def encrypt(message, one_time_pad, mode):
        if mode == 1:
            arr = []
            for i in range(len(message)):
                arr.append((message[i]+one_time_pad[i]) % 32)
            print(arr)
            return "".join([alp[i] for i in arr])
        else:
            arr = []
            for i in range(len(message)):
                arr.append((message[i]+one_time_pad[i]) % 98)
            print(arr)
            return "".join([for_big_text[i] for i in arr])
    def decrypt(ciphertext, one_time_pad, mode):
        if mode == 1:
            arr = []
            for i in range(len(ciphertext)):
                shift = (alp.index(ciphertext[i])-one_time_pad[i]+1) % 32 
                arr.append(shift)
            return "".join([alp[i-1] for i in arr])  
        else:
            arr = []
            for i in range(len(ciphertext)):
                shift = (for_big_text.index(ciphertext[i])-one_time_pad[i]) % 98
                arr.append(shift)
            return "".join([for_big_text[i-1] for i in arr])  

    from math import gcd

    mode = int(input("Выберите задание (1 - карточка, 2 - текст): "))
    a = int(input("a = "))
    if mode == 1:
        check = 32
    else:
        check = 99

    if a%2 != 0 and a%4 == 1 and a > 1:
        x = 32 if mode == 1 else 98
        c = int(input("c = "))
        if gcd(c, x) == 1:
            T0 = int(input("T0 = "))
            if 0<T0<check:
                # message = "отодногопорченогояблокавесьвоззагниваеттчк"
                message = str(input("Введите текст: "))

                one_time_pad, msg = gamma(message, a, c, T0 , mode)
                ciphertext = encrypt(msg, one_time_pad, mode)
                print("Зашифрованный текст:", ciphertext)

                decrypted_message = decrypt(ciphertext, one_time_pad, mode)
                print("Дешифрованный текст:", decrypted_message)
        else:
            print("c не взаимно прост с модулем m")
    else:
        print("неверные значения. a должно быть нечётным, больше 1 и меньше 32; T0 должно быть больше 1 и меньше мощности алфавита") 
elif choice == 14:
    def GOST_Magma_Add_32(a, b, c):
        internal = 0
        for i in range(3, -1, -1):
            internal = a[i] + b[i] + (internal >> 8)
            c[i] = internal & 0xff

    Pi = [
        [1, 7, 14, 13, 0, 5, 8, 3, 4, 15, 10, 6, 9, 12, 11, 2],
        [8, 14, 2, 5, 6, 9, 1, 12, 15, 4, 11, 0, 13, 10, 3, 7],
        [5, 13, 15, 6, 9, 2, 12, 10, 11, 7, 8, 1, 4, 3, 14, 0],
        [7, 15, 5, 10, 8, 1, 6, 13, 0, 9, 3, 14, 11, 4, 2, 12],
        [12, 8, 2, 1, 13, 4, 15, 6, 7, 0, 10, 5, 3, 14, 9, 11],
        [11, 3, 5, 8, 2, 15, 10, 13, 14, 1, 7, 4, 12, 9, 6, 0],
        [6, 8, 2, 3, 9, 10, 5, 12, 1, 14, 4, 7, 11, 13, 0, 15],
        [12, 4, 6, 2, 10, 5, 11, 9, 14, 8, 13, 7, 0, 3, 15, 1]
    ]

    def GOST_Magma_T(in_data, out_data):
        for i in range(4):
            first_part_byte = (in_data[i] & 0xf0) >> 4
            sec_part_byte = (in_data[i] & 0x0f)
            first_part_byte = Pi[i * 2][first_part_byte]
            sec_part_byte = Pi[i * 2 + 1][sec_part_byte]
            out_data[i] = (first_part_byte << 4) | sec_part_byte

    def GOST_Magma_g(k, a, out_data):
        internal = [0] * 4
        out_data_32 = 0

        GOST_Magma_Add_32(a, k, internal)
        GOST_Magma_T(internal, internal)

        out_data_32 = (internal[0] << 24) + (internal[1] << 16) + (internal[2] << 8) + internal[3]
        out_data_32 = ((out_data_32 << 11) | (out_data_32 >> 21)) & 0xFFFFFFFF

        out_data[3] = out_data_32 & 0xFF
        out_data[2] = (out_data_32 >> 8) & 0xFF
        out_data[1] = (out_data_32 >> 16) & 0xFF
        out_data[0] = (out_data_32 >> 24) & 0xFF

    def GOST_Magma_Add(a, b, c):
        for i in range(len(a)):
            c[i] = a[i] ^ b[i]


    def GOST_Magma_G(k, a, out_data):
        a_0 = [0] * 4  # Правая часть блока
        a_1 = [0] * 4  # Левая часть блока
        G = [0] * 4

        # Разделить 64-битный входной блок на две части
        for i in range(4):
            a_0[i] = a[4 + i]
            a_1[i] = a[i]

        # Применить преобразование g
        GOST_Magma_g(k, a_0, G)

        # Применить XOR результата преобразования g к левой части блока
        GOST_Magma_Add(a_1, G, G)

        for i in range(4):
            # Скопировать значение из правой части в левую часть
            a_1[i] = a_0[i]
            # Скопировать результат сложения в правую часть блока
            a_0[i] = G[i]

        # Объединить правую и левую части в один блок
        for i in range(4):
            out_data[i] = a_1[i]
            out_data[4 + i] = a_0[i]


    def GOST_Magma_G_Fin(k, a, out_data):
        a_0 = [0] * 4  # Правая часть блока
        a_1 = [0] * 4  # Левая часть блока
        G = [0] * 4

        # Разделить 64-битный входной блок на две части
        for i in range(4):
            a_0[i] = a[4 + i]
            a_1[i] = a[i]

        # Применить преобразование g
        GOST_Magma_g(k, a_0, G)

        # Применить XOR результата преобразования g к левой части блока
        GOST_Magma_Add(a_1, G, G)

        # Скопировать результат сложения в левую часть блока
        for i in range(4):
            a_1[i] = G[i]

        # Объединить правую и левую части в один блок
        for i in range(4):
            out_data[i] = a_1[i]
            out_data[4 + i] = a_0[i]


    def GOST_Magma_Encrypt(blk, out_blk):
        # Первое преобразование G
        GOST_Magma_G(iter_key[0], blk, out_blk)

        # Последующие (со второго по тридцать первое) преобразования G
        for i in range(1, 31):
            GOST_Magma_G(iter_key[i], out_blk, out_blk)

        # Последнее (тридцать второе) преобразование G
        GOST_Magma_G_Fin(iter_key[31], out_blk, out_blk)


    def GOST_Magma_Decript(blk, out_blk):
        # Первое преобразование G с использованием
        # тридцать второго итерационного ключа
        GOST_Magma_G(iter_key[31], blk, out_blk)

        # Последующие (со второго по тридцать первое) преобразования G
        # (итерационные ключи идут в обратном порядке)
        for i in range(30, 0, -1):
            GOST_Magma_G(iter_key[i], out_blk, out_blk)

        # Последнее (тридцать второе) преобразование G
        # с использованием первого итерационного ключа
        GOST_Magma_G_Fin(iter_key[0], out_blk, out_blk)

    iter_key = [bytearray(4) for _ in range(32)]  # Инициализация ключевого расписания

    def GOST_Magma_Expand_Key(key):
        # Формирование 8-ми 32-битных подключей
        for i in range(8):
            iter_key[i][:] = key[i * 4: (i + 1) * 4]

        #повторяем прошлый блок ещё 2 раза
        for j in range(2):
            for i in range(8):
                iter_key[8 * (j + 1) + i][:] = key[i * 4: (i + 1) * 4]

        for i in range(8):
            iter_key[-(i+1)][:] = iter_key[i][:]

    # print("Transformation t")
    def t(input_data):
        result = bytearray(4)
        GOST_Magma_T(input_data, result)
        return result

    def add_xor(a,b):
        block_size=8
        c=[""]*block_size
        for i in range(block_size):
            c[i]=a[i]^b[i]
        return c


    # def gamma_cipher(data, key):
    #     size=16
    #     s = bytearray.fromhex("12345678")
    #     s_out = bytearray(8)
    #     GOST_Magma_Encrypt(s, s_out)
    #     print(s_out)
    #     # inc_gamma()
    #     out_data=bytearray(8)
    #     GOST_Magma_Add(s_out, data,out_data)
    #     print(out_data)
    #
    # def xor(block, data):
    #     res = bytearray(8)
    #     for i in range(8):
    #         res[i] = block[i] ^ data[i]
    #     return bytes(res)
    #
    # def inc_gamma():
    #     global s
    #     t = int.from_bytes(s, byteorder='little')
    #     t += 1
    #     s = t.to_bytes(8, byteorder='little')
    #
    # # Пример использования
    # s = b'\x00\x00\x00\x00\x00\x00\x00\x00'  # Начальное значение синхропосылки
    # key = b'your_key_here'
    # data = b'your_data_here'
    # encrypted_data = gamma_cipher(data, key)


    # print(gamma_cipher("92def06b3c130a59",""))
    # Example 1
    # input_data_1 = bytearray.fromhex("fdb97531")
    # output_1 = t(input_data_1)
    # print("t(fdb97531) =", ''.join(format(x, '02x') for x in output_1))

    # # Example 2
    # input_data_2 = output_1
    # output_2 = t(input_data_2)
    # print("t(2a196f34) =", ''.join(format(x, '02x') for x in output_2))

    # # Example 3
    # input_data_3 = output_2
    # output_3 = t(input_data_3)
    # print("t(ebd9f03a) =", ''.join(format(x, '02x') for x in output_3))

    # # Example 4
    # input_data_4 = output_3
    # output_4 = t(input_data_4)
    # print("t(b039bb3d) =", ''.join(format(x, '02x') for x in output_4))


    # print("Transformation g")
    # A.2.2 Transformation g
    def g(k, a):
        result = bytearray(4)
        GOST_Magma_g(bytearray.fromhex(k), bytearray.fromhex(a), result)
        return result

    # # Example 1
    # output_g_1 = g("87654321", "fedcba98")
    # print("g[87654321](fedcba98) =", ''.join(format(x, '02x') for x in output_g_1))

    # # Example 2
    # output_g_2 = g("fdcbc20c", "87654321")
    # print("g[fdcbc20c](87654321) =", ''.join(format(x, '02x') for x in output_g_2))

    # # Example 3
    # output_g_3 = g("7e791a4b", "fdcbc20c")
    # print("g[7e791a4b](fdcbc20c) =", ''.join(format(x, '02x') for x in output_g_3))

    # # Example 4
    # output_g_4 = g("c76549ec", "7e791a4b")
    # print("g[c76549ec](7e791a4b) =", ''.join(format(x, '02x') for x in output_g_4))


    print("Key Expansion Algorithm")
    # A.2.3 Key Expansion Algorithm
    key_example = bytearray.fromhex("ffeeddccbbaa99887766554433221100f0f1f2f3f4f5f6f7f8f9fafbfcfdfeff")
    GOST_Magma_Expand_Key(key_example)
    print("Key Schedule:", [''.join(format(x, '02x') for x in subkey) for subkey in iter_key])

    # A.2.4 Encryption Algorithm
    def GOST_Magma_Encrypt_Example():
        plaintext = bytearray.fromhex("1234567800000000")
        encrypted_block = bytearray(8)

        GOST_Magma_Encrypt(plaintext, encrypted_block)

        print("Plaintext:", ''.join(format(x, '02x') for x in plaintext))
        print("Encrypted Block:", ''.join(format(x, '02x') for x in encrypted_block))

    GOST_Magma_Encrypt_Example()

    def GOST_Magma_Decrypt_Example():
        # Шифртекст для расшифрования
        ciphertext = bytearray.fromhex("4ee901e5c2d8ca3d")
        decrypted_block = bytearray(8)

        GOST_Magma_Decript(ciphertext, decrypted_block)

        print("Ciphertext:", ''.join(format(x, '02x') for x in ciphertext))
        print("Decrypted Block:", ''.join(format(x, '02x') for x in decrypted_block))

    # Пример расшифрования
    GOST_Magma_Decrypt_Example()

    def GOST_Magma_gamma_Example():
        print("Шифрование гаммированием")
        open_texts=['92def06b3c130a59','db54c704f8189d20','4a98fb2e67a8024c','8912409b17b57e41']

        # Инициализирующий вектор
        initialize_IV = 1234567800000000
        for i in range(4):
            initialize_vector = bytearray.fromhex(str(initialize_IV))
            gamma = bytearray(8)
            text=bytearray.fromhex(open_texts[i])
            GOST_Magma_Encrypt(initialize_vector, gamma)
            cipr_text=bytearray(8)
            GOST_Magma_Add(text,gamma,cipr_text)
            print(f"IV= {initialize_IV} Гамма = {''.join(format(x, '02x') for x in gamma)} Открытый текст: {''.join(format(x, '02x') for x in text)}")
            print("Результат: ", ''.join(format(x, '02x') for x in cipr_text))
            initialize_IV += 1
    # Пример шифрование гаммированием
    GOST_Magma_gamma_Example()

    def GOST_Magma_decipr_gamma_Example():
        print("Расшифрование гаммированием")
        cipred_texts = ['4e98110c97b7b93c', '3e250d93d6e85d69', '136d868807b2dbef', '568eb680ab52a12d']
        # Инициализирующий вектор
        initialize_IV = 1234567800000000
        for i in range(4):
            initialize_vector = bytearray.fromhex(str(initialize_IV))
            gamma = bytearray(8)
            text = bytearray.fromhex(cipred_texts[i])
            GOST_Magma_Encrypt(initialize_vector, gamma)
            open_text = bytearray(8)
            GOST_Magma_Add(text, gamma, open_text)
            print(f"IV= {initialize_IV} Гамма = {''.join(format(x, '02x') for x in gamma)} Открытый текст: {''.join(format(x, '02x') for x in text)}")
            print("Результат: ", ''.join(format(x, '02x') for x in open_text))
            initialize_IV += 1
    # Пример расшифрования гаммированием
    GOST_Magma_decipr_gamma_Example()
elif choice == 15:
    # from bit import BitArray
    import re
    for_big_text = "АБВГДЕёЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ".lower() + "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"  + " !\"#$%-'()*+,—–./:;<=>?@[\]^_`{|}"

    mode = int(input("выберите режим (1 - карточка, 2 - большой текст): "))

    if mode == 1:
        text = input("Введите текст: ").upper()
    else:
        text = input("Введите текст: ")
    text_reg = ''
    for i in text:
        c = str(bin(for_big_text.find(i)+1))[2:]
        while len(c) != 8: c = '0' + c
        text_reg += c
    key = [1] * 64
    print(text_reg)

    x = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    y = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    z = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    gamma = ''

    def F(x, y, z):
        return (x & y) or (x & z) or (y & z)

    for i in range(64):
        x.append(x[1] ^ x[2] ^ x[5] ^ x.pop(0) ^ key[i])
        y.append(y[1] ^ y.pop(0) ^ key[i])
        z.append(z[1] ^ z[2] ^ z[15] ^ z.pop(0) ^ key[i])
        # print(*x)
        # print(*y)
        # print(*z)
        # print("------------------------------------------")


    for i in range(100):
        f = F(x[10], y[11], z[12])
        if x[10] == f:
            x.append(x[1] ^ x[2] ^ x[5] ^ x.pop(0))
        if y[11] == f:
            y.append(y[1] ^ y.pop(0))
        if z[12] == f:
            z.append(z[1] ^ z[2] ^ z[15] ^ z.pop(0))

    for i in range(114):
        gamma += str(x[0] ^ y[0] ^ z[0])
        f = F(x[10], y[11], z[12])
        if x[10] == f:
            x.append(x[1] ^ x[2] ^ x[5] ^ x.pop(0))
        if y[11] == f:
            y.append(y[1] ^ y.pop(0))
        if z[12] == f:
            z.append(z[1] ^ z[2] ^ z[15] ^ z.pop(0)) 
    print(x, y, z)
    print("gamma:" + gamma)

    gamma = gamma*500
    text_enc = ''
    for i in range(len(text_reg)):
        text_enc += str(int(text_reg[i]) ^ int(gamma[i]))
    text_dec = ''
    text_dec_res = ''
    for i in range(len(text_enc)):
        text_dec += str(int(text_enc[i]) ^ int(gamma[i]))
    text_dec_sub = re.findall(".{8}", text_dec)
    # print(text_dec_sub)
    for i in text_dec_sub:
        text_dec_res += for_big_text[int(i, 2)-1]
    print(text_enc)
    print(text_dec_res)
elif choice == 16:
    # from bit import BitArray
    import re
    for_big_text = "АБВГДЕёЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ".lower() + "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"  + " !\"#$%-'()*+,—–./:;<=>?@[\]^_`{|}"

    mode = int(input("выберите режим (1 - карточка, 2 - большой текст): "))

    if mode == 1:
        text = input("Введите текст: ").upper()
    else:
        text = input("Введите текст: ")
    text_reg = ''
    for i in text:
        c = str(bin(for_big_text.find(i)+1))[2:]
        while len(c) != 8: c = '0' + c
        text_reg += c
    key = [1] * 64
    print(text_reg)


    x = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    y = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    z = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    r4 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    gamma = ''

    def F(x, y, z):
        return (x & y) or (x & z) or (y & z)

    for i in range(64):
        x.append(x[1] ^ x[2] ^ x[5] ^ x.pop(0) ^ key[i])
        y.append(y[1] ^ y.pop(0) ^ key[i])
        z.append(z[1] ^ z[2] ^ z[15] ^ z.pop(0) ^ key[i])
        r4.append(r4[5] ^ key[i] ^ r4.pop(0))
        # print(*x)
        # print(*y)
        # print(*z)
        # print("------------------------------------------")
    r4[6], r4[9], r4[13] = 1, 1, 1

    for i in range(99):
        f = F(r4[6], r4[9], r4[13])
        if r4[6] == f:
            x.append(x[1] ^ x[2] ^ x[5] ^ x.pop(0))
        if r4[9] == f:
            y.append(y[1] ^ y.pop(0))
        if r4[13] == f:
            z.append(z[1] ^ z[2] ^ z[15] ^ z.pop(0))
        r4.append(r4[5] ^ r4.pop(0))

    for i in range(114):
        f1 = F(x[3], x[4], x[6])
        f2 = F(y[6], y[9], y[13])
        f3 = F(z[4], z[6], z[9])
        gamma += str(x[0] ^ y[0] ^ z[0] ^ f1 ^ f2 ^ f3)
        f = F(r4[6], r4[9], r4[13])
        if r4[6] == f:
            x.append(x[1] ^ x[2] ^ x[5] ^ x.pop(0))
        if r4[9] == f:
            y.append(y[1] ^ y.pop(0))
        if r4[13] == f:
            z.append(z[1] ^ z[2] ^ z[15] ^ z.pop(0))
        r4.append(r4[5] ^ r4.pop(0))
    # for i in r4:
    #     print(i)
    print("gamma:"+ gamma)
    # for i in gamma:
    #     print(i)


    gamma = gamma*500
    text_enc = ''
    for i in range(len(text_reg)):
        text_enc += str(int(text_reg[i]) ^ int(gamma[i]))
    text_dec = ''
    text_dec_res = ''
    for i in range(len(text_enc)):
        text_dec += str(int(text_enc[i]) ^ int(gamma[i]))
    text_dec_sub = re.findall(".{8}", text_dec)
    # print(text_dec_sub)
    for i in text_dec_sub:
        text_dec_res += for_big_text[int(i, 2)-1]
    print(text_enc)
    print(text_dec_res)
    # for i in text_enc:
    #     print(i)
elif choice == 17:
    import pickle
    import binascii
    text = input("Введите текст: ")
    count = 0
    while len(text) % 16 != 0:
        text += "Я"
        count += 1
    ### Кузнечик ###
    class kuznechik:
        def __init__(self, key):
            self.pi = (252, 238, 221, 17, 207, 110, 49, 22, 251, 196, 250, 218, 35, 197, 4, 77, 233, 119, 240, 219, 147, 46,
                       153, 186, 23, 54, 241, 187, 20, 205, 95, 193, 249, 24, 101, 90, 226, 92, 239, 33, 129, 28, 60, 66,
                       139, 1, 142, 79, 5, 132, 2, 174, 227, 106, 143, 160, 6, 11, 237, 152, 127, 212, 211, 31, 235, 52, 44,
                       81, 234, 200, 72, 171, 242, 42, 104, 162, 253, 58, 206, 204, 181, 112, 14, 86, 8, 12, 118, 18, 191,
                       114, 19, 71, 156, 183, 93, 135, 21, 161, 150, 41, 16, 123, 154, 199, 243, 145, 120, 111, 157, 158,
                       178, 177, 50, 117, 25, 61, 255, 53, 138, 126, 109, 84, 198, 128, 195, 189, 13, 87, 223, 245, 36, 169,
                       62, 168, 67, 201, 215, 121, 214, 246, 124, 34, 185, 3, 224, 15, 236, 222, 122, 148, 176, 188, 220,
                       232, 40, 80, 78, 51, 10, 74, 167, 151, 96, 115, 30, 0, 98, 68, 26, 184, 56, 130, 100, 159, 38, 65,
                       173, 69, 70, 146, 39, 94, 85, 47, 140, 163, 165, 125, 105, 213, 149, 59, 7, 88, 179, 64, 134, 172,
                       29, 247, 48, 55, 107, 228, 136, 217, 231, 137, 225, 27, 131, 73, 76, 63, 248, 254, 141, 83, 170, 144,
                       202, 216, 133, 97, 32, 113, 103, 164, 45, 43, 9, 91, 203, 155, 37, 208, 190, 229, 108, 82, 89, 166,
                       116, 210, 230, 244, 180, 192, 209, 102, 175, 194, 57, 75, 99, 182)
            self.piinv = (165, 45, 50, 143, 14, 48, 56, 192, 84, 230, 158, 57, 85, 126, 82, 145, 100, 3, 87, 90, 28, 96, 7,
                          24, 33, 114, 168, 209, 41, 198, 164, 63, 224, 39, 141, 12, 130, 234, 174, 180, 154, 99, 73, 229,
                          66, 228, 21, 183, 200, 6, 112, 157, 65, 117, 25, 201, 170, 252, 77, 191, 42, 115, 132, 213, 195,
                          175, 43, 134, 167, 177, 178, 91, 70, 211, 159, 253, 212, 15, 156, 47, 155, 67, 239, 217, 121, 182,
                          83, 127, 193, 240, 35, 231, 37, 94, 181, 30, 162, 223, 166, 254, 172, 34, 249, 226, 74, 188, 53,
                          202, 238, 120, 5, 107, 81, 225, 89, 163, 242, 113, 86, 17, 106, 137, 148, 101, 140, 187, 119, 60,
                          123, 40, 171, 210, 49, 222, 196, 95, 204, 207, 118, 44, 184, 216, 46, 54, 219, 105, 179, 20, 149,
                          190, 98, 161, 59, 22, 102, 233, 92, 108, 109, 173, 55, 97, 75, 185, 227, 186, 241, 160, 133, 131,
                          218, 71, 197, 176, 51, 250, 150, 111, 110, 194, 246, 80, 255, 93, 169, 142, 23, 27, 151, 125, 236,
                          88, 247, 31, 251, 124, 9, 13, 122, 103, 69, 135, 220, 232, 79, 29, 78, 4, 235, 248, 243, 62, 61,
                          189, 138, 136, 221, 205, 11, 19, 152, 2, 147, 128, 144, 208, 36, 52, 203, 237, 244, 206, 153, 16,
                          68, 64, 146, 58, 1, 38, 18, 26, 72, 104, 245, 129, 139, 199, 214, 32, 10, 8, 0, 76, 215, 116)
            # Предварительно вычисленная таблица с результатами умножения в поле x^8 + x^7 + x^6 + x + 1
            f = open('C:\\Users\\Sergey\\Downloads\\gost_tables', 'rb')
            self.multtable = pickle.load(f)
            f.close()
            # Константы C, использующиеся для ключевого расписания
            self.C = [[110, 162, 118, 114, 108, 72, 122, 184, 93, 39, 189, 16, 221, 132, 148, 1],
                      [220, 135, 236, 228, 216, 144, 244, 179, 186, 78, 185, 32, 121, 203, 235, 2],
                      [178, 37, 154, 150, 180, 216, 142, 11, 231, 105, 4, 48, 164, 79, 127, 3],
                      [123, 205, 27, 11, 115, 227, 43, 165, 183, 156, 177, 64, 242, 85, 21, 4],
                      [21, 111, 109, 121, 31, 171, 81, 29, 234, 187, 12, 80, 47, 209, 129, 5],
                      [167, 74, 247, 239, 171, 115, 223, 22, 13, 210, 8, 96, 139, 158, 254, 6],
                      [201, 232, 129, 157, 199, 59, 165, 174, 80, 245, 181, 112, 86, 26, 106, 7],
                      [246, 89, 54, 22, 230, 5, 86, 137, 173, 251, 161, 128, 39, 170, 42, 8],
                      [152, 251, 64, 100, 138, 77, 44, 49, 240, 220, 28, 144, 250, 46, 190, 9],
                      [42, 222, 218, 242, 62, 149, 162, 58, 23, 181, 24, 160, 94, 97, 193, 10],
                      [68, 124, 172, 128, 82, 221, 216, 130, 74, 146, 165, 176, 131, 229, 85, 11],
                      [141, 148, 45, 29, 149, 230, 125, 44, 26, 103, 16, 192, 213, 255, 63, 12],
                      [227, 54, 91, 111, 249, 174, 7, 148, 71, 64, 173, 208, 8, 123, 171, 13],
                      [81, 19, 193, 249, 77, 118, 137, 159, 160, 41, 169, 224, 172, 52, 212, 14],
                      [63, 177, 183, 139, 33, 62, 243, 39, 253, 14, 20, 240, 113, 176, 64, 15],
                      [47, 178, 108, 44, 15, 10, 172, 209, 153, 53, 129, 195, 78, 151, 84, 16],
                      [65, 16, 26, 94, 99, 66, 214, 105, 196, 18, 60, 211, 147, 19, 192, 17],
                      [243, 53, 128, 200, 215, 154, 88, 98, 35, 123, 56, 227, 55, 92, 191, 18],
                      [157, 151, 246, 186, 187, 210, 34, 218, 126, 92, 133, 243, 234, 216, 43, 19],
                      [84, 127, 119, 39, 124, 233, 135, 116, 46, 169, 48, 131, 188, 194, 65, 20],
                      [58, 221, 1, 85, 16, 161, 253, 204, 115, 142, 141, 147, 97, 70, 213, 21],
                      [136, 248, 155, 195, 164, 121, 115, 199, 148, 231, 137, 163, 197, 9, 170, 22],
                      [230, 90, 237, 177, 200, 49, 9, 127, 201, 192, 52, 179, 24, 141, 62, 23],
                      [217, 235, 90, 58, 233, 15, 250, 88, 52, 206, 32, 67, 105, 61, 126, 24],
                      [183, 73, 44, 72, 133, 71, 128, 224, 105, 233, 157, 83, 180, 185, 234, 25],
                      [5, 108, 182, 222, 49, 159, 14, 235, 142, 128, 153, 99, 16, 246, 149, 26],
                      [107, 206, 192, 172, 93, 215, 116, 83, 211, 167, 36, 115, 205, 114, 1, 27],
                      [162, 38, 65, 49, 154, 236, 209, 253, 131, 82, 145, 3, 155, 104, 107, 28],
                      [204, 132, 55, 67, 246, 164, 171, 69, 222, 117, 44, 19, 70, 236, 255, 29],
                      [126, 161, 173, 213, 66, 124, 37, 78, 57, 28, 40, 35, 226, 163, 128, 30],
                      [16, 3, 219, 167, 46, 52, 95, 246, 100, 59, 149, 51, 63, 39, 20, 31],
                      [94, 167, 216, 88, 30, 20, 155, 97, 241, 106, 193, 69, 156, 237, 168, 32]]
            self.roundkey = [key[:16], key[16:]]
            self.roundkey = self.roundkey + self.keyschedule(self.roundkey)  # Просчёт раундовых ключей

        # Дополнение в поле x^8 + x^7 + x^6 + x + 1
        def add_field(self, x, y):
            return x ^ y

        # Суммирование всех x элементов
        def sum_field(self, x):
            s = 0
            for a in x:
                s ^= a
            return s

        # Умножение в поле
        def mult_field(self, x, y):
            p = 0
            while x:
                if x & 1:
                    p ^= y
                if y & 0x80:
                    y = (y << 1) ^ 0x1C3
                else:
                    y <<= 1
                x >>= 1
            return p

        # XOR двоичных строк x и k
        def xtransformation(self, x, k):
            return [x[i] ^ k[i] for i in range(len(k))]

        # возвращает элемент по счёту x из pi таблицы
        def pitransformation(self, x):
            return self.pi[x]

        ## Обратное преобразование pi
        def piinvtransformation(self, x):
            return self.piinv[x]

        # Замена каждого байта в x соответствующим байтом из таблицы pi
        def stransformation(self, x):
            return [self.pitransformation(x[i]) for i in range(len(x))]

        ## Обратное преобразование s
        def sinvtransformation(self, x):
            return [self.piinvtransformation(i) for i in x]

        # Преобразование списка байтов в однобайтовый с использованием арифметики с конечным полем
        def l(self, x):
            consts = [148, 32, 133, 16, 194, 192, 1, 251, 1, 192, 194, 16, 133, 32, 148, 1]
            multiplication = [self.multtable[x[i]][consts[i]] for i in range(len(x))]
            return self.sum_field(multiplication)

        # R преобразование добавить список байтов с результатом l-преобразования
        def rtransformation(self, x):
            return [self.l(x), ] + x[:-1]

        ## Обратное преобразование R
        def rinvtransformation(self, x):
            return x[1:] + [self.l(x[1:] + [x[0], ]), ]

        # Преобразование L по стандарту
        def ltransformation(self, x):
            for i in range(len(x)):
                x = self.rtransformation(x)
            return x

        ## Обратное преобразование L
        def linvtransformation(self, x):
            for i in range(len(x)):
                x = self.rinvtransformation(x)
            return x

        # преобразование F с использованием ключевого расписания
        def ftransformation(self, k, a):
            tmp = self.xtransformation(k, a[0])
            tmp = self.stransformation(tmp)
            tmp = self.ltransformation(tmp)
            tmp = self.xtransformation(tmp, a[1])
            return [tmp, a[0]]

        # Создание раундового ключа
        def keyschedule(self, roundkey):
            roundkeys = []
            for i in range(4):
                for k in range(8):
                    roundkey = self.ftransformation(self.C[8 * i + k], roundkey)
                roundkeys.append(roundkey[0])
                roundkeys.append(roundkey[1])
            return roundkeys

        def encryption(self, m):
            for i in range(9):
                m = self.xtransformation(m, self.roundkey[i])  # Выполнение XOR текущего значения байт с итерационым ключом
                m = self.stransformation(m)  # Замена байт текущего значения массива по таблице замен
                m = self.ltransformation(m)  # произведение в поле Галуа
            m = self.xtransformation(m, self.roundkey[9])  # Выполнение XOR
            return m

        def decryption(self, c):
            for i in range(9, 0, -1):
                c = self.xtransformation(c, self.roundkey[i])
                c = self.linvtransformation(c)
                c = self.sinvtransformation(c)
            c = self.xtransformation(c, self.roundkey[0])
            return c


    print("Проверка контрольными примерами:")
    k = '8899aabbccddeeff0011223344556677fedcba98765432100123456789abcdef'
    mtest = list(binascii.unhexlify('00112233445566778899aabbcceeff0a'))
    ktest = list(binascii.unhexlify('8899aabbccddeeff0011223344556677fedcba98765432100123456789abcdef'))

    gost = kuznechik(ktest)

    c = gost.encryption(mtest)
    d = gost.decryption(c)

    test1 = binascii.hexlify(bytearray(c)), b'b429912c6e0032f9285452d76718d08b'
    test2 = binascii.hexlify(bytearray(d)), b'00112233445566778899aabbcceeff0a'

    print("Шифрование: 00112233445566778899aabbcceeff0a")
    print("Используемый ключ: ", k)
    print("Результат // Эталон")
    print(test1)
    print("Расшифрование: b429912c6e0032f9285452d76718d08b")
    print("Результат  // Эталон")
    print(test2)


    def ghopper(text):
        temp1, temp2 = [], []

        b = binascii.hexlify(bytes(str.encode(text)))
        test = list(binascii.unhexlify(b))

        for i in range(0, len(test), 16):
            c = gost.encryption(test)
            test = test[16:]
            temp1 += c

        print(" ")
        print("Кузнечик")
        print(binascii.hexlify(bytearray(temp1)))
        print("Ключ:", k)

        for i in range(0, len(temp1), 16):
            d = gost.decryption(temp1)
            d = binascii.hexlify(bytearray(d))  # добавление защифрованного блока к массиву
            d = binascii.unhexlify(d).decode('utf-8')  # декодирование в utf-8
            temp1 = temp1[16:]
            temp2 += d

        decrypt = ""
        decrypt += ''.join(str(e) for e in temp2)
        print(decrypt[:-count])
        return decrypt[:-count]


    ghopper(text)
elif choice == 18:
    def GOST_Magma_Add_32(a, b, c):
        internal = 0
        for i in range(3, -1, -1):
            internal = a[i] + b[i] + (internal >> 8)
            c[i] = internal & 0xff
    Pi = [
        [1, 7, 14, 13, 0, 5, 8, 3, 4, 15, 10, 6, 9, 12, 11, 2],
        [8, 14, 2, 5, 6, 9, 1, 12, 15, 4, 11, 0, 13, 10, 3, 7],
        [5, 13, 15, 6, 9, 2, 12, 10, 11, 7, 8, 1, 4, 3, 14, 0],
        [7, 15, 5, 10, 8, 1, 6, 13, 0, 9, 3, 14, 11, 4, 2, 12],
        [12, 8, 2, 1, 13, 4, 15, 6, 7, 0, 10, 5, 3, 14, 9, 11],
        [11, 3, 5, 8, 2, 15, 10, 13, 14, 1, 7, 4, 12, 9, 6, 0],
        [6, 8, 2, 3, 9, 10, 5, 12, 1, 14, 4, 7, 11, 13, 0, 15],
        [12, 4, 6, 2, 10, 5, 11, 9, 14, 8, 13, 7, 0, 3, 15, 1]
    ]

    def GOST_Magma_T(in_data, out_data):
        for i in range(4):
            first_part_byte = (in_data[i] & 0xf0) >> 4
            sec_part_byte = (in_data[i] & 0x0f)
            first_part_byte = Pi[i * 2][first_part_byte]
            sec_part_byte = Pi[i * 2 + 1][sec_part_byte]
            out_data[i] = (first_part_byte << 4) | sec_part_byte

    def GOST_Magma_g(k, a, out_data):
        internal = [0] * 4
        out_data_32 = 0

        GOST_Magma_Add_32(a, k, internal)
        GOST_Magma_T(internal, internal)

        out_data_32 = (internal[0] << 24) + (internal[1] << 16) + (internal[2] << 8) + internal[3]
        out_data_32 = ((out_data_32 << 11) | (out_data_32 >> 21)) & 0xFFFFFFFF

        out_data[3] = out_data_32 & 0xFF
        out_data[2] = (out_data_32 >> 8) & 0xFF
        out_data[1] = (out_data_32 >> 16) & 0xFF
        out_data[0] = (out_data_32 >> 24) & 0xFF

    def GOST_Magma_Add(a, b, c):
        for i in range(len(a)):
            c[i] = a[i] ^ b[i]


    def GOST_Magma_G(k, a, out_data):
        a_0 = [0] * 4  # Правая часть блока
        a_1 = [0] * 4  # Левая часть блока
        G = [0] * 4

        # Разделить 64-битный входной блок на две части
        for i in range(4):
            a_0[i] = a[4 + i]
            a_1[i] = a[i]

        # Применить преобразование g
        GOST_Magma_g(k, a_0, G)

        # Применить XOR результата преобразования g к левой части блока
        GOST_Magma_Add(a_1, G, G)

        for i in range(4):
            # Скопировать значение из правой части в левую часть
            a_1[i] = a_0[i]
            # Скопировать результат сложения в правую часть блока
            a_0[i] = G[i]

        # Объединить правую и левую части в один блок
        for i in range(4):
            out_data[i] = a_1[i]
            out_data[4 + i] = a_0[i]


    def GOST_Magma_G_Fin(k, a, out_data):
        a_0 = [0] * 4  # Правая часть блока
        a_1 = [0] * 4  # Левая часть блока
        G = [0] * 4

        # Разделить 64-битный входной блок на две части
        for i in range(4):
            a_0[i] = a[4 + i]
            a_1[i] = a[i]

        # Применить преобразование g
        GOST_Magma_g(k, a_0, G)

        # Применить XOR результата преобразования g к левой части блока
        GOST_Magma_Add(a_1, G, G)

        # Скопировать результат сложения в левую часть блока
        for i in range(4):
            a_1[i] = G[i]

        # Объединить правую и левую части в один блок
        for i in range(4):
            out_data[i] = a_1[i]
            out_data[4 + i] = a_0[i]


    def GOST_Magma_Encrypt(blk, out_blk):
        # Первое преобразование G
        GOST_Magma_G(iter_key[0], blk, out_blk)

        # Последующие (со второго по тридцать первое) преобразования G
        for i in range(1, 31):
            GOST_Magma_G(iter_key[i], out_blk, out_blk)

        # Последнее (тридцать второе) преобразование G
        GOST_Magma_G_Fin(iter_key[31], out_blk, out_blk)


    def GOST_Magma_Decript(blk, out_blk):
        # Первое преобразование G с использованием
        # тридцать второго итерационного ключа
        GOST_Magma_G(iter_key[31], blk, out_blk)

        # Последующие (со второго по тридцать первое) преобразования G
        # (итерационные ключи идут в обратном порядке)
        for i in range(30, 0, -1):
            GOST_Magma_G(iter_key[i], out_blk, out_blk)

        # Последнее (тридцать второе) преобразование G
        # с использованием первого итерационного ключа
        GOST_Magma_G_Fin(iter_key[0], out_blk, out_blk)

    iter_key = [bytearray(4) for _ in range(32)]  # Инициализация ключевого расписания

    def GOST_Magma_Expand_Key(key):
        # Формирование 8-ми 32-битных подключей
        for i in range(8):
            iter_key[i][:] = key[i * 4: (i + 1) * 4]


        #повторяем прошлый блок ещё 2 раза
        for j in range(2):
            for i in range(8):
                iter_key[8 * (j + 1) + i][:] = key[i * 4: (i + 1) * 4]

        for i in range(8):
            iter_key[-(i+1)][:] = iter_key[i][:]

    # print("Transformation t")
    def t(input_data):
        result = bytearray(4)
        GOST_Magma_T(input_data, result)
        return result

    def add_xor(a,b):
        block_size=8
        c=[""]*block_size
        for i in range(block_size):
            c[i]=a[i]^b[i]
        return c



    def g(k, a):
        result = bytearray(4)
        GOST_Magma_g(bytearray.fromhex(k), bytearray.fromhex(a), result)
        return result


    key_example = bytearray.fromhex("ffeeddccbbaa99887766554433221100f0f1f2f3f4f5f6f7f8f9fafbfcfdfeff")
    GOST_Magma_Expand_Key(key_example)
    # print("Key Schedule:", [''.join(format(x, '02x') for x in subkey) for subkey in iter_key])

    # A.2.4 Encryption Algorithm
    def GOST_Magma_Encrypt_Example():
        plaintext = bytearray.fromhex("92def06b3c130a59")
        encrypted_block = bytearray(8)

        GOST_Magma_Encrypt(plaintext, encrypted_block)

        print("Open text:", ''.join(format(x, '02x') for x in plaintext))
        print("Encrypted Block:", ''.join(format(x, '02x') for x in encrypted_block))

    GOST_Magma_Encrypt_Example()

    def GOST_Magma_Decrypt_Example():
        # Шифртекст для расшифрования
        ciphertext = bytearray.fromhex("2b073f0494f372a0")
        decrypted_block = bytearray(8)

        GOST_Magma_Decript(ciphertext, decrypted_block)

        print("Ciphertext:", ''.join(format(x, '02x') for x in ciphertext))
        print("Decrypted Block:", ''.join(format(x, '02x') for x in decrypted_block))

    # Пример расшифрования
    GOST_Magma_Decrypt_Example()
elif choice == 19:
    import random
    def pred(s):
        llst = ['а','б','в','г','д','е','ж','з','и','й','к','л','м','н','о','п','р','с','т','у','ф','х','ц','ч','ш','щ','ъ','ы','ь','э','ю','я']
        s = s.lower().replace(' ', '')
        for sim in s:
            if sim not in llst:
                if sim == '.':
                    s = s.replace('.', 'тчк')
                elif sim == ',':
                    s = s.replace(',', 'зпт')
                elif sim == '-':
                    s = s.replace('-', 'тире')
                elif sim == 'ё':
                    s = s.replace('ё', 'е')
                elif sim == '0':
                    s = s.replace('0', 'ноль')
                elif sim == '1':
                    s = s.replace('1', 'один')
                elif sim == '2':
                    s = s.replace('2', 'два')
                elif sim == '3':
                    s = s.replace('3', 'три')
                elif sim == '4':
                    s = s.replace('4', 'четыре')
                elif sim == '5':
                    s = s.replace('5', 'пять')
                elif sim == '1':
                    s = s.replace('6', 'шесть')
                elif sim == '2':
                    s = s.replace('7', 'семь')
                elif sim == '3':
                    s = s.replace('8', 'восемь')
                elif sim == '4':
                    s = s.replace('9', 'девять')
                else:
                    s = s.replace(sim, '')
        return s



    """
             Рассмотрим K = kG, где K и G - точки на эллиптической кривой Ep (a, b), n - порядок G (nG = O∞), а k - целое число меньше n.
             Для заданных k и G легко вычислить K по правилу сложения, но, наоборот, для K и G найти k очень сложно.
             Поскольку при фактическом использовании ECC, в принципе, требуется, чтобы p было достаточно большим, а n также довольно большим, поэтому невозможно вычислить n точек решения по одной в приведенной выше таблице.
             Это математическая основа алгоритма шифрования эллиптической кривой.

             Точка G называется базовой точкой

             k (k <n) - закрытый ключ (частный ключ)

             K - открытый ключ (открытый ключ)
    # """

    def truemod(a):
        flag=False
        for i in range(1,10000):
            if (a*i)%mod==1:
                flag=True
                return i
        if flag==False:
            return 0

    big_alphabit = 'абвгдежзиклмнопрстуфхцчшщъыьэюя'
    # big_alphabit= 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ #!^*()?-–+.,:;абвгдеёжзийклмнопрстуфхцчшщъыьэюя'


    a = 2
    b = 6
    q=17
    # m = 10
    G = (1, 8)
    Cb = 6 # от 1 до q-1
    mod = 32# mod > длина алфавита

    def solve_R(k, g):
        x1, y1 = g[0], g[1]
        x2, y2 = x1, y1

        for i in range(2,k+1):
            if x1 == x2 and y1 == y2:
                lambd = ((3 * (x1 ** 2) + a) % mod * truemod(2 * y1)) % mod
                # if lambd==0:
                #     # print("0")
                #     break
                # else:
                x3 = (lambd ** 2 - 2 * x1) % mod
                y3 = (lambd * (x1 - x3) - y1) % mod
                # print("(" + str(x3) + ";" + str(y3)+")")
                x2 = x3
                y2 = y3
            else:
                lambd = (((y2 - y1) % mod) * truemod(x2 - x1)) % mod
                if x2 - x1 == 0:
                    # print("0")
                    break
                x3 = (lambd ** 2 - x1 - x2) % mod
                y3 = (lambd * (x1 - x3) - y1) % mod
                # print("(" + str(x3) + ";" + str(y3) + ")")
                x2 = x3
                y2 = y3
            # print("k= " + str(i))

        return x2, y2

    s = input("Введите текст: ")
    s=pred(s)
    cypr = []
    m_text=[]
    for i in range(len(s)):
        m=big_alphabit.find(s[i])
        m_text.append(m)
    # print("Входящий текст: ",m_text)
    k_arr=[3,5,7,]
    for i in range(len(s)):
        m=big_alphabit.find(s[i])+1
        # print("m= ",m)
        k=random.randrange(3,15,2)
       #невсетеповаразптчтосдлинныминожамиходяттчк
        # print(solve_R(k,G))
        x1, y1= solve_R (k, G)
        R=[x1,y1]
        # print()
        # print("k= "+str(k))
        # print("R", R)
        x1,y1= solve_R(Cb, G)
        Db=[x1,y1] #Открытый ключ
        # print("Db", Db)
        x1,y1 = solve_R(k, Db)
        P=[x1,y1]
        # print("P",P)
        e = (m * P[0]) % mod
        # print("(R, e)",R, e)
        cypr.append(R)
        cypr.append(e)
    n = 40
    for i in range(0, len(cypr), n):
        print(cypr[i:i + n])



    #расшифрование
    decypr=[]
    for i in range(0,len(cypr),2):
        R=cypr[i]
        e=cypr[i+1]
        xq,yq=solve_R(Cb,R)
        # print(f"x= {xq} y = {yq}")
        m_dec=e*truemod(xq)%mod
        # m_dec-=1
        # print("mdec==",m_dec)
        # decypr.append(m_dec-1)
        decypr.append((m_dec-1)%31)
    res=""
    # print(decypr)
    for i in decypr:
        res+=big_alphabit[i]
    n = 100
    for i in range(0, len(res), n):
        print(res[i:i + n])
elif choice == 20:
    ### Elgamal ###
    def encelga(s, P):
        llst = ['а', 'б', 'в', 'г', 'д', 'е', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф',
                'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']
    def is_prime(n):
        if n <= 1:
            return False
        if n <= 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True

    def pred(s):
        llst = ['а','б','в','г','д','е','ж','з','и','й','к','л','м','н','о','п','р','с','т','у','ф','х','ц','ч','ш','щ','ъ','ы','ь','э','ю','я']
        s = s.lower().replace(' ', '')
        for sim in s:
            if sim not in llst:
                if sim == '.':
                    s = s.replace('.', 'тчк')
                elif sim == ',':
                    s = s.replace(',', 'зпт')
                elif sim == '-':
                    s = s.replace('-', 'тире')
                elif sim == 'ё':
                    s = s.replace('ё', 'е')
                elif sim == '0':
                    s = s.replace('0', 'ноль')
                elif sim == '1':
                    s = s.replace('1', 'один')
                elif sim == '2':
                    s = s.replace('2', 'два')
                elif sim == '3':
                    s = s.replace('3', 'три')
                elif sim == '4':
                    s = s.replace('4', 'четыре')
                elif sim == '5':
                    s = s.replace('5', 'пять')
                elif sim == '1':
                    s = s.replace('6', 'шесть')
                elif sim == '2':
                    s = s.replace('7', 'семь')
                elif sim == '3':
                    s = s.replace('8', 'восемь')
                elif sim == '4':
                    s = s.replace('9', 'девять')
                else:
                    s = s.replace(sim, '')
        return s

    def hesh(str,p,i):
        alp = " АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
        if i==0:
            q=(alp.index(str[i])**2)%p
            return q
        else:
            q=((hesh(str,p,i-1)+alp.index(str[i]))**2)%p
            return q

        s = pred(s)
        res = []

        X = random.randint(2, P - 1)
        G = random.randint(2, P - 1)
        print("X = ", X)
        print("G = ", G)
        Y = (G ** X) % P
        print("Y = ", Y)
        arr = [i for i in range(2,P-1) if math.gcd(i, P-1) == 1 ]



        for i in s:
            k = random.choice(arr)
            print(k)
            i = llst.index(i)
            a = G ** k % P
            res.append(a)
            b = Y ** k * (i + 1) % P
            res.append(b)
        return res, P, X


    def decelga(s, p, x):
        llst = ['а', 'б', 'в', 'г', 'д', 'е', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф',
                'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']
        res = ""

        for i in range(0, len(s), 2):
            a = s[i]
            b = s[i + 1]
            Mi = (b * pow(a, p - 1 - x, p)) % p
            res += llst[Mi - 1]

        return res

    print("Elgamal")
    text = str(input("Введите текст : "))
    P = int(input("P = "))
    if P > 40 and is_prime(P):

        res = encelga(text, P)

        print("Зашифрованный текст = ", res[0])
        print("Расшифрованный текст = ", decelga(res[0], res[1], res[2]))
    else:
        print("P должен быть больше 40 и простым числом")
elif choice == 21:
    import random
    import math
    def is_prime(n):
        if n <= 1:
            return False
        if n <= 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True

    def pred(s):
        llst = ['а','б','в','г','д','е','ж','з','и','й','к','л','м','н','о','п','р','с','т','у','ф','х','ц','ч','ш','щ','ъ','ы','ь','э','ю','я']
        s = s.lower().replace(' ', '')
        for sim in s:
            if sim not in llst:
                if sim == '.':
                    s = s.replace('.', 'тчк')
                elif sim == ',':
                    s = s.replace(',', 'зпт')
                elif sim == '-':
                    s = s.replace('-', 'тире')
                elif sim == 'ё':
                    s = s.replace('ё', 'е')
                elif sim == '0':
                    s = s.replace('0', 'ноль')
                elif sim == '1':
                    s = s.replace('1', 'один')
                elif sim == '2':
                    s = s.replace('2', 'два')
                elif sim == '3':
                    s = s.replace('3', 'три')
                elif sim == '4':
                    s = s.replace('4', 'четыре')
                elif sim == '5':
                    s = s.replace('5', 'пять')
                elif sim == '1':
                    s = s.replace('6', 'шесть')
                elif sim == '2':
                    s = s.replace('7', 'семь')
                elif sim == '3':
                    s = s.replace('8', 'восемь')
                elif sim == '4':
                    s = s.replace('9', 'девять')
                else:
                    s = s.replace(sim, '')
        return s

    def hesh(str,p,i):
        alp = " АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
        if i==0:
            q=(alp.index(str[i])**2)%p
            return q
        else:
            q=((hesh(str,p,i-1)+alp.index(str[i]))**2)%p
            return q

    ### RSA ###
    def simple(l, b):
        k = random.randint(l, 500)
        while k != 0 and b != 0:
            if k > b:
                k %= b
            else:
                b %= k
        gcd = k + b
        if gcd != 1:
            simple(l, b)
        return k


    def encrsa(s, P, Q):
        llst = ['а','б','в','г','д','е','ж','з','и','й','к','л','м','н','о','п','р','с','т','у','ф','х','ц','ч','ш','щ','ъ','ы','ь','э','ю','я']
        s = pred(s)
        res = []
        D = 1
        N = P * Q
        F = (P - 1) * (Q - 1)

        arr = [i for i in range(2,F) if math.gcd(i,F) == 1]

        E = random.choice(arr)

        print("N = ", N)
        print("F = ", F)
        print("E = ", E)

        for i in range(10000):
            if i * E % F == 1 and i != D:
                D = i
                break
            
            

        print("D = ", D)
        for x in s:
            x = llst.index(x)
            res.append((x ** E) % N)
        return res, D, N


    def decrsa(s, d, n):
        llst = ['а','б','в','г','д','е','ж','з','и','й','к','л','м','н','о','п','р','с','т','у','ф','х','ц','ч','ш','щ','ъ','ы','ь','э','ю','я']
        res = ""
        for i in s:
            ind = (i ** d) % n
            res = res + llst[ind]
        return res


    ### Elgamal ###
    def encelga(s, P, mode):
        llst = ['а', 'б', 'в', 'г', 'д', 'е', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф',
                'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']

        s = pred(s)
        res = []

        X = random.randint(2, P - 1)
        G = random.randint(2, P - 1)

        # G = int(input("Введите G: "))
        print("X (секретный ключ)= ", X)
        print("G = ", G)
        Y = (G ** X) % P
        print("Y = ", Y)
        arr = [i for i in range(2,P-1) if math.gcd(i, P-1) == 1 ]


        mas = [3, 5, 7]
        count = 0
        for i in s:
            if mode == 1:
                k = mas[count%3]
            else:
                k = random.choice(arr)
            print(k)
            i = llst.index(i)
            a = G ** k % P
            res.append(a)
            b = Y ** k * (i + 1) % P
            res.append(b)
            count += 1
        return res, P, X


    def decelga(s, p, x):
        llst = ['а', 'б', 'в', 'г', 'д', 'е', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф',
                'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']
        res = ""

        for i in range(0, len(s), 2):
            a = s[i]
            b = s[i + 1]
            Mi = (b * pow(a, p - 1 - x, p)) % p
            res += llst[Mi - 1]

        return res

    ### RSA подпись ###
    def decrsakey(s, P, Q):
        llst = ['а', 'б', 'в', 'г', 'д', 'е', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф',
                'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']
        s = pred(s)

        D = 7
        # N = P * Q
        N = int(input("Введите N: "))
        F = (P - 1) * (Q - 1)

        arr = [i for i in range(2, F) if math.gcd(i, F) == 1]

        # E = random.choice(arr)
        E = int(input("Введите E: "))
        print("N = ", N)

        print("F = ", F)
        print("E = ", E)
        for i in range(10000):
            if i * E % F == 1 and i != E:
                D = i
                break
            
        print("D = ", D)
        h = 0
        for x in s:
            x = llst.index(x)
            h = ((h + x) ** 2) % N
        S = h ** D % N
        print("S = ", S)
        return s, S, E, N, D


    def checkrsakey(s, key):
        s = pred(s)
        S = int(key[0])
        E = int(key[1])
        N = int(key[2])
        llst = ['а', 'б', 'в', 'г', 'д', 'е', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф',
                'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']
        ho = 0
        for x in s:
            x = llst.index(x)
            ho = ((ho + x) ** 2) % N
        h = S ** E % N
        print("h = ", h)
        print("h0 = ", h)
        if h == ho:
            print(h, "равен", ho)
            print('Цифровая подпись подтверждена')
            result = 'Цифровая подпись подтверждена'
        else:
            print(h, "не равен", ho)
            print('Цифровая подпись не подтверждена')
            result = 'Цифровая подпись не подтверждена'
        return result


    ## Elgamal подпись ###
    def phi(n: int) -> int:
        result = n
        i = 2
        while i ** 2 < n:
            while n % i == 0:
                n /= i
                result -= result / i
            i += 1
        if n > 1:
            result -= result / n
        return result


    def decelgakey(s, P):
        llst = ['а', 'б', 'в', 'г', 'д', 'е', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф',
                'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']
        s = pred(s)
        h = 0

        X = random.randint(2, P - 1)
        X = 5
        G = random.randint(2, P - 1)
        G = 11
        print("G = ", G)
        print("X = ", X)

        Y = G ** X % P
        print("Y = ", Y)
        arr = [i for i in range(2, 10) if math.gcd(i, P - 1) == 1]
        K = random.choice(arr)
        K = 3
        print("K = ", K)
        A = (G ** K) % P
        print("A = ", A)
        for x in s:
            x = llst.index(x)
            h = ((h + x) ** 2) % 11
        print("h0 = ", h)
        B = ((h - A * X) * K ** (phi(P - 1) - 1)) % (P - 1)
        print("B = ", B)
        return s, Y, A, B, P, G, X


    def checkelgakey(s, key):
        s = pred(s)

        y = int(key[0])
        a = int(key[1])
        b = int(key[2])
        p = int(key[3])
        g = int(key[4])
        llst = ['а', 'б', 'в', 'г', 'д', 'е', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф',
                'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']
        h = 0
        for x in s:
            x = llst.index(x)
            h = ((h + x) ** 2) % 11
        print("h = ", h)
        A1 = (y ** a * a ** b) % p
        A2 = g ** h % p

        if A1 == A2:
            print("A1 = ",A1, "равен","A2 = ", A2)
            print('Цифровая подпись подтверждена')
            result = 'Цифровая подпись подтверждена'
        else:
            print("A1 = ", A1, " не равен","A2 = ", A2)

            print('Цифровая подпись не подтверждена')
            result = 'Цифровая подпись не подтверждена'
        return result


    ### ГОСТ Р 34.10-94 подпись ###
    # def decgost94(s, P, Q, A, X):
    #     llst = ['а', 'б', 'в', 'г', 'д', 'е', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф',
    #             'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']
    #     s = pred(s)

    #     Y = A ** X % P
    #     print("Y = ", Y)
    #     K = random.randint(2,Q)


    #     h = 0
    #     for x in s:
    #         x = llst.index(x)
    #         h = ((h + x) ** 2) % 11

    #     print("h0 = ", h)
    #     R = ((A ** K) % P) % Q
    #     if R == 0:
    #         while R == 0:
    #             K = random.randint(2,Q)
    #             R = ((A ** K) % P) % Q

    #     print("k = ", K)
    #     print("R = ", R)
    #     S = ((X * R) + (K * h)) % Q
    #     print("S = ", S)

    #     return R, S, Q, A, Y, P, s


    # def checkgost94(s, key):
    #     s = pred(s)

    #     R = int(key[0])
    #     S = int(key[1])
    #     Q = int(key[2])
    #     A = int(key[3])
    #     Y = int(key[4])
    #     P = int(key[5])
    #     llst = ['а', 'б', 'в', 'г', 'д', 'е', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф',
    #             'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']
    #     h = 0
    #     for x in s:
    #         x = llst.index(x)
    #         h = ((h + x) ** 2) % 11

    #     print("h = ", h)
    #     V = h ** (Q - 2) % Q
    #     Z1 = (S * V) % Q
    #     print("Z1 = ", Z1)
    #     Z2 = ((Q - R) * V) % Q
    #     print("Z2 = ", Z2)
    #     U = ((A ** Z1 * Y ** Z2) % P) % Q
    #     print("U = ", U)
    #     if U == R:
    #         print("U = ", U, "равен", "R = ", R)
    #         print('Цифровая подпись подтверждена')
    #         result = 'Цифровая подпись подтверждена'
    #     else:
    #         print("U = ", U, "не равен", "R = ", R)
    #         print('Цифровая подпись не подтверждена')
    #         result = 'Цифровая подпись не подтверждена'
    #     return result


    # # для RSA
    # print("RSA")
    # P = int(input("P = "))
    # if is_prime(P):
    #     Q = int(input("Q = "))
    #     if is_prime(Q):
    #         if P * Q >= 32:
    #             text = str(input("Введите текст: "))
    #             res = encrsa(text, P, Q)
    #             print("Зашифрованный текст: ",res[0])
    #             print("Расшифрованный текст: ",decrsa(res[0],res[1], res[2]))
    #         else:
    #             print("Произведение p и q меньше длинны алфавиты (32)")
    #     else: 
    #         print("Q не простое число")
    # else:
    #     print("P не простое число")




    # # для подпись RSA
    print("RSA подпись")
    P = int(input("P = "))

    if is_prime(P):
        Q = int(input("Q = "))
        if is_prime(Q):
            if P * Q >= 32:
                text = str(input("Введите текст: "))
                res = decrsakey(text, P, Q)
                checkrsakey(text, [res[1],res[2],res[3]])
            else:
                print("Произведение p и q меньше длинны алфавиты (32)")
        else: 
            print("Q не простое число")
    else:
        print("P не простое число")



    # # для Elgamal
    # print("Elgamal")
    # text = str(input("Введите текст : "))
    # mode = int(input("Проверка по карточке - 1, шифрование - 2: "))
    # P = int(input("P = "))
    # if P > 40 and is_prime(P):

    #     res = encelga(text, P, mode)

    #     print("Зашифрованный текст = ", res[0])
    #     print("Расшифрованный текст = ", decelga(res[0], res[1], res[2]))
    # else:
    #     print("P должен быть больше 40 и простым числом")


    #
    # для  Elgamal подпись


    print("Elgamal подпись")
    text = str(input("Введите текст : "))
    P = int(input("P = "))
    if P > 40 and is_prime(P):

        res = decelgakey(text, P)

        # print("Зашифрованный текст = ", res[0])
        checkelgakey(res[0], res[1:])
    else:
        print("P должен быть больше 40 и простым числом")



    # def is_prime_factor(q,n):
    #     Ans = []
    #     d = 2
    #     while d * d <= n:
    #         if n % d == 0:
    #             Ans.append(d)
    #             n //= d
    #         else:
    #             d += 1
    #     if n > 1:
    #         Ans.append(n)
    #     for i in Ans:
    #         if i == q:
    #             return True

    #     return False

    # # Гост 94 подпись


    # print("ГОСТ 94")
    # P = int(input("P = "))
    # if is_prime(P):
    #     Q = int(input("q = "))
    #     if is_prime_factor(Q, P-1):

    #         A = int(input("a = "))
    #         if (A**Q) % P == 1:

    #             X = int(input("x = "))
    #             if X < Q:
    #                 text = str(input("Вводите текст: "))
    #                 res = decgost94(text, P, Q, A, X)
    #                 checkgost94(res[-1],res[:-1])
    #             else:
    #                 print("X не может быть больше Q")
    #         else:
    #             print("A не удовлетворяет уровнения")
    #     else:
    #         print("q не простой сомножитель p-1")
    # else:
    #     print("Число P не простой")
elif choice == 22:
    import random
    import math
    def is_prime(n):
        if n <= 1:
            return False
        if n <= 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True

    def pred(s):
        llst = ['а','б','в','г','д','е','ж','з','и','й','к','л','м','н','о','п','р','с','т','у','ф','х','ц','ч','ш','щ','ъ','ы','ь','э','ю','я']
        s = s.lower().replace(' ', '')
        for sim in s:
            if sim not in llst:
                if sim == '.':
                    s = s.replace('.', 'тчк')
                elif sim == '?':
                    s = s.replace('?', 'впрс')
                elif sim == '!':
                    s = s.replace('!', 'всклзн')
                elif sim == ':':
                    s = s.replace(':', 'двтч')
                elif sim == '–':
                    s = s.replace('–', 'минус')
                elif sim == ',':
                    s = s.replace(',', 'зпт')
                elif sim == '-':
                    s = s.replace('-', 'тире')
                elif sim == 'ё':
                    s = s.replace('ё', 'е')
                elif sim == '0':
                    s = s.replace('0', 'ноль')
                elif sim == '1':
                    s = s.replace('1', 'один')
                elif sim == '2':
                    s = s.replace('2', 'два')
                elif sim == '3':
                    s = s.replace('3', 'три')
                elif sim == '4':
                    s = s.replace('4', 'четыре')
                elif sim == '5':
                    s = s.replace('5', 'пять')
                elif sim == '1':
                    s = s.replace('6', 'шесть')
                elif sim == '2':
                    s = s.replace('7', 'семь')
                elif sim == '3':
                    s = s.replace('8', 'восемь')
                elif sim == '4':
                    s = s.replace('9', 'девять')
                else:
                    s = s.replace(sim, '')
        return s

    def hesh(str,p,i):
        alp = " АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
        if i==0:
            q=(alp.index(str[i])**2)%p
            return q
        else:
            q=((hesh(str,p,i-1)+alp.index(str[i]))**2)%p
            return q

    ### RSA подпись ###
    def decrsakey(s, P, Q, mod):
        llst = ['а', 'б', 'в', 'г', 'д', 'е', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф',
                'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']
        s = pred(s)

        D = 7
        N = P * Q
        F = (P - 1) * (Q - 1)

        arr = [i for i in range(2, F) if math.gcd(i, F) == 1]
        if mod == 32:
            E = int(input("Введите E: "))
        else:
            E = 17
        if ((E < 1) or (E > mod) or (math.gcd(E, F) != 1)) and mod == 32:
            print("неверное E")
            return 0
        print("N = ", N)

        print("F = ", F)
        print("E = ", E)
        for i in range(10000):
            if i * E % F == 1 and i != E:
                D = i
                break
            
        print("D = ", D)
        h = 4
        for x in s:
            x = llst.index(x)
            h = ((h + x) ** 2) % 32
        S = h ** D % N
        print("S = ", S)
        return s, S, E, N, D


    def checkrsakey(s, key, mod):
        s = pred(s)
        S = int(key[0])
        E = int(key[1])
        N = int(key[2])
        llst = ['а', 'б', 'в', 'г', 'д', 'е', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф',
                'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']
        ho = 4
        for x in s:
            x = llst.index(x)
            ho = ((ho + x) ** 2) % 32
        h = S ** E % N
        print("h = ", h)
        print("h0 = ", h)
        if h == ho:
            print(h, "равен", ho)
            print('Цифровая подпись подтверждена')
            result = 'Цифровая подпись подтверждена'
        else:
            print(h, "не равен", ho)
            print('Цифровая подпись не подтверждена')
            result = 'Цифровая подпись не подтверждена'
        return result
    print("RSA подпись")
    P = int(input("P = "))

    if is_prime(P):
        Q = int(input("Q = "))
        if is_prime(Q):
            if P * Q >= mod:
                text = str(input("Введите текст: "))
                res = decrsakey(text, P, Q, mod)
                checkrsakey(text, [res[1],res[2],res[3]], mod)
            else:
                print(f"Произведение p и q меньше длинны алфавиты (32)")
        else: 
            print("Q не простое число")
    else:
        print("P не простое число")

elif choice == 23:
    import random
    import math


    def is_prime(n):
        if n <= 1:
            return False
        if n <= 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True

    def pred(s):
        llst = ['а','б','в','г','д','е','ж','з','и','й','к','л','м','н','о','п','р','с','т','у','ф','х','ц','ч','ш','щ','ъ','ы','ь','э','ю','я']
        s = s.lower().replace(' ', '')
        for sim in s:
            if sim not in llst:
                if sim == '.':
                    s = s.replace('.', 'тчк')
                elif sim == '?':
                    s = s.replace('?', 'впрс')
                elif sim == '!':
                    s = s.replace('!', 'всклзн')
                elif sim == ':':
                    s = s.replace(':', 'двтч')
                elif sim == '–':
                    s = s.replace('–', 'минус')
                elif sim == ',':
                    s = s.replace(',', 'зпт')
                elif sim == '-':
                    s = s.replace('-', 'тире')
                elif sim == 'ё':
                    s = s.replace('ё', 'е')
                elif sim == '0':
                    s = s.replace('0', 'ноль')
                elif sim == '1':
                    s = s.replace('1', 'один')
                elif sim == '2':
                    s = s.replace('2', 'два')
                elif sim == '3':
                    s = s.replace('3', 'три')
                elif sim == '4':
                    s = s.replace('4', 'четыре')
                elif sim == '5':
                    s = s.replace('5', 'пять')
                elif sim == '1':
                    s = s.replace('6', 'шесть')
                elif sim == '2':
                    s = s.replace('7', 'семь')
                elif sim == '3':
                    s = s.replace('8', 'восемь')
                elif sim == '4':
                    s = s.replace('9', 'девять')
                else:
                    s = s.replace(sim, '')
        return s

    def hesh(str,p,i):
        alp = " АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
        if i==0:
            q=(alp.index(str[i])**2)%p
            return q
        else:
            q=((hesh(str,p,i-1)+alp.index(str[i]))**2)%p
            return q

    ## Elgamal подпись ###
    def phi(n: int) -> int:
        result = n
        i = 2
        while i ** 2 < n:
            while n % i == 0:
                n /= i
                result -= result / i
            i += 1
        if n > 1:
            result -= result / n
        return result


    def decelgakey(s, P, mod):
        llst = ['а', 'б', 'в', 'г', 'д', 'е', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф',
                'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']
        s = pred(s)
        h = 0
        if mod ==32:
            h = 4
        for x in s:
            x = llst.index(x)
            h = ((h + x) ** 2) % 32

        if mod == 32:
            X = 5
            G = 11
        else:
            X = random.randint(2, P - 1)
            G = random.randint(2, P - 1)
        print("G = ", G)
        print("X = ", X)

        Y = G ** X % P
        print("Y = ", Y)
        arr = [i for i in range(2, 10) if math.gcd(i, P - 1) == 1]
        K = random.choice(arr)
        if mod == 32:
            K = 3
        print("K = ", K)
        A = (G ** K) % P
        print("A = ", A)

        print("h0 = ", h)
        B = ((h - A * X) * K ** (phi(P - 1) - 1)) % (P - 1)
        print("B = ", B)
        return s, Y, A, B, P, G, X


    def checkelgakey(s, key, mod):
        s = pred(s)

        y = int(key[0])
        a = int(key[1])
        b = int(key[2])
        p = int(key[3])
        g = int(key[4])
        llst = ['а', 'б', 'в', 'г', 'д', 'е', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф',
                'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']
        h = 0
        if mod == 32:
            h = 4
        for x in s:
            x = llst.index(x)
            h = ((h + x) ** 2) % 32

        print("h = ", h)
        A1 = (y ** a * a ** b) % p
        A2 = g ** h % p

        if A1 == A2:
            print("A1 = ",A1, "равен","A2 = ", A2)
            print('Цифровая подпись подтверждена')
            result = 'Цифровая подпись подтверждена'
        else:
            print("A1 = ", A1, " не равен","A2 = ", A2)

            print('Цифровая подпись не подтверждена')
            result = 'Цифровая подпись не подтверждена'
        return result
    a = int(input("выберите режим(1 - карточка, 2 - текст > 1000 символов): "))
    mod = 0
    if a == 1:
        mod = 32

    else:
        mod == 99

    #для подписи Elgamal
    print("Elgamal подпись")
    text = str(input("Введите текст : "))
    P = int(input("P = "))
    if P > 40 and is_prime(P):

        res = decelgakey(text, P, mod)

        # print("Зашифрованный текст = ", res[0])
        checkelgakey(res[0], res[1:], mod)
    else:
        print("P должен быть больше 40 и простым числом")
elif choice == 24:
    import random
    import math
    def is_prime(n):
        if n <= 1:
            return False
        if n <= 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True

    def pred(s):
        llst = ['а','б','в','г','д','е','ж','з','и','й','к','л','м','н','о','п','р','с','т','у','ф','х','ц','ч','ш','щ','ъ','ы','ь','э','ю','я']
        s = s.lower().replace(' ', '')
        for sim in s:
            if sim not in llst:
                if sim == '.':
                    s = s.replace('.', 'тчк')
                elif sim == ' ':
                    s = s.replace(' ', 'пробел')
                elif sim == '?':
                    s = s.replace('?', 'впрс')
                elif sim == '!':
                    s = s.replace('!', 'всклзн')
                elif sim == ':':
                    s = s.replace(':', 'двтч')
                elif sim == '–':
                    s = s.replace('–', 'минус')
                elif sim == ',':
                    s = s.replace(',', 'зпт')
                elif sim == '-':
                    s = s.replace('-', 'тире')
                elif sim == 'ё':
                    s = s.replace('ё', 'е')
                elif sim == ',':
                    s = s.replace(',', 'зпт')
                elif sim == '-':
                    s = s.replace('-', 'тире')
                elif sim == 'ё':
                    s = s.replace('ё', 'е')
                elif sim == '0':
                    s = s.replace('0', 'ноль')
                elif sim == '1':
                    s = s.replace('1', 'один')
                elif sim == '2':
                    s = s.replace('2', 'два')
                elif sim == '3':
                    s = s.replace('3', 'три')
                elif sim == '4':
                    s = s.replace('4', 'четыре')
                elif sim == '5':
                    s = s.replace('5', 'пять')
                elif sim == '1':
                    s = s.replace('6', 'шесть')
                elif sim == '2':
                    s = s.replace('7', 'семь')
                elif sim == '3':
                    s = s.replace('8', 'восемь')
                elif sim == '4':
                    s = s.replace('9', 'девять')
                else:
                    s = s.replace(sim, '')
        return s


    llst = ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф',
                'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']

    def hash(a):
        h = 0
        for x in a:
            x = llst.index(x)+1
            h = (h + x) ** 2 % 32
            # print(h)
        return h

    mod1 = 11
    def truemod(a):
        flag=False
        for i in range(1,10000):
            if (a*i)%mod1==1:
                flag=True
                return i
        if flag==False:
            return 0



    def solve_R(k, g):
            x1, y1 = g[0], g[1]
            x2, y2 = x1, y1
            mod = 11
            for i in range(2,k+1):
                if x1 == x2 and y1 == y2:
                    lambd = ((3 * (x1 ** 2) + a) % mod * truemod(2 * y1)) % mod
                    # if lambd==0:
                    #     # print("0")
                    #     break
                    # else:
                    x3 = (lambd ** 2 - 2 * x1) % mod
                    y3 = (lambd * (x1 - x3) - y1) % mod
                    # print("(" + str(x3) + ";" + str(y3)+")")
                    x2 = x3
                    y2 = y3
                else:
                    lambd = (((y2 - y1) % mod) * truemod(x2 - x1)) % mod
                    if x2 - x1 == 0:
                        # print("0")
                        break
                    x3 = (lambd ** 2 - x1 - x2) % mod
                    y3 = (lambd * (x1 - x3) - y1) % mod
                    # print("(" + str(x3) + ";" + str(y3) + ")")
                    x2 = x3
                    y2 = y3
                # print("k= " + str(i))

            return x2, y2

    def dota_plus(dot1, dot2):
        x1, y1 = dot1
        x2, y2 = dot2
        mod = 11
        if x1 == x2 and y1 == y2:
            lambd = ((3 * (x1 ** 2) + a) % mod * truemod(2 * y1)) % mod
            # if lambd==0:
            #     # print("0")
            #     break
            # else:
            x3 = (lambd ** 2 - 2 * x1) % mod
            y3 = (lambd * (x1 - x3) - y1) % mod
            # print("(" + str(x3) + ";" + str(y3)+")")
            x2 = x3
            y2 = y3
        else:
            lambd = (((y2 - y1) % mod) * truemod(x2 - x1)) % mod
            if x2 - x1 == 0:
                return 0, 0
            x3 = (lambd ** 2 - x1 - x2) % mod
            y3 = (lambd * (x1 - x3) - y1) % mod
            # print("(" + str(x3) + ";" + str(y3) + ")")
            x2 = x3
            y2 = y3
        return x3, y3 

    q = 13

    x = 0
    k = 0
    text = input("Введите текст для подписи: ")
    while True:
        x = int(input("Введите секрентый ключ x: "))
        if x >= q or x < 1:
            print("Х должен быть меньше q и больше 0")
        else:
            break
    while True:
        k = int(input("Введите  k: "))
        if k >= q or k < 1:
            print("k должен быть меньше q и больше 0")
        else:
            break
    print("Введите парамарты эллептической кривой:")
    a = int(input("a = "))
    b = int(input("b = "))
    modul = int(input("modul = "))
    open_key = 0
    G = (1, 8)
    def decgost(x, mes, a, b, modul, k = 0):
        s = pred(mes)
        q=13
        m = hash(s)
        print(m)
        open_key = solve_R(x, G)
        print('Открытый ключ ', open_key)
        # mod = 32# mod > длина алфавит
        x1, y1= solve_R (k, G)
        P = [x1,y1]
        r = P[0] % q
        if r == 0:
            return "Неподходящее k"
        s = (k*m + r * x) % q

        return r, s, open_key

    def check_gost(sign, open_key, mes, G, mode):
        s = pred(mes)
        q=13
        # if mode == 1:
        #     print("Хэш при проверке 27")
        #     m = 16
        # else:
        #     m = hash(s)
        #     print("Хэш при проверке ", m)
        m = hash(s)
        print("Хэш при проверке ", m)
        r, s = sign
        print(r, s)
        if r > 0 and r < q and s > 0 and s < q:
            u1 = (s * truemod(m)) % q
            u2 = (-r * truemod(m)) % q
            print("u1 ", u1)
            print("u2 ", u2)
            P1 = solve_R(u1, G)
            P2 = solve_R(u2, open_key)
            print("P1 ", P1)
            print("P2 ", P2)
            res = dota_plus(P1, P2)
            print(res[0] % q)
            if res[0] % q == r:
                return "подпись верна ", res[0] % q

        return "Подпись неверна" 

    mode = int(input("1 - карточка, 2 - текст: "))

    res_gost = decgost(x, text, a, b, modul, k)
    open_key = res_gost[2]
    res_gost = res_gost[0], res_gost[1]
    print("Подпись ",res_gost)
    print(open_key)
    print(check_gost(res_gost, open_key, text, G, mode))
elif choice == 25:
    import random
    import math



    def is_prime(n):
        if n <= 1:
            return False
        if n <= 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True

    def pred(s):
        llst = ['а','б','в','г','д','е','ж','з','и','й','к','л','м','н','о','п','р','с','т','у','ф','х','ц','ч','ш','щ','ъ','ы','ь','э','ю','я']
        s = s.lower().replace(' ', '')
        for sim in s:
            if sim not in llst:
                if sim == '.':
                    s = s.replace('.', 'тчк')
                elif sim == ' ':
                    s = s.replace(' ', 'пробел')
                elif sim == '?':
                    s = s.replace('?', 'впрс')
                elif sim == '!':
                    s = s.replace('!', 'всклзн')
                elif sim == ':':
                    s = s.replace(':', 'двтч')
                elif sim == '–':
                    s = s.replace('–', 'минус')
                elif sim == ',':
                    s = s.replace(',', 'зпт')
                elif sim == '-':
                    s = s.replace('-', 'тире')
                elif sim == 'ё':
                    s = s.replace('ё', 'е')
                elif sim == ',':
                    s = s.replace(',', 'зпт')
                elif sim == '-':
                    s = s.replace('-', 'тире')
                elif sim == 'ё':
                    s = s.replace('ё', 'е')
                elif sim == '0':
                    s = s.replace('0', 'ноль')
                elif sim == '1':
                    s = s.replace('1', 'один')
                elif sim == '2':
                    s = s.replace('2', 'два')
                elif sim == '3':
                    s = s.replace('3', 'три')
                elif sim == '4':
                    s = s.replace('4', 'четыре')
                elif sim == '5':
                    s = s.replace('5', 'пять')
                elif sim == '1':
                    s = s.replace('6', 'шесть')
                elif sim == '2':
                    s = s.replace('7', 'семь')
                elif sim == '3':
                    s = s.replace('8', 'восемь')
                elif sim == '4':
                    s = s.replace('9', 'девять')
                else:
                    s = s.replace(sim, '')
        return s

    def hesh(str,p,i):
        alp = " АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
        if i==0:
            q=(alp.index(str[i])**2)%p
            return q
        else:
            q=((hesh(str,p,i-1)+alp.index(str[i]))**2)%p
            return q



    ### ГОСТ Р 34.10-94 подпись ###
    def decgost94(s, P, Q, A, X):
        llst = ['а', 'б', 'в', 'г', 'д', 'е', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф',
                'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']
        s = pred(s)

        Y = A ** X % P
        print("Y = ", Y)
        # K = random.randint(2,Q)
        K = 4


        h = 0
        for x in s:
            x = llst.index(x)
            h = ((h + x) ** 2) % 32

        print("h0 = ", h)
        R = ((A ** K) % P) % Q
        if R == 0:
            while R == 0:
                # K = random.randint(2,Q)
                R = ((A ** K) % P) % Q

        print("k = ", K)
        print("R = ", R)
        S = ((X * R) + (K * h)) % Q
        print("S = ", S)

        return R, S, Q, A, Y, P, s


    def checkgost94(s, key):
        s = pred(s)

        R = int(key[0])
        S = int(key[1])
        Q = int(key[2])
        A = int(key[3])
        Y = int(key[4])
        P = int(key[5])
        llst = ['а', 'б', 'в', 'г', 'д', 'е', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф',
                'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']
        h = 0
        for x in s:
            x = llst.index(x)
            h = ((h + x) ** 2) % 32

        print("h = ", h)
        V = h ** (Q - 2) % Q
        Z1 = (S * V) % Q
        print("Z1 = ", Z1)
        Z2 = ((Q - R) * V) % Q
        print("Z2 = ", Z2)
        U = ((A ** Z1 * Y ** Z2) % P) % Q
        print("U = ", U)
        if U == R:
            print("U = ", U, "равен", "R = ", R)
            print('Цифровая подпись подтверждена')
            result = 'Цифровая подпись подтверждена'
        else:
            print("U = ", U, "не равен", "R = ", R)
            print('Цифровая подпись не подтверждена')
            result = 'Цифровая подпись не подтверждена'
        return result






    def is_prime_factor(q,n):
        Ans = []
        d = 2
        while d * d <= n:
            if n % d == 0:
                Ans.append(d)
                n //= d
            else:
                d += 1
        if n > 1:
            Ans.append(n)
        for i in Ans:
            if i == q:
                return True

        return False

    # # Гост 94 подпись
    def x(Q,P):
        res = []
        for i in range(2,P):
            if (i**Q) % P == 1 :
                res.append(i)
        return res



    print("ГОСТ 94")
    P = int(input("P = "))
    if is_prime(P):
        Q = int(input("q = "))
        if is_prime_factor(Q, P-1):
            # print(x(Q,P))
            A = int(input("a = "))


            if (A**Q) % P == 1 and (A != 1):

                X = int(input("x = "))
                if X < Q and X > 1:
                    text = str(input("Вводите текст: "))
                    res = decgost94(text, P, Q, A, X)
                    checkgost94(res[-1],res[:-1])
                else:
                    print("X не может быть больше Q")
            else:
                print("A не удовлетворяет условиям уравнения")
        else:
            print("q не простой сомножитель p-1")
    else:
        print("Число P не простое")
elif choice == 26:
    import random

    ### ОБМЕН КЛЮЧАМИ ПО ДИФФИ-ХЕЛЛМАНУ ###
    def dfplayer1(p1, N, A):
        K = p1 # Секретный ключ 1 пользователя
        Y1 = (A ** K) % N # Открытый ключ
        return N, A, Y1, K

    def dfplayer2(N, A, Y1, p2):
        K = p2 # Секретный ключ 2 пользователя
        Y2 = (A ** K) % N # Открытый ключ
        K = (Y1 ** p2) % N # Общий ключ
        return Y2, K

    def dfplayer1key(Y2, KU2, N, K1):
        KU1 = (Y2 ** K1) % N # Общий ключ
        print("Секретный ключ первого пользователя:", KU1)
        if KU1 == KU2 and KU1 not in [0,1] and KU2 not in [0,1]:
            print("Ключи совпали")
            return True
        elif  KU1 in [0,1] and KU2 in [0,1]:
            print("Ключи не подходят")
            return True
        else:
            print("Ключи не совпали")
            return False

    def is_prime(n):
        if n <= 1:
            return False
        if n <= 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True

    ### Обмен ключами ###
    print("ОБМЕН КЛЮЧАМИ ПО ДИФФИ-ХЕЛЛМАНУ")

    while True:
        start_over = False

        while True:
            N = int(input("Введите N (простое число и не равное 1) = "))
            if is_prime(N) and N != 1:
                break
            print("N должно быть простым числом и не может быть равным 1.")

        while True:
            A = int(input("Введите A (не равное 1 и меньшее N) = "))
            if A != 1 and A < N:
                break
            print("A должно быть меньше N и не может быть равно 1.")

        while True:
            p1 = int(input("Первый пользователь вводит секретный ключ (не равный 1 и p1 < N - 1) = "))
            if p1 != 1 and p1 < N and (A ** p1) % N != 1:
                break
            print("Секретный ключ не удовлетворяет условие. Пожалуйста, введите другое значение.")

        while True:
            p2 = int(input("Второй пользователь вводит секретный ключ (не равный 1 и p1 < N - 1) = "))
            if p2 != 1 and p2 < N and (A ** p2) % N != 1:
                break
            print("Секретный ключ не удовлетворяет условие. Пожалуйста, введите другое значение.")

        itog = dfplayer1(p1, N, A)
        print("N =", itog[0])
        print("A =", itog[1])
        print("Открытый ключ первого пользователя:", itog[2])

        itog2 = dfplayer2(itog[0], itog[1], itog[2], p2)
        print("Открытый ключ второго пользователя:", itog2[0])
        print("Секретный ключ второго пользователя:", itog2[1])

        start_over = dfplayer1key(itog2[0], itog2[1], itog[0], itog[3])
        prodolg = int(input("Обменятсяь ещё раз (1 - да, 0 - нет) "))
        if prodolg:
            print("Новый обмен:")
        else:
            break

