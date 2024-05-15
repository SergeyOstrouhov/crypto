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


