from ipspot.utils import _filter_parameter

TEST_CASE_NAME = "Utils tests"


def test_filter_parameter1():
    assert _filter_parameter(None) == "N/A"


def test_filter_parameter2():
    assert _filter_parameter("") == "N/A"


def test_filter_parameter3():
    assert _filter_parameter("   ") == "N/A"


def test_filter_parameter4():
    assert _filter_parameter("GB") == "GB"





