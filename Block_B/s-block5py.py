import textwrap

s_block = [
    [1,7,14,13,0,5,8,3,4,15,10,6,9,12,11,2], 
    [8,14,2,5,6,9,1,12,15,4,11,0,13,10,3,7], 
    [5,13,15,6,9,2,12,10,11,7,8,1,4,3,14,0], 
    [7,15,5,10,8,1,6,13,0,9,3,14,11,4,2,12], 
    [12,8,2,1,13,4,15,6,7,0,10,5,3,14,9,11], 
    [11,3,5,8,2,15,10,13,14,1,7,4,12,9,6,0], 
    [6,8,2,3,9,10,5,12,1,14,4,7,11,13,0,15], 
    [12,4,6,2,10,5,11,9,14,8,13,7,0,3,15,1]
]

def GOST_Magma_T(in_data):
    out_data = [0x00, 0x00, 0x00, 0x00]
    for i in range(4):
        # Извлекаем первую 4-битную часть байта
        first_part_byte = (in_data[i] & 0xf0) >> 4
        # Извлекаем вторую 4-битную часть байта
        sec_part_byte = (in_data[i] & 0x0f)
        # Выполняем замену в соответствии с таблицей подстановок
        first_part_byte = s_block[i * 2][first_part_byte]
        sec_part_byte = s_block[i * 2 + 1][sec_part_byte]
        # «Склеиваем» обе 4-битные части обратно в байт
        out_data[i] = (first_part_byte << 4) | sec_part_byte
    return out_data

def GOST_Magma_T_inverse(in_data):
    out_data = [0x00, 0x00, 0x00, 0x00]
    for i in range(4):
        # Извлекаем первую 4-битную часть байта
        first_part_byte = (in_data[i] & 0xf0) >> 4
        # Извлекаем вторую 4-битную часть байта
        sec_part_byte = (in_data[i] & 0x0f)
        # Выполняем обратную замену в соответствии с таблицей подстановок
        first_part_byte = s_block[i * 2].index(first_part_byte)
        sec_part_byte = s_block[i * 2 + 1].index(sec_part_byte)
        # «Склеиваем» обе 4-битные части обратно в байт
        out_data[i] = (first_part_byte << 4) | sec_part_byte
    return out_data

print("Преобразование по S-блоку из примера в ГОСТ: ")
example1 = [0xfd, 0xb9, 0x75, 0x31]
example2 = [0x2a, 0x19, 0x6f, 0x34]
example3 = [0xeb, 0xd9, 0xf0, 0x3a]
example4 = [0xb0, 0x39, 0xbb, 0x3d]

result1 = GOST_Magma_T(example1)
result2 = GOST_Magma_T(example2)
result3 = GOST_Magma_T(example3)
result4 = GOST_Magma_T(example4)

print([hex(byte) for byte in result1])
print([hex(byte) for byte in result2])
print([hex(byte) for byte in result3])
print([hex(byte) for byte in result4])


print("-----------------------------------------------")
print("Обратное преобразование по S-блоку из примера в ГОСТ: ")

result1_inverse = GOST_Magma_T_inverse(result1)
result2_inverse = GOST_Magma_T_inverse(result2)
result3_inverse = GOST_Magma_T_inverse(result3)
result4_inverse = GOST_Magma_T_inverse(result4)

print([hex(byte) for byte in result1_inverse])
print([hex(byte) for byte in result2_inverse])
print([hex(byte) for byte in result3_inverse])
print([hex(byte) for byte in result4_inverse])


print("-----------------------------------------------")

alphabet_up = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ #!^*()?-–+.,:;абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
def text_to_hex(text, alphabet):
    hex_representation = ""
    for char in text:
        if char in alphabet:
            index_hex = format(alphabet.index(char), 'X')
            hex_representation += index_hex.rjust(2, '0')  # Right-justify and pad to two characters
    return hex_representation


def pad_to_64_bits(input_string):
    length = len(input_string)
    remainder = length % 32
    if remainder != 0:
        padding_length = 32 - remainder
        padded_string = input_string + '0' * padding_length
        return padded_string
    else:
        return input_string

def split_into_32_bits(hex_data):
    return textwrap.wrap(hex_data, 8)

def apply_gost_magma_t(hex_block):
    block_bytes = [int(hex_block[i:i+2], 16) for i in range(0, len(hex_block), 2)]
    result_block = GOST_Magma_T(block_bytes)
    return ''.join([format(byte, '02X') for byte in result_block])

def encrypt_text(input_text):
    hex_representation = text_to_hex(input_text, alphabet_up)
    padded_hex_data = pad_to_64_bits(hex_representation)
    blocks_32_bits = split_into_32_bits(padded_hex_data)

    encrypted_blocks = []
    for block in blocks_32_bits:
        encrypted_block = apply_gost_magma_t(block)
        encrypted_blocks.append(encrypted_block)

    encrypted_text = ''.join(encrypted_blocks)
    return encrypted_text



def text_to_hex(text, alphabet):
    hex_representation = ""
    for char in text:
        if char in alphabet:
            index_hex = format(alphabet.index(char), 'X')
            hex_representation += index_hex.rjust(2, '0')  # Right-justify and pad to two characters
    return hex_representation


def apply_gost_magma_t(hex_block):
    block_bytes = [int(hex_block[i:i+2], 16) for i in range(0, len(hex_block), 2)]
    result_block = GOST_Magma_T(block_bytes)
    return ''.join([format(byte, '02X') for byte in result_block])

def apply_gost_magma_t_inverse(hex_block):
    block_bytes = [int(hex_block[i:i+2], 16) for i in range(0, len(hex_block), 2)]
    result_block = GOST_Magma_T_inverse(block_bytes)
    return ''.join([format(byte, '02X') for byte in result_block])

def decrypt_text(encrypted_text):
    blocks_32_bits = split_into_32_bits(encrypted_text)

    decrypted_blocks = []
    for block in blocks_32_bits:
        decrypted_block = apply_gost_magma_t_inverse(block)
        decrypted_blocks.append(decrypted_block)

    decrypted_hex_data = ''.join(decrypted_blocks)
    decrypted_text = hex_to_text(decrypted_hex_data, alphabet_up)
    return decrypted_text

def hex_to_text(hex_data, alphabet):
    text_representation = ""
    for i in range(0, len(hex_data), 2):
        hex_pair = hex_data[i:i+2]
        decimal_value = int(hex_pair, 16)
        text_representation += alphabet[decimal_value]
    return text_representation


input_text = input("Открытый текст: ").upper()
# input_text = input_text.replace(".", "ТЧК")
# input_text = input_text.replace(",", "ЗПТ")
# input_text = input_text.replace(" ", "ПРБ")
input_text = input_text + "КНЦШФР"
encrypted_text = encrypt_text(input_text)
print("Зашифрованный текст: ", encrypted_text)

decrypted_text = decrypt_text(encrypted_text)
# decrypted_text = decrypted_text.replace("ТЧК", ".")
# decrypted_text = decrypted_text.replace("ЗПТ", ",")
# decrypted_text = decrypted_text.replace("ПРБ", " ")
decrypted_text = decrypted_text[:decrypted_text.find("КНЦШФР")]
print("Расшифрованный текст: ", decrypted_text)