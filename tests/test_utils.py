# These 3 tests are all failing. To make them pass you will need to modify the utils.str_to_bool()
# function and one of these tests.
# Hint: The tests that assert the boolean result require updating the str_to_bool() function
# And the test that asserts the exception needs the exception to be udpated

from utils import str_to_bool
import pytest


def test_str_to_bool_one():
    result = str_to_bool("1")
    assert result is True


def test_str_to_bool_zero():
    result = str_to_bool("0")
    assert result is False


def test_runtimeerror():
    with pytest.raises(RuntimeError):
        str_to_bool(None)
