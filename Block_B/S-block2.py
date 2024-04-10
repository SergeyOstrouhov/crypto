alp = 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдежзийклмнопрстуфхцчшщъыьэюя ,.!?:1234567890-—;/()[]<>\'"' 
HEX = '0123456789abcdef'

# таблица с s-блоками
s_blocks = [
	[1, 15, 3, 0, 7, 13, 8, 14, 9, 11, 5, 10, 2, 6, 4, 12],
	[15, 0, 13, 11, 7, 4, 14, 1, 12, 5, 10, 9, 3, 2, 8, 6],
	[0, 6, 9, 12, 4, 7, 1, 14, 13, 10, 15, 2, 8, 5, 3, 11],
	[11, 9, 14, 3, 5, 10, 0, 7, 6, 15, 4, 13, 1, 2, 8, 12],
	[12, 2, 4, 11, 14, 3, 9, 0, 13, 6, 1, 8, 10, 5, 15, 7],
	[0, 14, 3, 4, 1, 8, 7, 11, 10, 12, 2, 9, 6, 15, 13, 5],
	[7, 3, 10, 13, 0, 11, 4, 15, 12, 1, 9, 6, 5, 2, 14, 8],
	[2, 11, 12, 9, 6, 10, 15, 4, 3, 8, 5, 0, 13, 14, 7, 1]]

# шифрование
def encrypt(inp: str) -> str:
	# делим на 8 частей
	i0 = (alp.index(inp[0]) & 0b11110000) >> 4;
	i1 = (alp.index(inp[0]) & 0b00001111);

	i2 = (alp.index(inp[1]) & 0b11110000) >> 4;
	i3 = (alp.index(inp[1]) & 0b00001111);

	i4 = (alp.index(inp[2]) & 0b11110000) >> 4;
	i5 = (alp.index(inp[2]) & 0b00001111);

	i6 = (alp.index(inp[3]) & 0b11110000) >> 4;
	i7 = (alp.index(inp[3]) & 0b00001111);

	# подставление индексов в s блоки и получение результата 4 буквы
	return HEX[s_blocks[0][i0]] + HEX[s_blocks[1][i1]] + \
		HEX[s_blocks[2][i2]] + HEX[s_blocks[3][i3]] + \
		HEX[s_blocks[4][i4]] + HEX[s_blocks[5][i5]] + \
		HEX[s_blocks[6][i6]] + HEX[s_blocks[7][i7]]

# s блок расшифрование
def decrypt(inp: str) -> str:
		
	# определяем индексы по значению из s блоков
	i0 = s_blocks[0].index(HEX.index(inp[0]));
	i1 = s_blocks[1].index(HEX.index(inp[1]));

	i2 = s_blocks[2].index(HEX.index(inp[2]));
	i3 = s_blocks[3].index(HEX.index(inp[3]));

	i4 = s_blocks[4].index(HEX.index(inp[4]));
	i5 = s_blocks[5].index(HEX.index(inp[5]));

	i6 = s_blocks[6].index(HEX.index(inp[6]));
	i7 = s_blocks[7].index(HEX.index(inp[7]));

	# складываем левые и правые 4 бит в байты и получаем букву в алфавите
	return alp[(i0 << 4) | i1] + alp[(i2 << 4) | i3] + alp[(i4 << 4) | i5] + alp[(i6 << 4) | i7]

def encrypt(text: str) -> str:
	out = ""
	l = len(text)
	while l%4 != 0:
		text += " "
		l += 1
	for i in range(l//4):
		out += encrypt(text[i*4:i*4+4])
	return out

def decrypt(text: str) -> str:
	out = ""
	l = len(text)
	for i in range(l//8):
		out += decrypt(text[i*8:i*8+8])
	while text[-1] == " ":
		text = text[0:-1]
	return out

text = input("Введите сообщение: ")
result = encrypt(text)
print("Зашифрованный текст: " + result)
print("Расшифрованный текст: " + decrypt(result))
