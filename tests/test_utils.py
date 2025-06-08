from ipspot.utils import _filter_parameter, _attempt_with_retries
from unittest.mock import Mock

TEST_CASE_NAME = "Utils tests"


def test_filter_parameter1():
    assert _filter_parameter(None) == "N/A"


def test_filter_parameter2():
    assert _filter_parameter("") == "N/A"


def test_filter_parameter3():
    assert _filter_parameter("   ") == "N/A"


def test_filter_parameter4():
    assert _filter_parameter("GB") == "GB"

def test_attempt_with_retries1():
    mock_func = Mock(return_value={"status": True, "data": {"message": "ok"}})
    result = _attempt_with_retries(mock_func, max_retries=3, retry_delay=0.01)
    assert result["status"] is True
    assert mock_func.call_count == 1

def test_attempt_with_retries2():
    mock_func = Mock(side_effect=[
        {"status": False, "error": "fail"},
        {"status": False, "error": "fail again"},
        {"status": True, "data": {"message": "ok"}}
    ])
    result = _attempt_with_retries(mock_func, max_retries=5, retry_delay=0.01)
    assert result["status"] is True
    assert mock_func.call_count == 3

def test_attempt_with_retries3():
    mock_func = Mock(return_value={"status": False, "error": "permanent failure"})
    result = _attempt_with_retries(mock_func, max_retries=2, retry_delay=0.01)
    assert result["status"] is False
    assert result["error"] == "permanent failure"
    assert mock_func.call_count == 3

def test_attempt_with_retries4():
    mock_func = Mock(return_value={"status": False, "error": "no retry"})
    result = _attempt_with_retries(mock_func, max_retries=0, retry_delay=0.01)
    assert result["status"] is False
    assert mock_func.call_count == 1

def test_attempt_with_retries5():
    mock_func = Mock(return_value={"status": False, "error": "invalid"})
    result = _attempt_with_retries(mock_func, max_retries=-5, retry_delay=0.01)
    assert result["status"] is False
    assert mock_func.call_count == 1

def test_attempt_with_retries6():
    def example_func(x, y):
        return {"status": x + y > 0, "data": {"sum": x + y} if x + y > 0 else {}, "error": "" if x + y > 0 else "negative"}
    result = _attempt_with_retries(example_func, max_retries=1, retry_delay=0.01, x=1, y=2)
    assert result["status"] is True
    assert result["data"]["sum"] == 3





