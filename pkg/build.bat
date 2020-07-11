RMDIR "build" /S /Q
RMDIR "lib" /S /Q
RMDIR "dist" /S /Q

setup.py build --build-lib=lib bdist_wheel

pause
