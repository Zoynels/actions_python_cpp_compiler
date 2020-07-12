import actions_python_cpp_compiler
import pytest


@pytest.mark.parametrize("value", [1, "some text"])
def test_echo(value):
    assert str(value) == actions_python_cpp_compiler.echo(value)
