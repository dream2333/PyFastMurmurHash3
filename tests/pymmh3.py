'''

'''
def hash128_x64(key, seed):
    def fmix(k):
        k ^= k >> 33
        k = (k * 0xFF51AFD7ED558CCD) & 0xFFFFFFFFFFFFFFFF
        k ^= k >> 33
        k = (k * 0xC4CEB9FE1A85EC53) & 0xFFFFFFFFFFFFFFFF
        k ^= k >> 33
        return k

    length = len(key)
    nblocks = int(length / 16)

    h1 = seed
    h2 = seed

    c1 = 0x87C37B91114253D5
    c2 = 0x4CF5AD432745937F

    for block_start in range(0, nblocks * 8, 8):
        k1 = (
            key[2 * block_start + 7] << 56
            | key[2 * block_start + 6] << 48
            | key[2 * block_start + 5] << 40
            | key[2 * block_start + 4] << 32
            | key[2 * block_start + 3] << 24
            | key[2 * block_start + 2] << 16
            | key[2 * block_start + 1] << 8
            | key[2 * block_start + 0]
        )

        k2 = (
            key[2 * block_start + 15] << 56
            | key[2 * block_start + 14] << 48
            | key[2 * block_start + 13] << 40
            | key[2 * block_start + 12] << 32
            | key[2 * block_start + 11] << 24
            | key[2 * block_start + 10] << 16
            | key[2 * block_start + 9] << 8
            | key[2 * block_start + 8]
        )

        k1 = (c1 * k1) & 0xFFFFFFFFFFFFFFFF
        k1 = (k1 << 31 | k1 >> 33) & 0xFFFFFFFFFFFFFFFF
        k1 = (c2 * k1) & 0xFFFFFFFFFFFFFFFF
        h1 ^= k1

        h1 = (h1 << 27 | h1 >> 37) & 0xFFFFFFFFFFFFFFFF
        h1 = (h1 + h2) & 0xFFFFFFFFFFFFFFFF
        h1 = (h1 * 5 + 0x52DCE729) & 0xFFFFFFFFFFFFFFFF

        k2 = (c2 * k2) & 0xFFFFFFFFFFFFFFFF
        k2 = (k2 << 33 | k2 >> 31) & 0xFFFFFFFFFFFFFFFF
        k2 = (c1 * k2) & 0xFFFFFFFFFFFFFFFF
        h2 ^= k2

        h2 = (h2 << 31 | h2 >> 33) & 0xFFFFFFFFFFFFFFFF
        h2 = (h1 + h2) & 0xFFFFFFFFFFFFFFFF
        h2 = (h2 * 5 + 0x38495AB5) & 0xFFFFFFFFFFFFFFFF

    tail_index = nblocks * 16
    k1 = 0
    k2 = 0
    tail_size = length & 15

    if tail_size >= 15:
        k2 ^= key[tail_index + 14] << 48
    if tail_size >= 14:
        k2 ^= key[tail_index + 13] << 40
    if tail_size >= 13:
        k2 ^= key[tail_index + 12] << 32
    if tail_size >= 12:
        k2 ^= key[tail_index + 11] << 24
    if tail_size >= 11:
        k2 ^= key[tail_index + 10] << 16
    if tail_size >= 10:
        k2 ^= key[tail_index + 9] << 8
    if tail_size >= 9:
        k2 ^= key[tail_index + 8]

    if tail_size > 8:
        k2 = (k2 * c2) & 0xFFFFFFFFFFFFFFFF
        k2 = (k2 << 33 | k2 >> 31) & 0xFFFFFFFFFFFFFFFF
        k2 = (k2 * c1) & 0xFFFFFFFFFFFFFFFF
        h2 ^= k2

    if tail_size >= 8:
        k1 ^= key[tail_index + 7] << 56
    if tail_size >= 7:
        k1 ^= key[tail_index + 6] << 48
    if tail_size >= 6:
        k1 ^= key[tail_index + 5] << 40
    if tail_size >= 5:
        k1 ^= key[tail_index + 4] << 32
    if tail_size >= 4:
        k1 ^= key[tail_index + 3] << 24
    if tail_size >= 3:
        k1 ^= key[tail_index + 2] << 16
    if tail_size >= 2:
        k1 ^= key[tail_index + 1] << 8
    if tail_size >= 1:
        k1 ^= key[tail_index + 0]

    if tail_size > 0:
        k1 = (k1 * c1) & 0xFFFFFFFFFFFFFFFF
        k1 = (k1 << 31 | k1 >> 33) & 0xFFFFFFFFFFFFFFFF
        k1 = (k1 * c2) & 0xFFFFFFFFFFFFFFFF
        h1 ^= k1

    h1 ^= length
    h2 ^= length

    h1 = (h1 + h2) & 0xFFFFFFFFFFFFFFFF
    h2 = (h1 + h2) & 0xFFFFFFFFFFFFFFFF

    h1 = fmix(h1)
    h2 = fmix(h2)

    h1 = (h1 + h2) & 0xFFFFFFFFFFFFFFFF
    h2 = (h1 + h2) & 0xFFFFFFFFFFFFFFFF

    return h2 << 64 | h1
