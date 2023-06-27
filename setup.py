from setuptools import Extension, Distribution
from Cython.Build import cythonize

compile_args = ["-O3", "-msse", "-msse2", "-mfma", "-mfpmath=sse"]
link_args = []
include_dirs = []

ext = [
    Extension(
        "*",
        sources=[
            "fmmh3/*.pyx",
            "fmmh3/includes/murmur3.c",
        ],
        # libraries=["murmur3"],
        library_dirs=["fmmh3/includes"],
        include_dirs=["fmmh3/includes"],
        extra_compile_args=compile_args,
    )
]

ext_modules = cythonize(
    ext,
    language_level=3,
    annotate=False,
    force=True,
)
dist = Distribution({"ext_modules": ext_modules})
build_ext_cmd = dist.get_command_obj("build_ext")
build_ext_cmd.ensure_finalized()
build_ext_cmd.inplace = 1
build_ext_cmd.run()
