alp = 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯфбвгджзийклмнопрстуфхцчшщъыьэюя ,.!?:1234567890-—;/()[]<>\'"' # для большого текста
HEX = '0123456789abcdef'

# это наши s блоки 8 штук
s_blocks = [
	[12, 4,  6,  2,  10, 5,  11, 9,  14, 8,  13, 7,  0,  3,  15, 1],
	[6,  8,  2,  3,  9,  10, 5,  12, 1,  14, 4,  7,  11, 13, 0,  15],
	[11, 3,  5,  8,  2,  15, 10, 13, 14, 1,  7,  4,  12, 9,  6,  0],
	[12, 8,  2,  1,  13, 4,  15, 6,  7,  0,  10, 5,  3,  14, 9,  11],
	[7,  15, 5,  10, 8,  1,  6,  13, 0,  9,  3,  14, 11, 4,  2,  12],
	[5,  13, 15, 6,  9,  2,  12, 10, 11, 7,  8,  1,  4,  3,  14, 0],
	[8,  14, 2,  5,  6,  9,  1,  12, 15, 4,  11, 0,  13, 10, 3,  7],
	[1,  7,  14, 13, 0,  5,  8,  3,  4,  15, 10, 6,  9,  12, 11, 2]]

# s блок шифрование
def s_block_encrypt(inp: str) -> str:
	
	# надо поделить 4 буквы по 8 индексов
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
def s_block_decrypt(inp: str) -> str:
		
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
		out += s_block_encrypt(text[i*4:i*4+4])
	return out

def decrypt(text: str) -> str:
	out = ""
	l = len(text)
	for i in range(l//8):
		out += s_block_decrypt(text[i*8:i*8+8])
	while text[-1] == " ":
		text = text[0:-1]
	return out

text = input("Введите сообщение: ").upper()
result = encrypt(text)
print("Зашифрованный текст: " + result)
print("Расшифрованный текст: " + decrypt(result))
