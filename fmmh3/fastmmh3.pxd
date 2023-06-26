cdef extern from "<stdint.h>":
    ctypedef int uint128 "__uint128_t"
    ctypedef int uint32 "__uint32_t"

cdef extern from "<string.h>":
    int strlen(const char *s)

cdef extern from "murmur3.h":
    void MurmurHash3_x86_32 (const void *key, int _len, uint32 seed, void *out)
    void MurmurHash3_x86_128(const void *key, int _len, uint32 seed, void *out)
    void MurmurHash3_x64_128(const void *key, int _len, uint32 seed, void *out)