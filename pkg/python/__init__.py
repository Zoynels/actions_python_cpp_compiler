from . import cpp_module_test

__version_cpp__ = cpp_module_test.__version__
__version__ = "0.0.1"


def echo(value):
    return cpp_module_test.echo(str(value))


def run_tests(fname=None):
    import pathlib
    import subprocess

    test_files = []
    if fname is None:
        test_files.append(pathlib.Path(__file__).parent / "test_ping.py")
    elif pathlib.Path(fname).is_file():
        test_files.append(fname)
    elif (pathlib.Path(__file__).parent / fname).is_file():
        test_files.append(pathlib.Path(__file__).parent / fname)

    # py37 not support pathlib.Path in subprocess
    test_files = [str(fname) for fname in test_files]
    child = subprocess.Popen(["pytest",
                              "-vv",
                              "--capture=tee-sys",
                              "-r",
                              "s"] + test_files,
                             stdout=subprocess.PIPE,
                             stderr=subprocess.PIPE)
    streamdata = child.communicate()
    for ch in [streamdata[0].split(b"\n"), streamdata[1].split(b"\n")]:
        for line in ch:
            try:
                print(line.decode().strip())
            except BaseException:
                try:
                    print(line.strip())
                except BaseException:
                    print(line)
    assert child.returncode == 0
