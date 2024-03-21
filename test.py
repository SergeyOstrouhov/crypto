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
a = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ #!^*()?-–+.,:;абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
print(len(a))