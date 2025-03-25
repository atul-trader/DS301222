# Command to install pytest
# pip install pytest

from _1_pytest_demo import add

def test_add_int():
    assert add(2,3) == 5

def test_add_str():
    assert add("a","b") == "ab"

class Test_Cases:
    def test_add_int(self):
        assert add(2,3) == 5

    def test_add_str(self):
        assert add("a","b") == "abc"