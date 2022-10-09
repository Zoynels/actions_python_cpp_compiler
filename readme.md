### Example of github actions with python and c++ module.

This is not the best solution, but it works!
![Python + CPP package](https://github.com/Zoynels/actions_python_cpp_compiler/workflows/Python%20+%20CPP%20package/badge.svg)

### Update submodules
```
cd external/pybind11
git checkout master
git pull
cd ../..
git commit -am "Pulled down update to external/pybind11"
```

### How to release
We have several version (changes could be only in wrapper, but cpp-module could not be changed)
1. Version of cpp-module file (`pkg/src/python_onefile.cpp`)
2. Version of python wrapper on cpp-module file (`pkg/python/__init__.py`)

If cpp module changes also should be changed module version, but if wrapper changed and cpp-module not changed, then cpp-module version could be not changed.

3. Change `release_notes.md` with changes.
4. Create tag starts with `v`, e.y. `v0.0.1` or `version 0.0.1 release` or `very good` (also will trigger as it starts with `v`).
5. Push
6. GitHub Action will restart build and create record on release page.
