from setuptools import setup, Extension
from Cython.Build import cythonize

ext = [
    Extension(
        "cmmh3.cmurmur3",
        sources=[
            "cmmh3/cmurmur3.pyx",
            "cmmh3/murmur3.c",
        ],
        extra_compile_args=["-O3"],
    )
]
package_data = {"cmmh3.cmurmur3": ["*.pyi"]}
setup(
    ext_modules=cythonize(ext, language_level=3, annotate=False),
    package_data=package_data,
    packages=["cmmh3"],
)
