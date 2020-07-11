from . import cpp_module_test
__version__ = cpp_module_test.__version__

def echo(value):
    return cpp_module_test.echo(str(value))

def run_tests(fname=None):
    import sys
    import pathlib
    import subprocess

    test_files = []
    if fname is None:
        test_files.append(str(pathlib.Path(__file__).parent / "test_ping.py"))
    elif pathlib.Path(fname).is_file():
        test_files.append(str(fname))
    elif (pathlib.Path(__file__).parent / fname).is_file():
        test_files.append(str(pathlib.Path(__file__).parent / fname))


    child = subprocess.Popen(["pytest", "-vv", "--capture=tee-sys", "-r", "s"] + test_files, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    streamdata = child.communicate()
    for ch in [streamdata[0].split(b"\n"), streamdata[1].split(b"\n")]:
        for line in ch:
            try:
                print(line.decode().strip())
            except:
                try:
                    print(line.strip())
                except:
                    print(line)
    assert child.returncode == 0
