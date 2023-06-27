import fmmh3
import mmh3

import time

key = b"n" * 5000


def test_func(func, key, times, **other_kwargs):
    start = time.perf_counter()
    for i in range(times):
        func(key, 13, **other_kwargs)
    end = time.perf_counter()
    return end - start


# print("fmmh3:", test_func(fmmh3.hash128_x64, key))
# print("mmh3:", test_func(mmh3.hash128, key, signed=False))
print(
    test_func(mmh3.hash128, key, 10_000_00, signed=False)
    / test_func(fmmh3.hash128_x64, key, 10_000_00)
)
