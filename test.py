
# # arr=[0, 1 , 4, 9, 16, 25, 36, 8, 23, 40, 18, 39, 21, 5, 32, 20, 10, 2, 37, 33, 31]
# # for i in range (41):
# #     q=(i**3+i+3)%41
# #     print("x = "+ str(i) +" y^2= "+ str(q))
# #     if q in arr:
# #         print("exist")
# def truemod(a):
#     flag=False
#     for i in range(1,10000):
#         if (a*i)%mod==1:
#             flag=True
#             return i
#     if flag==False:
#         return 0
# ## Первая точка
# x1=1
# y1=8
# #Вторая точка
# x2=x1
# y2=y1
# mod=11
# # k = 110
# print("")
# for i in range(2,42):
#     if x1==x2 and y1==y2:
#         lambd=((3*(x1**2)+a)%mod*truemod(2*y1))%mod
#         if lambd==0:
#              print("0")
#              break
#         else:
#             x3=(lambd**2-2*x1)%mod
#             y3=(lambd*(x1-x3)-y1)%mod
#             print("(" + str(x3) + ";" + str(y3)+")")
#             x2 = x3
#             y2 = y3
#     else:
#         lambd=(((y2-y1)%mod)*truemod(x2-x1))%mod
#         if x2-x1==0:
#             print("0")
#             break
#         x3=(lambd**2-x1-x2)%mod
#         y3=(lambd*(x1-x3)-y1)%mod
#         print("(" + str(x3) + ";" + str(y3) + ")")
#         x2=x3
#         y2=y3

#     #print("k= "+str(i))
# a = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ #!^*()?-–+.,:;абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
# print(len(a))
# alp = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
# def hash(text, modul, mode):
#     res = 0
#     for i in text:
#         res = ((res + alp.index(i))**2) % modul
#     return res
# a = 'неттакогомудрецазптвкоторомнебылобыглупоститчк'
# print(hash(a, 32, 1))


def egcd(a, b):
  """
  Расширенный алгоритм Евклида.

  Args:
      a: целое число.
      b: целое число.

  Returns:
      (d, x, y): 
          - НОД (a, b)
          - x, такое, что ax + by = d
  """
  if b == 0:
    return (a, 1, 0)
  else:
    (g, x1, y1) = egcd(b, a % b)
    return (g, y1, x1 - (a // b) * y1)

def mod_inverse(a, m):
  """
  Находит обратный элемент a по модулю m.

  Args:
      a: целое число.
      m: целое число (модуль).

  Returns:
      Обратный элемент a по модулю m (целое число) или None, 
      если обратного элемента не существует.
  """

  (d, x, y) = egcd(a, m)
  if d != 1:
    return None
  else:
    return x % m


print(mod_inverse(6, 22))

# def solve_modular_comparison(a, b, m):
#   """
#   Решает сравнение первой степени ax ≡ b (mod m).

#   Args:
#       a: целое число (коэффициент при x).
#       b: целое число (правая часть).
#       m: целое число (модуль).

#   Returns:
#       Множество решений (целые числа) или None, если решений нет.
#   """

#   # Проверка на делимость a на m
#   if a % m == 0:
#     return None  # Решений нет

#   # Вычисление обратного элемента a по модулю m
#   inverse_a = mod_inverse(a, m)

#   # Решение уравнения
#   x = b * inverse_a % m

#   # Возвращение решения
#   return {x}

# # Пример использования
# a = 6
# b = 26
# m = 22

# solution = solve_modular_comparison(a, b, m)
# print(solution)  # {2}