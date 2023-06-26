from cmmh3.cmurmur3 import hash128_x64, hash128_x86, hash32_x86
from mmh3 import hash128
import time


def caculate_time(func):
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        func(*args, **kwargs)
        end = time.perf_counter()
        return end - start

    return wrapper


def test_func(func, key=b"hello world"):
    @caculate_time
    def wrapper(*args, **kwargs):
        for i in range(10000000):
            func(*args, **kwargs)

    return wrapper(key, 13)


print(test_func(hash128_x64))
