def tritemiy_cypr(opentext,alphabet):
    cyprtext = ""
    n=len(alphabet) #Длинна алфавита
    for j in range(0,len(opentext)):
        i=alphabet.find(opentext[j])
        Y=(i+j)%n # Вычисление индекса буквы
        cyprtext+=alphabet[Y]
    return cyprtext
def tritemiy_decypr(cyprtext,alphabet):
    decypr= ""
    n = len(alphabet)
    for j in range(0, len(cyprtext)):
        i = alphabet.find(cyprtext[j])
        Y = (i - j) % n # Вычисление индекса буквы
        decypr += alphabet[Y]
    return decypr
flag=True
while flag:
    type = int(input("Введите тип текста (1- поговорка, 2 - текст 1000 символов) "))
    if type == 1:
        alphabet = "абвгдежзийклмнопрстуфхцчшщъыьэюя"
        text = "Нет такого мудреца, в котором не было бы глупости."
        text = text.replace('.', "тчк").replace(',', "зпт").replace(" ", "").lower()
        cypr=tritemiy_cypr(text,alphabet)
        print(cypr)
        decypr=tritemiy_decypr(cypr,alphabet)
        print(decypr)
        # err=caesar(1,text,card_alp,card_alp_len) Ввел в качестве ключа длинну алфавита для проверки на ошибку
    elif type == 2:
        alphabet = "абвгдежзийклмнопрстуфхцчшщъыьэюя" + "абвгдежзийклмнопрстуфхцчшщъыьэюя".upper() + ".,-!? "
        
        text = input("Введите текст: ")
        cypr = tritemiy_cypr(text,alphabet)
        decypr = tritemiy_decypr(cypr,alphabet)
        n = 500
        print("Результат шифрования")
        for i in range(0, len(cypr), n):
            print(cypr[i:i + n])
        print()
        print("Результат расшифрования")
        for i in range(0, len(decypr), n):
            print(decypr[i:i + n])
    else:
        print("неправильный тип")
        flag=False
