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


