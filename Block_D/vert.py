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
