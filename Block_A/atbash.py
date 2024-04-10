
def crypt(text):
    res = ''
    for i in text:
        #Находим на какой поизиции стоит буква в алфавите
        ind = small_alphabit.find(i)
        #Если мы находим букву в алфавите со строчными буквами, то работаем с ними, иначе работаем по алфавиту прописных букв.
        if ind != -1:
            res += small_alphabit[-ind-1]
            continue
        ind = big_alphabit.find(i)
        if ind != -1:
            res += big_alphabit[-ind-1]
            continue
        #Для случая, если буква не найдена ни в одном из алфавитов
        else:
            res += i
    return res

# mode = int(input("Выберите режим (1 - шифрование; 2 - расшифрование): "))
task = int(input("Работа с карточкой - 1, работа с большим текстом - 2: "))
if task == 1:
    big_alphabit = 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
    small_alphabit = big_alphabit.lower()
else:
    big_alphabit = 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ @#!%^&*()-+.:;'
    small_alphabit = big_alphabit.lower()
open_text = input("Введитек текст для работы: \n")
print(crypt(open_text))