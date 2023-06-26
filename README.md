# FastMurmurHash3

[中文文档按此](https://github.com/dream2333/FastMurmurHash3/blob/main/README_CN.md)

`fmmh3` is a Python extension module developed using a mix of C language and Cython. It wraps the C language MurmurHash3 hash function, making it available for use in Python. Compared to the pure Python version of [MurmurHash3](https://github.com/wc-duck/pymmh3), `fmmh3` is several tens to hundreds of times faster. Compared to another C language implementation, the [mmh3](https://github.com/hajimes/mmh3) library, `fmmh3` is 1-2.5 times faster in processing medium and small texts.

## Installation

### Using pip

```bash
pip install fmmh3
```

### Using Poetry

```bash
poetry add fmmh3
```

## Benchmark Tests

We compared the performance of fmmh3, the pure Python version of MurmurHash3, and the mmh3 library bound with ctypes. Here are our test results:

| Byte String Length | MurmurHash3 (Python) | mmh3  | fmmh3  |
| ----------------- | -------------------- | ----  | ------ |
| 1                 | 1x                   | 6.27x | 15.62x |
| 10                | 1x                   | 9.43x | 23.08x |
| 512               | 1x                   | 197x  | 373x   |
| 1000              | 1x                   | 324x  | 538x   |

When the byte string size is greater than 1kb, the Python version of the algorithm exceeds the test time. Therefore, we excluded the Python version of the test in data above 1kb. Here is the speed difference between mmh3 and fmmh3:

| Byte String Length | mmh3 | fmmh3 |
| ----------------- | ---- | ----- |
| 1                 | 1x     |  2.51x |
| 10                |  1x    |  2.44x |
| 100               |   1x   |  2.36x |
| 512               |   1x   |  1.90x |
| 1000              | 1x     | 1.65x |
| 5000              | 1x     | 1.18x |
| 10000             | 1x     | 1.09x |

As we can see, fmmh3 has a significant performance advantage.

## Function Usage

fmmh3 provides three functions to calculate MurmurHash3 hash values: `hash32_x86`, `hash128_x86`, and `hash128_x64`:

```python
from fmmh3 import hash32_x86, hash128_x86, hash128_x64

key = b"hello world"
seed = 0

hash32_value = hash32_x86(key, seed)
hash128_x86_value = hash128_x86(key, seed)
hash128_x64_value = hash128_x64(key, seed)
```

The function returns a hash value integer. `key` is the byte string to calculate the hash value, and `seed` is the hash seed, usually a prime number.

## Author

This project was developed by Dream2333.

The MurmurHash algorithm was originally proposed by [Austin Appleby](https://github.com/aappleby/smhasher/blob/master/src/MurmurHash3.cpp).

The C version of the algorithm comes from [PeterScott](https://github.com/PeterScott/murmur3).

The Python version used in the benchmark test comes from [wc-duck](https://github.com/wc-duck/pymmh3).

## Contribution

If you want to contribute to this project, you can:

- Report issues or suggest improvements on [GitHub](https://github.com/dream2333/FastMurmurHash3/issues).
- Submit [pull requests](https://github.com/dream2333/FastMurmurHash3/pulls) to fix issues or add new features.
- Share this project to let more people know about it.

## License

This project is licensed under the [MIT](https://github.com/dream2333/FastMurmurHash3/blob/main/LICENSE) license.