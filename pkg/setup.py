#!/usr/bin/python3
#-*- coding: utf-8 -*-

from setuptools import setup
from distutils.core import setup, Extension

import os, sys, platform
import ast


def get_version():
    """Return version tuple of strings."""
    import os
    __version__ = ""
    __version_cpp__ = ""
    with open("python/__init__.py") as input_file:
        for line in input_file:
            if line.startswith("__version__"):
                __version__ = ast.parse(line).body[0].value.s  # type: ignore
                break
    with open("src/python_onefile.cpp") as input_file:
        for line in input_file:
            if "__version__" in line:
                L = line.strip()
                pos = L.find("__version__")
                pos = L.find("=", pos)
                L = "__version_cpp__ " + L[pos:]
                __version_cpp__ = ast.parse(L).body[0].value.s  # type: ignore
                break
    return __version__, __version_cpp__


def get_fname_path(start_path, fname):
    for dp, dn, filenames in os.walk(start_path):
        for f in filenames:
            if str(f).lower() == fname:
                return os.path.abspath(dp)


cpython_include = []
if (os.environ.get("pythonLocation", "") != ""):
    cpython_include.append(get_fname_path(os.path.join(os.environ["pythonLocation"]), "python.h"))
    cpython_include.append(get_fname_path(os.path.join(os.environ["pythonLocation"]), "pyconfig.h"))
elif (sys.version_info[0] == 3) and  (sys.version_info[1] == 7):
    cpython_include.append(get_fname_path("../external/cpython_3_7_7", "python.h"))
    cpython_include.append(get_fname_path("../external/cpython_3_7_7", "pyconfig.h"))
elif (sys.version_info[0] == 3) and  (sys.version_info[1] == 8):
    cpython_include.append(get_fname_path("../external/cpython_3_8_3", "python.h"))
    cpython_include.append(get_fname_path("../external/cpython_3_8_3", "pyconfig.h"))
else:
    raise NotImplementedError(f"Not implemented on {sys.version_info}")

cpython_library = []
if (os.environ.get("pythonLocation", "") != ""):
    cpython_include.append(get_fname_path(os.path.join(os.environ["pythonLocation"]), "python3.lib")) # for windows
    cpython_include.append(get_fname_path(os.path.join(os.environ["pythonLocation"]), "libpython3.so")) # for linux
elif sys.platform == "linux" or platform == "linux2":
    raise NotImplementedError("Not implemented on Linux")
elif sys.platform == "darwin":
    raise NotImplementedError("Not implemented on OS X")
elif sys.platform == "win32":
    if platform.architecture()[0] == "32bit":
        if (sys.version_info[0] == 3) and  (sys.version_info[1] == 7):
            cpython_library.append("../external/cpython_3_7_7/PCbuild/win32/")
        elif (sys.version_info[0] == 3) and  (sys.version_info[1] == 8):
            cpython_library.append("../external/cpython_3_8_3/PCbuild/win32/")
    if platform.architecture()[0] == "64bit":
        if (sys.version_info[0] == 3) and  (sys.version_info[1] == 7):
            cpython_library.append("../external/cpython_3_7_7/PCbuild/amd64/")
        elif (sys.version_info[0] == 3) and  (sys.version_info[1] == 8):
            cpython_library.append("../external/cpython_3_8_3/PCbuild/amd64/")

if sys.platform == "linux" or platform == "linux2":
    extra_compile_args = ["-std=c++17"]
elif sys.platform == "darwin":
    extra_compile_args = ["-std=c++17"]
elif sys.platform == "win32":
    extra_compile_args = ["/std:c++17", "/MP", "/WX-", "/W4", "/sdl", "/Zi", "/Ox", "/O2"] # Visual Studio 2019

test_mode = True
if test_mode:
    sources = ["src/python_onefile.cpp"]


ext_modules = [
    Extension(
        "actions_python_cpp_compiler.cpp_module_test", # save to 'folder.filename'
        sources=sources, # files to compile (all cpp files in project)
        include_dirs=list(set(cpython_include)) + [
                     "../external/pybind11/include/pybind11/", # instead hard dependency for pybin11 could be used 'pybind11.get_include()' function
                     ],
        library_dirs=list(set(cpython_library)),
        runtime_library_dirs=[],
        libraries=[],
        language="c++",
        extra_compile_args=extra_compile_args, 
    ),
]

setup(
    name="actions_python_cpp_compiler",
    version=get_version()[0],
    url="https://github.com/Zoynels/actions_python_cpp_compiler",
    author="Zoynels",
    author_email="zoynels@gmail.com",
    description=f"actions_python_cpp_compiler: wrapper version {get_version()[0]} and cpp-module version {get_version()[1]}",
    ext_modules=ext_modules,
    packages=["actions_python_cpp_compiler"],
    package_dir = {"actions_python_cpp_compiler": "lib" , "actions_python_cpp_compiler":"python"}
)
