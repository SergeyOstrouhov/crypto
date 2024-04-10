def GOST_Magma_Add_32(a, b, c):
    internal = 0
    for i in range(3, -1, -1):
        internal = a[i] + b[i] + (internal >> 8)
        c[i] = internal & 0xff

Pi = [
    [1, 7, 14, 13, 0, 5, 8, 3, 4, 15, 10, 6, 9, 12, 11, 2],
    [8, 14, 2, 5, 6, 9, 1, 12, 15, 4, 11, 0, 13, 10, 3, 7],
    [5, 13, 15, 6, 9, 2, 12, 10, 11, 7, 8, 1, 4, 3, 14, 0],
    [7, 15, 5, 10, 8, 1, 6, 13, 0, 9, 3, 14, 11, 4, 2, 12],
    [12, 8, 2, 1, 13, 4, 15, 6, 7, 0, 10, 5, 3, 14, 9, 11],
    [11, 3, 5, 8, 2, 15, 10, 13, 14, 1, 7, 4, 12, 9, 6, 0],
    [6, 8, 2, 3, 9, 10, 5, 12, 1, 14, 4, 7, 11, 13, 0, 15],
    [12, 4, 6, 2, 10, 5, 11, 9, 14, 8, 13, 7, 0, 3, 15, 1]
]

def GOST_Magma_T(in_data, out_data):
    for i in range(4):
        first_part_byte = (in_data[i] & 0xf0) >> 4
        sec_part_byte = (in_data[i] & 0x0f)
        first_part_byte = Pi[i * 2][first_part_byte]
        sec_part_byte = Pi[i * 2 + 1][sec_part_byte]
        out_data[i] = (first_part_byte << 4) | sec_part_byte

def GOST_Magma_g(k, a, out_data):
    internal = [0] * 4
    out_data_32 = 0

    GOST_Magma_Add_32(a, k, internal)
    GOST_Magma_T(internal, internal)

    out_data_32 = (internal[0] << 24) + (internal[1] << 16) + (internal[2] << 8) + internal[3]
    out_data_32 = ((out_data_32 << 11) | (out_data_32 >> 21)) & 0xFFFFFFFF

    out_data[3] = out_data_32 & 0xFF
    out_data[2] = (out_data_32 >> 8) & 0xFF
    out_data[1] = (out_data_32 >> 16) & 0xFF
    out_data[0] = (out_data_32 >> 24) & 0xFF

def GOST_Magma_Add(a, b, c):
    for i in range(len(a)):
        c[i] = a[i] ^ b[i]


def GOST_Magma_G(k, a, out_data):
    a_0 = [0] * 4  # Правая часть блока
    a_1 = [0] * 4  # Левая часть блока
    G = [0] * 4

    # Разделить 64-битный входной блок на две части
    for i in range(4):
        a_0[i] = a[4 + i]
        a_1[i] = a[i]

    # Применить преобразование g
    GOST_Magma_g(k, a_0, G)

    # Применить XOR результата преобразования g к левой части блока
    GOST_Magma_Add(a_1, G, G)

    for i in range(4):
        # Скопировать значение из правой части в левую часть
        a_1[i] = a_0[i]
        # Скопировать результат сложения в правую часть блока
        a_0[i] = G[i]

    # Объединить правую и левую части в один блок
    for i in range(4):
        out_data[i] = a_1[i]
        out_data[4 + i] = a_0[i]


def GOST_Magma_G_Fin(k, a, out_data):
    a_0 = [0] * 4  # Правая часть блока
    a_1 = [0] * 4  # Левая часть блока
    G = [0] * 4

    # Разделить 64-битный входной блок на две части
    for i in range(4):
        a_0[i] = a[4 + i]
        a_1[i] = a[i]

    # Применить преобразование g
    GOST_Magma_g(k, a_0, G)

    # Применить XOR результата преобразования g к левой части блока
    GOST_Magma_Add(a_1, G, G)

    # Скопировать результат сложения в левую часть блока
    for i in range(4):
        a_1[i] = G[i]

    # Объединить правую и левую части в один блок
    for i in range(4):
        out_data[i] = a_1[i]
        out_data[4 + i] = a_0[i]


def GOST_Magma_Encrypt(blk, out_blk):
    # Первое преобразование G
    GOST_Magma_G(iter_key[0], blk, out_blk)

    # Последующие (со второго по тридцать первое) преобразования G
    for i in range(1, 31):
        GOST_Magma_G(iter_key[i], out_blk, out_blk)

    # Последнее (тридцать второе) преобразование G
    GOST_Magma_G_Fin(iter_key[31], out_blk, out_blk)


def GOST_Magma_Decript(blk, out_blk):
    # Первое преобразование G с использованием
    # тридцать второго итерационного ключа
    GOST_Magma_G(iter_key[31], blk, out_blk)
    
    # Последующие (со второго по тридцать первое) преобразования G
    # (итерационные ключи идут в обратном порядке)
    for i in range(30, 0, -1):
        GOST_Magma_G(iter_key[i], out_blk, out_blk)
    
    # Последнее (тридцать второе) преобразование G
    # с использованием первого итерационного ключа
    GOST_Magma_G_Fin(iter_key[0], out_blk, out_blk)

iter_key = [bytearray(4) for _ in range(32)]  # Инициализация ключевого расписания

def GOST_Magma_Expand_Key(key):
    # Формирование 8-ми 32-битных подключей
    for i in range(8):
        iter_key[i][:] = key[i * 4: (i + 1) * 4]


    #повторяем прошлый блок ещё 2 раза
    for j in range(2):
        for i in range(8):
            iter_key[8 * (j + 1) + i][:] = key[i * 4: (i + 1) * 4]

    for i in range(8):
        iter_key[-(i+1)][:] = iter_key[i][:]

# print("Transformation t")
def t(input_data):
    result = bytearray(4)
    GOST_Magma_T(input_data, result)
    return result

def add_xor(a,b):
    block_size=8
    c=[""]*block_size
    for i in range(block_size):
        c[i]=a[i]^b[i]
    return c



def g(k, a):
    result = bytearray(4)
    GOST_Magma_g(bytearray.fromhex(k), bytearray.fromhex(a), result)
    return result


key_example = bytearray.fromhex("ffeeddccbbaa99887766554433221100f0f1f2f3f4f5f6f7f8f9fafbfcfdfeff")
GOST_Magma_Expand_Key(key_example)
# print("Key Schedule:", [''.join(format(x, '02x') for x in subkey) for subkey in iter_key])

# A.2.4 Encryption Algorithm
def GOST_Magma_Encrypt_Example():
    plaintext = bytearray.fromhex("92def06b3c130a59")
    encrypted_block = bytearray(8)

    GOST_Magma_Encrypt(plaintext, encrypted_block)

    print("Open text:", ''.join(format(x, '02x') for x in plaintext))
    print("Encrypted Block:", ''.join(format(x, '02x') for x in encrypted_block))

GOST_Magma_Encrypt_Example()

def GOST_Magma_Decrypt_Example():
    # Шифртекст для расшифрования
    ciphertext = bytearray.fromhex("2b073f0494f372a0")
    decrypted_block = bytearray(8)

    GOST_Magma_Decript(ciphertext, decrypted_block)

    print("Ciphertext:", ''.join(format(x, '02x') for x in ciphertext))
    print("Decrypted Block:", ''.join(format(x, '02x') for x in decrypted_block))

# Пример расшифрования
GOST_Magma_Decrypt_Example()


