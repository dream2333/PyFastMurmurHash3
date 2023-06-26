# FastMurmurHash3

`fmmh3` 是一个使用 C 语言和 Cython 混合开发的 Python 扩展模块，它对 C 语言的 MurmurHash3 哈希函数进行了包装，使其能够在 Python 中使用。相比纯 Python 版本的 [MurmurHash3](https://github.com/wc-duck/pymmh3)，`fmmh3` 的性能要快上几十至上百倍不等。相比于另一个c语言实现 [mmh3](https://github.com/hajimes/mmh3) 库，在处理中型及小型文本上，`fmmh3` 的性能要快上 1-2.5 倍不等。

## 安装

### 使用 pip

```bash
pip install fmmh3
```

### 使用 Poetry

```bash
poetry add fmmh3
```

## 基准测试

我们对 fmmh3、纯 Python 版本的 MurmurHash3 和 ctypes 绑定的 mmh3 库进行了性能对比。以下是我们的测试结果：

| 字节串长度  | MurmurHash3 (Python) | mmh3  | fmmh3  |
| -------- | -------------------- | ----  | ------ |
| 1        | 1x                   | 6.27x | 15.62x |
| 10       | 1x                   | 9.43x | 23.08x |
| 512      | 1x                   | 197x  | 373x   |
| 1000    | 1x                   | 324x  | 538x   |

当字节串大小大于1kb时，python版本的算法超出测试时间。因此我们在1kb以上数据中排除了python版本的测试，以下为mmh3与fmmh3的速度差距：

| 字节串长度 | mmh3 | fmmh3 |
| -------- | ---- | ----- |
| 1       | 1x     |  2.51x |
| 10      |  1x    |  2.44x |
| 100     |   1x   |  2.36x |
| 512     |   1x   |  1.90x |
| 1000     | 1x     | 1.65x |
| 5000     | 1x     | 1.18x |
| 10000     | 1x     | 1.09x |

我们可以看到，fmmh3 具有显著的性能优势。

## 函数用法

fmmh3 提供了三个函数来计算 MurmurHash3 哈希值：`hash32_x86`、`hash128_x86` 和 `hash128_x64` ：

```python
from fmmh3 import hash32_x86, hash128_x86, hash128_x64

key = b"hello world"
seed = 0

hash32_value = hash32_x86(key, seed)
hash128_x86_value = hash128_x86(key, seed)
hash128_x64_value = hash128_x64(key, seed)
```

函数返回一个哈希值整数。`key` 是要计算哈希值的字节串，`seed` 是哈希种子，一般为素数

## 作者

本项目由 Dream2333 开发

MurmurHash 算法最初由 [Austin Appleby](https://github.com/aappleby/smhasher/blob/master/src/MurmurHash3.cpp) 提出

C 版本算法来源于 [PeterScott](https://github.com/PeterScott/murmur3)

基准测试中使用的Python版本来源于 [wc-duck](https://github.com/wc-duck/pymmh3)

## 贡献

如果你想为这个项目做出贡献，你可以：

- 在 GitHub 上报告问题 [issues](https://github.com/dream2333/FastMurmurHash3/issues) 或提出建议。
- 提交 [pull](https://github.com/dream2333/FastMurmurHash3/pulls) 请求来修复问题或添加新功能。
- 分享这个项目，让更多的人知道它。

## 许可证

这个项目使用 [MIT](https://github.com/dream2333/FastMurmurHash3/blob/main/LICENSE) 许可证。