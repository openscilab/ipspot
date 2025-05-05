import re
from unittest import mock
from ipspot import get_private_ipv4
from ipspot import get_public_ipv4, IPv4API

TEST_CASE_NAME = "IPv4 tests"
IPV4_REGEX = re.compile(r'^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$')
DATA_ITEMS = {'country_code', 'latitude', 'longitude', 'api', 'country', 'timezone', 'organization', 'region', 'ip', 'city'}
LOOPBACK_LIST = ["127.0.0.1", "127.0.0.0", "127.0.1.1", "0.0.0.0"]

def test_private_ipv4_success():
    result = get_private_ipv4()
    assert result["status"]
    assert IPV4_REGEX.match(result["data"]["ip"])
    assert result["data"]["ip"] not in LOOPBACK_LIST


def test_private_ipv4_error():
    with mock.patch("socket.gethostbyname", side_effect=Exception("Test error")):
        result = get_private_ipv4()
        assert not result["status"]
        assert result["error"] == "Test error"


def test_public_ipv4_auto_success():
    result = get_public_ipv4(api=IPv4API.AUTO, geo=True)
    assert result["status"]
    assert IPV4_REGEX.match(result["data"]["ip"])
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
    assert IPV4_REGEX.match(result["data"]["ip"])
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
    assert IPV4_REGEX.match(result["data"]["ip"])
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
    assert IPV4_REGEX.match(result["data"]["ip"])
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
    assert IPV4_REGEX.match(result["data"]["ip"])
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

