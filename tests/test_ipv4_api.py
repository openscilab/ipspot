from ipspot import is_ipv4
from ipspot import get_public_ipv4, IPv4API

TEST_CASE_NAME = "IPv4 API tests"
DATA_ITEMS = {'country_code', 'latitude', 'longitude', 'api', 'country', 'timezone', 'organization', 'region', 'ip', 'city'}


def test_public_ipv4_auto_success():
    result = get_public_ipv4(api=IPv4API.AUTO, geo=True)
    assert result["status"]
    assert is_ipv4(result["data"]["ip"])
    assert set(result["data"].keys()) == DATA_ITEMS


def test_public_ipv4_auto_safe_success():
    result = get_public_ipv4(api=IPv4API.AUTO_SAFE, geo=True)
    assert result["status"]
    assert is_ipv4(result["data"]["ip"])
    assert set(result["data"].keys()) == DATA_ITEMS


def test_public_ipv4_ipapi_co_success():
    result = get_public_ipv4(api=IPv4API.IPAPI_CO, geo=True, timeout=40, max_retries=4, retry_delay=90)
    assert result["status"]
    assert is_ipv4(result["data"]["ip"])
    assert set(result["data"].keys()) == DATA_ITEMS
    assert result["data"]["api"] == "ipapi.co"


def test_public_ipv4_ipleak_net_success():
    result = get_public_ipv4(api=IPv4API.IPLEAK_NET, geo=True, timeout=40, max_retries=4, retry_delay=90)
    assert result["status"]
    assert is_ipv4(result["data"]["ip"])
    assert set(result["data"].keys()) == DATA_ITEMS
    assert result["data"]["api"] == "ipleak.net"


def test_public_ipv4_my_ip_io_success():
    result = get_public_ipv4(api=IPv4API.MY_IP_IO, geo=True, timeout=40, max_retries=4, retry_delay=90)
    assert result["status"]
    assert is_ipv4(result["data"]["ip"])
    assert set(result["data"].keys()) == DATA_ITEMS
    assert result["data"]["api"] == "my-ip.io"


def test_public_ipv4_ifconfig_co_success():
    result = get_public_ipv4(api=IPv4API.IFCONFIG_CO, geo=True, timeout=40, max_retries=4, retry_delay=90)
    assert result["status"]
    assert is_ipv4(result["data"]["ip"])
    assert set(result["data"].keys()) == DATA_ITEMS
    assert result["data"]["api"] == "ifconfig.co"


def test_public_ipv4_myip_la_success():
    result = get_public_ipv4(api=IPv4API.MYIP_LA, geo=True, timeout=40, max_retries=4, retry_delay=90)
    assert result["status"]
    assert is_ipv4(result["data"]["ip"])
    assert set(result["data"].keys()) == DATA_ITEMS
    assert result["data"]["api"] == "myip.la"


def test_public_ipv4_ipquery_io_success():
    result = get_public_ipv4(api=IPv4API.IPQUERY_IO, geo=True, timeout=40, max_retries=4, retry_delay=90)
    assert result["status"]
    assert is_ipv4(result["data"]["ip"])
    assert set(result["data"].keys()) == DATA_ITEMS
    assert result["data"]["api"] == "ipquery.io"


def test_public_ipv4_ipwho_is_success():
    result = get_public_ipv4(api=IPv4API.IPWHO_IS, geo=True, timeout=40, max_retries=4, retry_delay=90)
    assert result["status"]
    assert is_ipv4(result["data"]["ip"])
    assert set(result["data"].keys()) == DATA_ITEMS
    assert result["data"]["api"] == "ipwho.is"


def test_public_ipv4_freeipapi_com_success():
    result = get_public_ipv4(api=IPv4API.FREEIPAPI_COM, geo=True, timeout=40, max_retries=4, retry_delay=90)
    assert result["status"]
    assert is_ipv4(result["data"]["ip"])
    assert set(result["data"].keys()) == DATA_ITEMS
    assert result["data"]["api"] == "freeipapi.com"


def test_public_ipv4_ip_api_com_success():
    result = get_public_ipv4(api=IPv4API.IP_API_COM, geo=True, timeout=40, max_retries=4, retry_delay=90)
    assert result["status"]
    assert is_ipv4(result["data"]["ip"])
    assert set(result["data"].keys()) == DATA_ITEMS
    assert result["data"]["api"] == "ip-api.com"


def test_public_ipv4_ipinfo_io_success():
    result = get_public_ipv4(api=IPv4API.IPINFO_IO, geo=True, timeout=40, max_retries=4, retry_delay=90)
    assert result["status"]
    assert is_ipv4(result["data"]["ip"])
    assert set(result["data"].keys()) == DATA_ITEMS
    assert result["data"]["api"] == "ipinfo.io"


def test_public_ipv4_ip_sb_success():
    result = get_public_ipv4(api=IPv4API.IP_SB, geo=True, timeout=40, max_retries=4, retry_delay=90)
    assert result["status"]
    assert is_ipv4(result["data"]["ip"])
    assert set(result["data"].keys()) == DATA_ITEMS
    assert result["data"]["api"] == "ip.sb"


def test_public_ipv4_ident_me_success():
    result = get_public_ipv4(api=IPv4API.IDENT_ME, geo=True, timeout=40, max_retries=4, retry_delay=90)
    assert result["status"]
    assert is_ipv4(result["data"]["ip"])
    assert set(result["data"].keys()) == DATA_ITEMS
    assert result["data"]["api"] == "ident.me"


def test_public_ipv4_tnedi_me_success():
    result = get_public_ipv4(api=IPv4API.TNEDI_ME, geo=True, timeout=40, max_retries=4, retry_delay=90)
    assert result["status"]
    assert is_ipv4(result["data"]["ip"])
    assert set(result["data"].keys()) == DATA_ITEMS
    assert result["data"]["api"] == "tnedi.me"


def test_public_ipv4_reallyfreegeoip_org_success():
    result = get_public_ipv4(api=IPv4API.REALLYFREEGEOIP_ORG, geo=True, timeout=40, max_retries=4, retry_delay=90)
    assert result["status"]
    assert is_ipv4(result["data"]["ip"])
    assert set(result["data"].keys()) == DATA_ITEMS
    assert result["data"]["api"] == "reallyfreegeoip.org"


def test_public_ipv4_wtfismyip_com_success():
    result = get_public_ipv4(api=IPv4API.WTFISMYIP_COM, geo=True, timeout=40, max_retries=4, retry_delay=90)
    assert result["status"]
    assert is_ipv4(result["data"]["ip"])
    assert set(result["data"].keys()) == DATA_ITEMS
    assert result["data"]["api"] == "wtfismyip.com"
