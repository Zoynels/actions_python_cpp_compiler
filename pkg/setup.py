# -*- coding: utf-8 -*-

import ast
import os
import platform
import sys

# first import setuptools
# second import distutils
import setuptools  # noqa
from distutils.core import Extension
from distutils.core import setup


def get_version():
    """Return version tuple of strings."""
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
    if __version__ == "" and __version_cpp__ == "":
        raise ValueError(
            "Can't detect __version__ of main module and __version_cpp__ of cpp module!")
    if __version__ == "":
        raise ValueError("Can't detect __version__ of main module!")
    if __version_cpp__ == "":
        raise ValueError("Can't detect __version_cpp__ of cpp module!")

    return __version__, __version_cpp__


def get_fname_path(start_path, fname):
    for dp, dn, filenames in os.walk(start_path):
        for f in filenames:
            if str(f).lower() == fname:
                return os.path.abspath(dp)
    msg = (f"Can't find {fname} in folder {start_path} and its subfolders! " +
           "Please check 'pythonLocation' environment variable!")
    raise ValueError(msg)


cpython_include = []
if (os.environ.get("pythonLocation", "") != ""):
    cpython_include.append(get_fname_path(os.path.join(os.environ["pythonLocation"]), "python.h"))
    cpython_include.append(get_fname_path(os.path.join(os.environ["pythonLocation"]), "pyconfig.h"))
else:
    raise ValueError("Please set 'pythonLocation' environment variable where Python.h and " +
                     "python3.lib/libpython3.so exist! Files will be searched recursively is this folder.")

cpython_library = []
if (os.environ.get("pythonLocation", "") != ""):
    if sys.platform == "linux" or platform == "linux2":
        cpython_include.append(get_fname_path(os.path.join(os.environ["pythonLocation"]), "libpython3.so"))
    elif sys.platform == "darwin":
        cpython_include.append(get_fname_path(os.path.join(os.environ["pythonLocation"]), "libpython3.so"))
    elif sys.platform == "win32":
        cpython_include.append(get_fname_path(os.path.join(os.environ["pythonLocation"]), "python3.lib"))
    else:
        raise RuntimeError(f"Unknown platform: {sys.platform}")
else:
    raise ValueError("Please set 'pythonLocation' environment variable where Python.h and " +
                     "python3.lib/libpython3.so exist! Files will be searched recursively is this folder.")

if sys.platform == "linux" or platform == "linux2":
    extra_compile_args = ["-std=c++17"]
elif sys.platform == "darwin":
    extra_compile_args = ["-std=c++17"]
elif sys.platform == "win32":
    extra_compile_args = [
        "/std:c++17",
        "/MP",
        "/WX-",
        "/W4",
        "/sdl",
        "/Zi",
        "/Ox",
        "/O2"]  # Visual Studio 2019

test_mode = True
if test_mode:
    sources = ["src/python_onefile.cpp"]


ext_modules = [
    Extension(
        "actions_python_cpp_compiler.cpp_module_test",  # save to 'folder.filename'
        sources=sources,  # files to compile (all cpp files in project)
        include_dirs=list(set(cpython_include)) + ["../external/pybind11/include/pybind11/"],
        library_dirs=list(set(cpython_library)),
        runtime_library_dirs=[],
        libraries=[],
        language="c++",
        extra_compile_args=extra_compile_args,
    ),
]

long_description = ""
long_description_content_type = "text/markdown"
with open("../readme.md") as readme:
    long_description = readme.read()
    long_description_content_type = "text/markdown"


setup(
    name="actions_python_cpp_compiler",
    version=get_version()[0],
    url="https://github.com/Zoynels/actions_python_cpp_compiler",
    author="Zoynels",
    author_email="zoynels@gmail.com",
    description=("GitHub Actions to build/install/test for c++ module with pybind11:" +
                 f"wrapper version {get_version()[0]} and cpp-module version {get_version()[1]}"),
    long_description=long_description,
    long_description_content_type=long_description_content_type,
    license="GNU Affero General Public License v3",
    classifiers=[
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: C++",
        "Programming Language :: Pybind11",
        "License :: OSI Approved :: GNU Affero General Public License v3"],
    keywords="pybind11, c++, github, actions",
    ext_modules=ext_modules,
    packages=["actions_python_cpp_compiler"],
    package_dir={
        "actions_python_cpp_compiler": "python"})
