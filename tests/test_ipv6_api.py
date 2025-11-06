from ipspot import get_public_ipv6, is_ipv6
from ipspot import IPv6API

TEST_CASE_NAME = "IPv6 API tests"
DATA_ITEMS = {'country_code', 'latitude', 'longitude', 'api', 'country', 'timezone', 'organization', 'region', 'ip', 'city'}


def test_public_ipv6_ip_sb_success():
    result = get_public_ipv6(api=IPv6API.IP_SB)
    assert result["status"]
    assert is_ipv6(result["data"]["ip"])
    assert set(result["data"].keys()) == DATA_ITEMS


def test_public_ipv6_ident_me_success():
    result = get_public_ipv6(api=IPv6API.IDENT_ME, geo=True, timeout=40, max_retries=4, retry_delay=90)
    assert result["status"]
    assert is_ipv6(result["data"]["ip"])
    assert set(result["data"].keys()) == DATA_ITEMS
    assert result["data"]["api"] == "ident.me"


def test_public_ipv6_tnedi_me_success():
    result = get_public_ipv6(api=IPv6API.TNEDI_ME, geo=True, timeout=40, max_retries=4, retry_delay=90)
    assert result["status"]
    assert is_ipv6(result["data"]["ip"])
    assert set(result["data"].keys()) == DATA_ITEMS
    assert result["data"]["api"] == "tnedi.me"


def test_public_ipv6_ipleak_net_success():
    result = get_public_ipv6(api=IPv6API.IPLEAK_NET, geo=True, timeout=40, max_retries=4, retry_delay=90)
    assert result["status"]
    assert is_ipv6(result["data"]["ip"])
    assert set(result["data"].keys()) == DATA_ITEMS
    assert result["data"]["api"] == "ipleak.net"


def test_public_ipv6_my_ip_io_success():
    result = get_public_ipv6(api=IPv6API.MY_IP_IO, geo=True, timeout=40, max_retries=4, retry_delay=90)
    assert result["status"]
    assert is_ipv6(result["data"]["ip"])
    assert set(result["data"].keys()) == DATA_ITEMS
    assert result["data"]["api"] == "my-ip.io"


def test_public_ipv6_ifconfig_co_success():
    result = get_public_ipv6(api=IPv6API.IFCONFIG_CO, geo=True, timeout=40, max_retries=4, retry_delay=90)
    assert result["status"]
    assert is_ipv6(result["data"]["ip"])
    assert set(result["data"].keys()) == DATA_ITEMS
    assert result["data"]["api"] == "ifconfig.co"


def test_public_ipv6_reallyfreegeoip_org_success():
    result = get_public_ipv6(api=IPv6API.REALLYFREEGEOIP_ORG, geo=True, timeout=40, max_retries=4, retry_delay=90)
    assert result["status"]
    assert is_ipv6(result["data"]["ip"])
    assert set(result["data"].keys()) == DATA_ITEMS
    assert result["data"]["api"] == "reallyfreegeoip.org"


def test_public_ipv6_myip_la_success():
    result = get_public_ipv6(api=IPv6API.MYIP_LA, geo=True, timeout=40, max_retries=4, retry_delay=90)
    assert result["status"]
    assert is_ipv6(result["data"]["ip"])
    assert set(result["data"].keys()) == DATA_ITEMS
    assert result["data"]["api"] == "myip.la"


def test_public_freeipapi_com_success():
    result = get_public_ipv6(api=IPv6API.FREEIPAPI_COM, geo=True, timeout=40, max_retries=4, retry_delay=90)
    assert result["status"]
    assert is_ipv6(result["data"]["ip"])
    assert set(result["data"].keys()) == DATA_ITEMS
    assert result["data"]["api"] == "freeipapi.com"


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