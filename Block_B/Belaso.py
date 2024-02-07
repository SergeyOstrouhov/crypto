def decrypt_bellaso(msg, key):
    decrypted_text = ''  # Переменная для хранения расшифрованного текста
    alphabet = "абвгдежзийклмнопрстуфхцчшщъыьэюя" + "абвгдежзийклмнопрстуфхцчшщъыьэюя".upper() + " !\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"
    offset = 0  # Смещение для коррекции индексов шифрованного текста
    
    for ix in range(len(msg)):  # Проходим по каждому символу в сообщении
        if msg[ix] not in alphabet:  # Если символ не находится в алфавите, то оставляем его без изменений
            output = msg[ix]
            offset += -1  # Уменьшаем смещение, чтобы правильно сопоставить символы
        else:
            # Расшифровываем символ с помощью ключа и алфавита с учетом смещения
            output = alphabet[(alphabet.find(msg[ix]) - (alphabet.find(key[((ix + offset) % len(key))]))) % len(alphabet)]
        decrypted_text += output  # Добавляем расшифрованный символ к результату
    return decrypted_text  # Возвращаем расшифрованный текст

def encrypt_bellaso(msg, key):
    encrypted_text = ''  # Переменная для хранения зашифрованного текста
    alphabet = "абвгдежзийклмнопрстуфхцчшщъыьэюя" + "абвгдежзийклмнопрстуфхцчшщъыьэюя".upper() + " !\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"
    offset = 0  # Смещение для коррекции индексов шифрованного текста
    
    for ix in range(len(msg)):  # Проходим по каждому символу в сообщении
        if msg[ix] not in alphabet:  # Если символ не находится в алфавите, то оставляем его без изменений
            output = msg[ix]
            offset += -1  # Уменьшаем смещение, чтобы правильно сопоставить символы
        else:
            # Шифруем символ с помощью ключа и алфавита с учетом смещения
            output = alphabet[(alphabet.find(msg[ix]) + (alphabet.find(key[((ix + offset) % len(key))]))) % len(alphabet)]
        encrypted_text += output  # Добавляем зашифрованный символ к результату
    return encrypted_text  # Возвращаем зашифрованный текст



    
text = input("введите текст:")
key = input("вввдеите ключ: ")
encrypted_result = encrypt_bellaso(msg=text, key=key)
print("Зашифрованный текст:", encrypted_result)
print("Расшифрованный текст:", decrypt_bellaso(msg=encrypted_result, key=key))
