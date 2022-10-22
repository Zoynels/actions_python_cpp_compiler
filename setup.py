# -*- coding: utf-8 -*-

import ast
import glob

from pybind11.setup_helpers import Pybind11Extension
from pybind11.setup_helpers import build_ext

from setuptools import setup


def get_version():
    """Return version tuple of strings."""
    __version__ = ""
    __version_cpp__ = ""

    fname_py = "pkg/python/__init__.py"
    fname_cpp = "pkg/src/python_onefile.cpp"

    with open(fname_py) as input_file:
        for line in input_file:
            if line.startswith("__version__"):
                __version__ = ast.parse(line).body[0].value.s  # type: ignore
                break

    with open(fname_cpp) as input_file:
        for line in input_file:
            if "__version__" in line:
                L = line.strip()
                pos = L.find("__version__")
                pos = L.find("=", pos)
                L = "__version_cpp__ " + L[pos:]
                __version_cpp__ = ast.parse(L).body[0].value.s  # type: ignore
                break
    if __version__ == "" and __version_cpp__ == "":
        raise ValueError("Can't detect __version__ of main module and __version_cpp__ of cpp module!")
    if __version__ == "":
        raise ValueError("Can't detect __version__ of main module!")
    if __version_cpp__ == "":
        raise ValueError("Can't detect __version_cpp__ of cpp module!")

    return __version__, __version_cpp__


sources = sorted(glob.glob("pkg/src/**/*.cpp", recursive=True))

ext_modules = [
    Pybind11Extension("actions_python_cpp_compiler.cpp_module_test", sources)
]


long_description = ""
long_description_content_type = "text/markdown"
try:
    with open("readme.md") as readme:
        long_description = readme.read()
        long_description_content_type = "text/markdown"
except BaseException:
    print("readme.md not found")

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
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: C++",
        "License :: OSI Approved :: GNU Affero General Public License v3"],
    keywords="pybind11, c++, github, actions",
    cmdclass={"build_ext": build_ext},
    ext_modules=ext_modules,
    packages=["actions_python_cpp_compiler"],
    package_dir={
        "actions_python_cpp_compiler": "pkg/python"})
