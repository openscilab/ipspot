import re
from ipspot import get_private_ipv4
from ipspot import get_public_ipv4, IPv4API

TEST_CASE_NAME = "IPv4 tests"
IPV4_REGEX = re.compile(r'^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$')
DATA_ITEMS = {'country_code', 'latitude', 'longitude', 'api', 'country', 'timezone', 'organization', 'region', 'ip', 'city'}


def test_private_ipv4():
    result = get_private_ipv4()
    assert result["status"]
    assert IPV4_REGEX.match(result["data"]["ip"])


def test_public_ipv4_auto1():
    result = get_public_ipv4(api=IPv4API.AUTO, geo=True)
    assert result["status"]
    assert IPV4_REGEX.match(result["data"]["ip"])
    assert set(result["data"].keys()) == DATA_ITEMS


def test_public_ipv4_auto2():
    result = get_public_ipv4(api=IPv4API.AUTO, geo=True, timeout="5")
    assert not result["status"]


def test_public_ipv4_ipapi1():
    result = get_public_ipv4(api=IPv4API.IPAPI, geo=True)
    assert result["status"]
    assert IPV4_REGEX.match(result["data"]["ip"])
    assert set(result["data"].keys()) == DATA_ITEMS
    assert result["data"]["api"] == "ip-api.com"


def test_public_ipv4_ipapi2():
    result = get_public_ipv4(api=IPv4API.IPAPI, geo=True, timeout="5")
    assert not result["status"]


def test_public_ipv4_ipinfo1():
    result = get_public_ipv4(api=IPv4API.IPINFO, geo=True)
    assert result["status"]
    assert IPV4_REGEX.match(result["data"]["ip"])
    assert set(result["data"].keys()) == DATA_ITEMS
    assert result["data"]["api"] == "ipinfo.io"


def test_public_ipv4_ipinfo2():
    result = get_public_ipv4(api=IPv4API.IPINFO, geo=True, timeout="5")
    assert not result["status"]


def test_public_ipv4_ipsb1():
    result = get_public_ipv4(api=IPv4API.IPSB, geo=True)
    assert result["status"]
    assert IPV4_REGEX.match(result["data"]["ip"])
    assert set(result["data"].keys()) == DATA_ITEMS
    assert result["data"]["api"] == "ip.sb"


def test_public_ipv4_ipsb2():
    result = get_public_ipv4(api=IPv4API.IPSB, geo=True, timeout="5")
    assert not result["status"]

