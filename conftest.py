import pytest
import os


@pytest.fixture(scope="session", autouse=True)
def setup(request):
    with open("test_report.txt", "w") as _f:
        _f.write('')

    def remove_test_report():
        if os.path.exists("test_report.txt"):
            os.remove("test_report.txt")
    request.addfinalizer(remove_test_report)
