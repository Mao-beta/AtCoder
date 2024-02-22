
from distutils.core import setup, Extension
module = Extension(
    "cppset",
    sources=["set_wrapper.cpp"],
    extra_compile_args=["-O3", "-march=native", "-std=c++14"]
)
setup(
    name="SetMethod",
    version="0.2.1",
    description="wrapper for C++ set",
    ext_modules=[module]
)
