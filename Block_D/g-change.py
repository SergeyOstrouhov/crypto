def mod2in32(a, b, c):
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

def T_func(in_data, out_data):
    for i in range(4):
        first_part_byte = (in_data[i] & 0xf0) >> 4
        sec_part_byte = (in_data[i] & 0x0f)
        first_part_byte = Pi[i * 2][first_part_byte]
        sec_part_byte = Pi[i * 2 + 1][sec_part_byte]
        out_data[i] = (first_part_byte << 4) | sec_part_byte

def g_func(k, a, out_data):
    internal = [0] * 4
    out_data_32 = 0

    mod2in32(a, k, internal)
    T_func(internal, internal)

    out_data_32 = (internal[0] << 24) + (internal[1] << 16) + (internal[2] << 8) + internal[3]
    out_data_32 = ((out_data_32 << 11) | (out_data_32 >> 21)) & 0xFFFFFFFF

    out_data[3] = out_data_32 & 0xFF
    out_data[2] = (out_data_32 >> 8) & 0xFF
    out_data[1] = (out_data_32 >> 16) & 0xFF
    out_data[0] = (out_data_32 >> 24) & 0xFF

def add(a, b, c):
    for i in range(len(a)):
        c[i] = a[i] ^ b[i]


def g_func(k, a, out_data):
    a_0 = [0] * 4  # Right half of the block
    a_1 = [0] * 4  # Left half of the block
    G = [0] * 4

    # Divide the 64-bit input block into two parts
    for i in range(4):
        a_0[i] = a[4 + i]
        a_1[i] = a[i]

    # Apply the g transformation
    g_func(k, a_0, G)
    
    # XOR the result of the g transformation with the left half of the block
    add(a_1, G, G)

    for i in range(4):
        # Copy the value from the right half to the left half
        a_1[i] = a_0[i]
        # Copy the result of the addition to the right half of the block
        a_0[i] = G[i]

    # Combine the right and left halves into a single block
    for i in range(4):
        out_data[i] = a_1[i]
        out_data[4 + i] = a_0[i]


def g_func_Fin(k, a, out_data):
    a_0 = [0] * 4  # Right half of the block
    a_1 = [0] * 4  # Left half of the block
    G = [0] * 4

    # Divide the 64-bit input block into two parts
    for i in range(4):
        a_0[i] = a[4 + i]
        a_1[i] = a[i]

    # Apply the g transformation
    g_func(k, a_0, G)

    # XOR the result of the g transformation with the left half of the block
    add(a_1, G, G)

    # Copy the result of add to the left half of the block
    for i in range(4):
        a_1[i] = G[i]

    # Combine the right and left halves into a single block
    for i in range(4):
        out_data[i] = a_1[i]
        out_data[4 + i] = a_0[i]


def Encrypt(blk, out_blk):
    # First G transformation
    g_func(iter_key[0], blk, out_blk)

    # Subsequent (from the second to the thirty-first) G transformations
    for i in range(1, 31):
        g_func(iter_key[i], out_blk, out_blk)

    # Last (thirty-second) G transformation
    g_func_Fin(iter_key[31], out_blk, out_blk)


def Decript(blk, out_blk):
    # Первое преобразование G с использованием
    # тридцать второго итерационного ключа
    g_func(iter_key[31], blk, out_blk)
    
    # Последующие (со второго по тридцать первое) преобразования G
    # (итерационные ключи идут в обратном порядке)
    for i in range(30, 0, -1):
        g_func(iter_key[i], out_blk, out_blk)
    
    # Последнее (тридцать второе) преобразование G
    # с использованием первого итерационного ключа
    g_func_Fin(iter_key[0], out_blk, out_blk)

iter_key = [bytearray(4) for _ in range(32)]  # Initialization of the key schedule

def Expand_Key(key):
    # Forming eight 32-bit subkeys in order from the first to the eighth
    for i in range(8):
        iter_key[i][:] = key[i * 4: (i + 1) * 4]

    # Repeating the previous block of code two more times
    for j in range(2):
        for i in range(8):
            iter_key[8 * (j + 1) + i][:] = key[i * 4: (i + 1) * 4]

    for i in range(8):
        iter_key[-(i+1)][:] = iter_key[i][:]

print("Transformation t")
# A.2.1 Transformation t
def t(input_data):
    result = bytearray(4)
    T_func(input_data, result)
    return result

# Example 1
input_data_1 = bytearray.fromhex("fdb97531")
output_1 = t(input_data_1)
print("t(fdb97531) =", ''.join(format(x, '02x') for x in output_1))

# Example 2
input_data_2 = output_1
output_2 = t(input_data_2)
print("t(2a196f34) =", ''.join(format(x, '02x') for x in output_2))

# Example 3
input_data_3 = output_2
output_3 = t(input_data_3)
print("t(ebd9f03a) =", ''.join(format(x, '02x') for x in output_3))

# Example 4
input_data_4 = output_3
output_4 = t(input_data_4)
print("t(b039bb3d) =", ''.join(format(x, '02x') for x in output_4))


print("Transformation g")
# A.2.2 Transformation g
def g(k, a):
    result = bytearray(4)
    g_func(bytearray.fromhex(k), bytearray.fromhex(a), result)
    return result

# Example 1
output_g_1 = g("87654321", "fedcba98")
print("g[87654321](fedcba98) =", ''.join(format(x, '02x') for x in output_g_1))

# Example 2
output_g_2 = g("fdcbc20c", "87654321")
print("g[fdcbc20c](87654321) =", ''.join(format(x, '02x') for x in output_g_2))

# Example 3
output_g_3 = g("7e791a4b", "fdcbc20c")
print("g[7e791a4b](fdcbc20c) =", ''.join(format(x, '02x') for x in output_g_3))

# Example 4
output_g_4 = g("c76549ec", "7e791a4b")
print("g[c76549ec](7e791a4b) =", ''.join(format(x, '02x') for x in output_g_4))


print("Key Expansion Algorithm")
# A.2.3 Key Expansion Algorithm
key_example = bytearray.fromhex("ffeeddccbbaa99887766554433221100f0f1f2f3f4f5f6f7f8f9fafbfcfdfeff")
Expand_Key(key_example)
print("Key Schedule:", [''.join(format(x, '02x') for x in subkey) for subkey in iter_key])

# A.2.4 Encryption Algorithm
def Encrypt_Example():
    plaintext = bytearray.fromhex("fedcba9876543210")
    encrypted_block = bytearray(8)

    Encrypt(plaintext, encrypted_block)

    print("Plaintext:", ''.join(format(x, '02x') for x in plaintext))
    print("Encrypted Block:", ''.join(format(x, '02x') for x in encrypted_block))

Encrypt_Example()

def Decrypt_Example():
    # Шифртекст для расшифрования
    ciphertext = bytearray.fromhex("4ee901e5c2d8ca3d")
    decrypted_block = bytearray(8)

    Decript(ciphertext, decrypted_block)
    
    print("Ciphertext:", ''.join(format(x, '02x') for x in ciphertext))
    print("Decrypted Block:", ''.join(format(x, '02x') for x in decrypted_block))

# Пример расшифрования
Decrypt_Example()
