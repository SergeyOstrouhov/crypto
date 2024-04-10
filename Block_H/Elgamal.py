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