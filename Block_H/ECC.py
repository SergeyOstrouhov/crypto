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