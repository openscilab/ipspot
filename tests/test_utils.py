from ipspot.utils import filter_parameter

TEST_CASE_NAME = "Utils tests"


def test_filter_parameter1():
    assert filter_parameter(None) == "N/A"


def test_filter_parameter2():
    assert filter_parameter("") == "N/A"


def test_filter_parameter3():
    assert filter_parameter("   ") == "N/A"


def test_filter_parameter4():
    assert filter_parameter("GB") == "GB"





