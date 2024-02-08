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
