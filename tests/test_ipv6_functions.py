import socket
from unittest import mock
from ipspot import get_private_ipv6, is_ipv6
from ipspot import is_loopback

TEST_CASE_NAME = "IPv6 functions tests"
DATA_ITEMS = {'country_code', 'latitude', 'longitude', 'api', 'country', 'timezone', 'organization', 'region', 'ip', 'city'}


def test_is_ipv6_1():
    assert is_ipv6("2001:0db8:85a3:0000:0000:8a2e:0370:7334")


def test_is_ipv6_2():
    assert is_ipv6("::")


def test_is_ipv6_3():
    assert is_ipv6("ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff")


def test_is_ipv6_4():
    assert not is_ipv6("2001:0db8:85a3::8a2e:370g:7334")


def test_is_ipv6_5():
    assert not is_ipv6("abc.def.ghi.jkl")


def test_is_ipv6_6():
    assert not is_ipv6(123)


def test_is_ipv6_7():
    assert not is_ipv6("1234:5678:9abc:defg::1")


@mock.patch("socket.socket")
def test_private_ipv6_success(mock_socket_class):
    mock_socket_instance = mock.MagicMock()
    mock_socket_class.return_value.__enter__.return_value = mock_socket_instance
    mock_socket_instance.getsockname.return_value = ("fe80::e1bd:f78:b233:21c9", 1, 0, 0)
    result = get_private_ipv6()
    assert result["status"]
    assert result["data"]["ip"] == "fe80::e1bd:f78:b233:21c9"


def test_get_private_ipv6_loopback():
    mock_socket = mock.MagicMock()
    mock_socket.__enter__.return_value.getsockname.return_value = ('::1',)
    with mock.patch('socket.socket', return_value=mock_socket):
        result = get_private_ipv6()
        assert not result["status"]
        assert result["error"] == "Could not identify a non-loopback IPv6 address for this system."


def test_get_private_ipv6_exception():
    with mock.patch('socket.socket', side_effect=Exception("Test error")):
        result = get_private_ipv6()
        assert not result["status"]
        assert result["error"] == "Test error"