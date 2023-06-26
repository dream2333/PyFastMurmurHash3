import os
import shutil
from setuptools import setup, Extension, Distribution
from Cython.Build import cythonize, build_ext

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

ext_modules = cythonize(ext, language_level=3, annotate=False)
dist = Distribution({"ext_modules": ext_modules})
cmd = build_ext(dist)
cmd.ensure_finalized()
cmd.run()

# Copy the extensions into the root directory so they can be imported
for output in cmd.get_outputs():
    relative_extension = os.path.relpath(output, cmd.build_lib)
    shutil.copyfile(output, relative_extension)
