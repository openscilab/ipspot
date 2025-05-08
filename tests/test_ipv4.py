from unittest import mock
from ipspot import get_private_ipv4, is_ipv4
from ipspot import get_public_ipv4, IPv4API
from ipspot import is_loopback

TEST_CASE_NAME = "IPv4 tests"
DATA_ITEMS = {'country_code', 'latitude', 'longitude', 'api', 'country', 'timezone', 'organization', 'region', 'ip', 'city'}


def test_is_ipv4_1():
    assert is_ipv4("192.168.0.1")


def test_is_ipv4_2():
    assert is_ipv4("0.0.0.0")


def test_is_ipv4_3():
    assert is_ipv4("255.255.255.255")


def test_is_ipv4_4():
    assert not is_ipv4("256.0.0.1")


def test_is_ipv4_5():
    assert not is_ipv4("abc.def.ghi.jkl")


def test_is_ipv4_6():
    assert not is_ipv4(123)


def test_is_ipv4_7():
    assert not is_ipv4("2001:0db8:85a3:0000:0000:8a2e:0370:7334")


def test_is_loopback_1():
    assert not is_loopback("192.168.0.1")


def test_is_loopback_2():
    assert is_loopback("127.0.0.1")


def test_is_loopback_3():
    assert is_loopback("127.255.255.255")


def test_is_loopback_4():
    assert not is_loopback("abc.def.ghi.jkl")


def test_private_ipv4_success():
    result = get_private_ipv4()
    assert result["status"]
    assert is_ipv4(result["data"]["ip"])
    assert not is_loopback(result["data"]["ip"])


def test_get_private_ipv4_loopback():
    mock_socket = mock.MagicMock()
    mock_socket.__enter__.return_value.getsockname.return_value = ('127.0.0.1',)
    with mock.patch('socket.socket', return_value=mock_socket):
        result = get_private_ipv4()
        assert not result["status"]
        assert result["error"] == "Could not identify a non-loopback IPv4 address for this system."


def test_get_private_ipv4_exception():
    with mock.patch('socket.socket', side_effect=Exception("Test error")):
        result = get_private_ipv4()
        assert not result["status"]
        assert result["error"] == "Test error"


def test_public_ipv4_auto_success():
    result = get_public_ipv4(api=IPv4API.AUTO, geo=True)
    assert result["status"]
    assert is_ipv4(result["data"]["ip"])
    assert set(result["data"].keys()) == DATA_ITEMS


def test_public_ipv4_auto_timeout_error():
    result = get_public_ipv4(api=IPv4API.AUTO, geo=True, timeout="5")
    assert not result["status"]


def test_public_ipv4_auto_net_error():
    with mock.patch("requests.get", side_effect=Exception("No Internet")):
        result = get_public_ipv4(api=IPv4API.AUTO)
        assert not result["status"]
        assert result["error"] == "All attempts failed."


def test_public_ipv4_ipapi_success():
    result = get_public_ipv4(api=IPv4API.IPAPI, geo=True)
    assert result["status"]
    assert is_ipv4(result["data"]["ip"])
    assert set(result["data"].keys()) == DATA_ITEMS
    assert result["data"]["api"] == "ip-api.com"


def test_public_ipv4_ipapi_timeout_error():
    result = get_public_ipv4(api=IPv4API.IPAPI, geo=True, timeout="5")
    assert not result["status"]


def test_public_ipv4_ipapi_net_error():
    with mock.patch("requests.get", side_effect=Exception("No Internet")):
        result = get_public_ipv4(api=IPv4API.IPAPI)
        assert not result["status"]
        assert result["error"] == "No Internet"


def test_public_ipv4_ipinfo_success():
    result = get_public_ipv4(api=IPv4API.IPINFO, geo=True)
    assert result["status"]
    assert is_ipv4(result["data"]["ip"])
    assert set(result["data"].keys()) == DATA_ITEMS
    assert result["data"]["api"] == "ipinfo.io"


def test_public_ipv4_ipinfo_timeout_error():
    result = get_public_ipv4(api=IPv4API.IPINFO, geo=True, timeout="5")
    assert not result["status"]


def test_public_ipv4_ipinfo_net_error():
    with mock.patch("requests.get", side_effect=Exception("No Internet")):
        result = get_public_ipv4(api=IPv4API.IPINFO)
        assert not result["status"]
        assert result["error"] == "No Internet"


def test_public_ipv4_ipsb_success():
    result = get_public_ipv4(api=IPv4API.IPSB, geo=True)
    assert result["status"]
    assert is_ipv4(result["data"]["ip"])
    assert set(result["data"].keys()) == DATA_ITEMS
    assert result["data"]["api"] == "ip.sb"


def test_public_ipv4_ipsb_timeout_error():
    result = get_public_ipv4(api=IPv4API.IPSB, geo=True, timeout="5")
    assert not result["status"]



def test_public_ipv4_ipsb_net_error():
    with mock.patch("requests.get", side_effect=Exception("No Internet")):
        result = get_public_ipv4(api=IPv4API.IPSB)
        assert not result["status"]
        assert result["error"] == "No Internet"


def test_public_ipv4_identme_success():
    result = get_public_ipv4(api=IPv4API.IDENTME, geo=True)
    assert result["status"]
    assert is_ipv4(result["data"]["ip"])
    assert set(result["data"].keys()) == DATA_ITEMS
    assert result["data"]["api"] == "ident.me"


def test_public_ipv4_identme_timeout_error():
    result = get_public_ipv4(api=IPv4API.IDENTME, geo=True, timeout="5")
    assert not result["status"]


def test_public_ipv4_identme_net_error():
    with mock.patch("requests.get", side_effect=Exception("No Internet")):
        result = get_public_ipv4(api=IPv4API.IDENTME)
        assert not result["status"]
        assert result["error"] == "No Internet"


def test_public_ipv4_api_error():
    result = get_public_ipv4(api="api1", geo=True)
    assert not result["status"]
    assert result["error"] == "Unsupported API: api1"

