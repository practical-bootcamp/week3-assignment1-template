####################################################################################################
# !!!! DO NOT MODIFY THIS TEST FILE !!!!                                                           #
# This test file is not part of your assignment                                                    #
####################################################################################################
import os
from os.path import dirname

expected_tests = [
    "test 1",
    "test 2",
    "test 3",
]


def test_expected_tests_ran():
    current_file = os.path.abspath(__file__)
    root = dirname(dirname(current_file))
    report = os.path.join(root, "test_report.txt")
    with open(report, "r") as _f:
        tests = [line.strip('\n') for line in _f]
    assert sorted(tests) == expected_tests, f"Expected {len(expected_tests)} to run but saw {len(tests)}. Fix the invalid.py tests to make them pass"
