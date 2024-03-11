# from bit import BitArray
import re
for_big_text = "АБВГДЕёЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ".lower() + "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"  + " !\"#$%-'()*+,—–./:;<=>?@[\]^_`{|}"

mode = int(input("выберите режим (1 - карточка, 2 - большой текст): "))

if mode == 1:
    text = input("Введите текст: ").upper()
else:
    text = input("Введите текст: ")
text_reg = ''
for i in text:
    c = str(bin(for_big_text.find(i)+1))[2:]
    while len(c) != 8: c = '0' + c
    text_reg += c
key = [1] * 64
print(text_reg)

x = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
y = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
z = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

gamma = ''

def F(x, y, z):
    return (x & y) or (x & z) or (y & z)

for i in range(64):
    x.append(x[1] ^ x[2] ^ x[5] ^ x.pop(0) ^ key[i])
    y.append(y[1] ^ y.pop(0) ^ key[i])
    z.append(z[1] ^ z[2] ^ z[15] ^ z.pop(0) ^ key[i])
    # print(*x)
    # print(*y)
    # print(*z)
    # print("------------------------------------------")


for i in range(100):
    f = F(x[10], y[11], z[12])
    if x[10] == f:
        x.append(x[1] ^ x[2] ^ x[5] ^ x.pop(0))
    if y[11] == f:
        y.append(y[1] ^ y.pop(0))
    if z[12] == f:
        z.append(z[1] ^ z[2] ^ z[15] ^ z.pop(0))

for i in range(114):
    gamma += str(x[0] ^ y[0] ^ z[0])
    f = F(x[10], y[11], z[12])
    if x[10] == f:
        x.append(x[1] ^ x[2] ^ x[5] ^ x.pop(0))
    if y[11] == f:
        y.append(y[1] ^ y.pop(0))
    if z[12] == f:
        z.append(z[1] ^ z[2] ^ z[15] ^ z.pop(0)) 
print(x, y, z)
print("gamma:" + gamma)

gamma = gamma*500
text_enc = ''
for i in range(len(text_reg)):
    text_enc += str(int(text_reg[i]) ^ int(gamma[i]))
text_dec = ''
text_dec_res = ''
for i in range(len(text_enc)):
    text_dec += str(int(text_enc[i]) ^ int(gamma[i]))
text_dec_sub = re.findall(".{8}", text_dec)
# print(text_dec_sub)
for i in text_dec_sub:
    text_dec_res += for_big_text[int(i, 2)-1]
print(text_enc)
print(text_dec_res)
