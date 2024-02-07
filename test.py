def split_and_adjust(string):
    substrings = []
    i = 0
    while i < len(string):
        if i == len(string) - 1:
            substrings.append([string[i], ""])  # Добавляем последний символ как подстроку
            break
        if string[i] == string[i+1]:  # Проверяем на повторение символов
            substrings.append([string[i], "я"])  # Если повторяется, заменяем второй символ
            i += 1  # Переходим к следующему символу
        else:
            substrings.append([string[i], string[i+1]])  # Если нет повторения, добавляем оба символа
            i += 2  # Переходим к следующей паре символов
    if substrings[-1][1] == "":
        substrings[-1][1] = "ф"
    return substrings

# Пример использования:
string = "неттакого"
substrings = split_and_adjust(string)
print(substrings)  # Выводим список подстрок
