import numpy as np
def multi_matr(matr, vector):
    if len(vector) == 1:
        vector.append(0)
        vector.append(0)
    elif len(vector) == 2:
        vector.append(0)
    res = []
    for i in matr:
        a = 0
        for j in range(len(i)):
            a += i[j] * vector[j]
        res.append(a)
    return(res)

def inv_matr(matr):
    try:
        # Преобразование двумерного списка в массив numpy
        numpy_matrix = np.array(matr)

        # Нахождение обратной матрицы
        inverse = np.linalg.inv(numpy_matrix)

        return inverse.tolist()  # Преобразование обратной матрицы обратно в двумерный список
    except np.linalg.LinAlgError:
        # Если матрица вырожденная, обратной матрицы не существует
        return "Матрица вырожденная, обратной матрицы не существует"
    
def crypt(text,  matr):
    blocks = []
    res = []
    nums = []

    for i in text:
        nums.append(alp.index(i)+1)
    for i in range(0, len(text), size):
        blocks.append(nums[i:i+size])
    for i in blocks:
        new_vector = multi_matr(matr, i)
        for j in new_vector:
            res.append(j)
            # print(j)
    return res

def decrypt(text, matr):
    new_matr = inv_matr(matr)
    res = []
    blocks = []
    otv = ""
    for i in range(0, len(text), size):
        blocks.append(text[i:i+size])
    for i in blocks:
        new_vector = multi_matr(new_matr, i)
        for j in new_vector:
            res.append(int(j+0.5))
            # print(j)
    for i in res:
        otv += alp[i-1]
    return otv
matr = []
size = int(input("Введите размер КВАДРАТНОЙ матрицы: "))
for i in range(size):
    l = list(map(int, input(f'Введите {i+1} строку матрицы: ').split()))
    if len(l) != size:
        print("Неверный ввод!")
    else:
        matr.append(l)

task = int(input("Выберите режим (1- карточка, 2 - текст > 1000 символов):"))
if task == 1:
    alp = 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
elif task == 2:
    alp = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ #!^*()?-–+.,:;абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
text = input("Введите текст: ")
ciphertext = crypt(text,  matr)
print("".join(list(map(str, ciphertext))))
print(decrypt(ciphertext, matr))
# print(inv_matr(matr))