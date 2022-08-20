# There is 1 function, 1 class, and 2 methods in this module. All of them are
# tests This Python file is also a test. You will need to:
# - modify this filename so that it gets collected automatically
# - change the names of the function, class, and methods so that they run


import os
from os.path import dirname
import pytest


current_dir = dirname(os.path.abspath(__file__))
root = dirname(current_dir)
report_file = os.path.join(root, "test_report.txt")


def invalid_test():
    with open(report_file, "a") as _f:
        _f.write("test 1\n")


class InvalidTestClass:

    def invalid_method(self):
        with open(report_file, "a") as _f:
            _f.write("test 2\n")

    def other_test(self):
        with open(report_file, "a") as _f:
            _f.write("test 3\n")
