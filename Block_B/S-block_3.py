simbs = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ.,-+/!&%? "
hex_val = "00 01 02 03 04 05 06 07 08 09 0A 0B 0C 0D 0E 0F 10 11 12 13 14 15 16 17 18 19 1A 1B 1C 1D 1E 1F 20 21 22 23 24 25 26 27 28 29 2A 2B 2C 2D 2E 2F 30 31 32 33 34 35 36 37 38 39 3A 3B 3C 3D 3E 3F 40"

translate = dict(zip(simbs, hex_val.split()))

hexnum = '0123456789abcdef'
s_blocks = [
	[1,7,14,13,0,5,8,3,4,15,10,6,9,12,11,2], 
    [8,14,2,5,6,9,1,12,15,4,11,0,13,10,3,7], 
    [5,13,15,6,9,2,12,10,11,7,8,1,4,3,14,0], 
    [7,15,5,10,8,1,6,13,0,9,3,14,11,4,2,12], 
    [12,8,2,1,13,4,15,6,7,0,10,5,3,14,9,11], 
    [11,3,5,8,2,15,10,13,14,1,7,4,12,9,6,0], 
    [6,8,2,3,9,10,5,12,1,14,4,7,11,13,0,15], 
    [12,4,6,2,10,5,11,9,14,8,13,7,0,3,15,1]]

def func_t(text):
    res = ''
    for i in range(len(text)):
       ind = hexnum.index(text[i])
       res += hexnum[s_blocks[i][ind]]
    return res

def func_t_decrypt(text):
    res = ''
    for i in range(len(text)):
       ind = hexnum.index(text[i])
    #    print(s_blocks[7-i])
       res += hexnum[s_blocks[i].index(ind)]
    return res 
text = input("Введите текст для работы: ")
res_enc = func_t(text)
res_decr = func_t_decrypt(res_enc)
print(res_enc)
print(res_decr)
# print(translate["щ"])
#fdb97531