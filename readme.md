### Example of GitHub actions with python and c++ module.

This is not the best solution, but it works!

### How to release
We have several versions (changes could be only in the wrapper, but the cpp-module could not be changed)
1. Version of cpp-module file (`pkg/src/python_onefile.cpp`)
2. Version of python wrapper on cpp-module file (`pkg/python/__init__.py`)

If cpp-module changes also should be changed module version, but if the wrapper is changed and cpp-module is not changed, then cpp-module version could be not changed.

3. Change `release_notes.md` with changes.
4. Create a tag that starts with `v`, e.y. `v0.0.1` or `version 0.0.1 release` or `very good` (also will trigger as it starts with `v`).
5. Push
6. Goto GitHub Actions page and choose workflow for your purpose: build and create a record on the release page.
7. If you want to upload to the PyPI server, then add a user/password/token as documented in https://pypi.org/manage/account/token/.
