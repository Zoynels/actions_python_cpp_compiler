### Build
* Rewrite setup.py with pybind11 examples without complex code
* Remove the pybind11 submodule (need to install before build)

### Changes in GitHub Actions
* Refactor workflow (build process use GitHub actions)
* Build packages on different platforms and python versions
* Create Release with workflow
* Upload Release to https://pypi.org/
