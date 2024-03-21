
"""
         Рассмотрим K = kG, где K и G - точки на эллиптической кривой Ep (a, b), n - порядок G (nG = O∞), а k - целое число меньше n.
         Для заданных k и G легко вычислить K по правилу сложения, но, наоборот, для K и G найти k очень сложно.
         Поскольку при фактическом использовании ECC, в принципе, требуется, чтобы p было достаточно большим, а n также довольно большим, поэтому невозможно вычислить n точек решения по одной в приведенной выше таблице.
         Это математическая основа алгоритма шифрования эллиптической кривой.

         Точка G называется базовой точкой

         k (k <n) - закрытый ключ (частный ключ)

         K - открытый ключ (открытый ключ)
"""

big_alphabit = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ #!^*()?-–+.,:;абвгдеёжзийклмнопрстуфхцчшщъыьэюя'

a = 2
b = 7
m = 10
G = (6, 2)
Cb = 5
k = 6
mod = 11
def truemod(a):
    flag=False
    for i in range(1,10000):
        if (a*i) % mod ==1:
            flag=True
            return i
    if flag==False:
        return 0
    
def solve_R(k, g):
    x1, y1 = g[0], g[1]
    x2, y2 = x1, y1
    
    for i in range(k-1):
        if x1==x2 and y1==y2:
            lambd=((3*(x1**2)+a) % mod*truemod(2*y1)) % mod
            # if lambd==0:
            #     # print("0")
            #     break
            # else:
            x3=(lambd**2-2*x1) % mod
            y3=(lambd*(x1-x3)-y1) % mod
            # print("(" + str(x3) + ";" + str(y3)+")")
            x2 = x3
            y2 = y3
        else:
            lambd=(((y2-y1) % mod)*truemod(x2-x1)) % mod
            if x2-x1==0:
                # print("0")
                break
            x3=(lambd**2-x1-x2) % mod
            y3=(lambd*(x1-x3)-y1) % mod
            # print("(" + str(x3) + ";" + str(y3) + ")")
            x2=x3
            y2=y3

    return x2, y2

r = solve_R(k, G)
print("R", r)
Db = solve_R(Cb, G)
print("Db", Db)
print("P", solve_R(k, Db))

e = (m * r[0])% mod
print ("(R, e)", r, e) 

s = input("Введите текст: ")







