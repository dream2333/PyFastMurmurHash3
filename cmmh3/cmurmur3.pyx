
cpdef uint128 hash128_x64(char *key,unsigned int seed):
    cdef uint128 _hash
    MurmurHash3_x64_128(key, strlen(key), seed, &_hash)
    return _hash

cpdef uint128 hash128_x86(char *key,unsigned int seed):
    cdef uint128 _hash
    MurmurHash3_x64_128(key, strlen(key), seed, &_hash)
    return _hash

cpdef uint128 hash32_x86(char *key,unsigned int seed):
    cdef uint32 _hash
    MurmurHash3_x64_128(key, strlen(key), seed, &_hash)
    return _hash

