### Example of github actions with python and c++ module.

This is not the best solution, but it works!
![Python + CPP package](https://github.com/Zoynels/actions_python_cpp_compiler/workflows/Python%20+%20CPP%20package/badge.svg)

We have several version (changes could be only in wrapper, but cpp-module could not be changed)
1. Version of cpp-module file
2. Version of wrapper on cpp-module file (module version)

If cpp module changes also should be changed module version, but if wrapper changed and cpp-module not changed, then cpp-module version could be not changed.
