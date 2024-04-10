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
r4 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
gamma = ''

def F(x, y, z):
    return (x & y) or (x & z) or (y & z)

for i in range(64):
    x.append(x[1] ^ x[2] ^ x[5] ^ x.pop(0) ^ key[i])
    y.append(y[1] ^ y.pop(0) ^ key[i])
    z.append(z[1] ^ z[2] ^ z[15] ^ z.pop(0) ^ key[i])
    r4.append(r4[5] ^ key[i] ^ r4.pop(0))
    # print(*x)
    # print(*y)
    # print(*z)
    # print("------------------------------------------")
r4[6], r4[9], r4[13] = 1, 1, 1

for i in range(99):
    f = F(r4[6], r4[9], r4[13])
    if r4[6] == f:
        x.append(x[1] ^ x[2] ^ x[5] ^ x.pop(0))
    if r4[9] == f:
        y.append(y[1] ^ y.pop(0))
    if r4[13] == f:
        z.append(z[1] ^ z[2] ^ z[15] ^ z.pop(0))
    r4.append(r4[5] ^ r4.pop(0))

for i in range(114):
    f1 = F(x[3], x[4], x[6])
    f2 = F(y[6], y[9], y[13])
    f3 = F(z[4], z[6], z[9])
    gamma += str(x[0] ^ y[0] ^ z[0] ^ f1 ^ f2 ^ f3)
    f = F(r4[6], r4[9], r4[13])
    if r4[6] == f:
        x.append(x[1] ^ x[2] ^ x[5] ^ x.pop(0))
    if r4[9] == f:
        y.append(y[1] ^ y.pop(0))
    if r4[13] == f:
        z.append(z[1] ^ z[2] ^ z[15] ^ z.pop(0))
    r4.append(r4[5] ^ r4.pop(0))
# for i in r4:
#     print(i)
print("gamma:"+ gamma)
# for i in gamma:
#     print(i)


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
# for i in text_enc:
#     print(i)