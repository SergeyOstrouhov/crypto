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
    
