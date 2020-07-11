from . import cpp_module_test
__version__ = cpp_module_test.__version__

def echo(value):
    return cpp_module_test.echo(str(value))
