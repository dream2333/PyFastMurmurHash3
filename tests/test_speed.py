from cmmh3.cmurmur3 import hash128_x64, hash128_x86,hash32_x86
import mmh3
import time

# print("==============mmh3==============")
# start = time.time()
# for i in range(10000000):
#     mmh3.hash128(b"hello world", 13, False)
# end = time.time()
# print("hash128: ", end - start)

# start = time.time()
# for i in range(10000000):
#     mmh3.hash64(b"hello world", 13, False)
# end = time.time()
# print("hash64: ", end - start)

print("==============cmmh3==============")
start = time.time()
for i in range(10000000):
    hash128_x64(b"hello world", 13)
end = time.time()
print("hash128_x64: ", end - start)


start = time.time()
for i in range(10000000):
    hash128_x86(b"hello world", 13)
end = time.time()
print("hash128_x86: ", end - start)


start = time.time()
for i in range(10000000):
    hash32_x86(b"hello world", 13)
end = time.time()
print("hash32_x86: ", end - start)
