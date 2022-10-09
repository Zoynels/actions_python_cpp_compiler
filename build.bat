RMDIR "build" /S /Q
RMDIR "lib" /S /Q
RMDIR "dist" /S /Q

python -m setup.py build --build-lib=lib bdist_wheel

pause
