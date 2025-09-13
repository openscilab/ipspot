from ipspot import get_public_ipv6, is_ipv6
from ipspot import IPv6API

TEST_CASE_NAME = "IPv6 API tests"
DATA_ITEMS = {'country_code', 'latitude', 'longitude', 'api', 'country', 'timezone', 'organization', 'region', 'ip', 'city'}


def test_public_ipv6_ip_sb_success():
    result = get_public_ipv6(api=IPv6API.IP_SB)
    assert result["status"]
    assert is_ipv6(result["data"]["ip"])
    assert set(result["data"].keys()) == DATA_ITEMS

def test_public_ipv6_auto_success():
    result = get_public_ipv6(api=IPv6API.AUTO, geo=True, timeout=40, max_retries=4, retry_delay=90)
    assert result["status"]
    assert is_ipv6(result["data"]["ip"])
    assert set(result["data"].keys()) == DATA_ITEMS


def test_public_ipv6_auto_safe_success():
    result = get_public_ipv6(api=IPv6API.AUTO_SAFE, geo=True, timeout=40, max_retries=4, retry_delay=90)
    assert result["status"]
    assert is_ipv6(result["data"]["ip"])
    assert set(result["data"].keys()) == DATA_ITEMS