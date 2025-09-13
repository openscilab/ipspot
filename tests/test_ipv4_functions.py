from unittest import mock
import requests
from ipspot import get_private_ipv4, is_ipv4
from ipspot import get_public_ipv4, IPv4API
from ipspot import is_loopback

TEST_CASE_NAME = "IPv4 functions tests"
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





def test_public_ipv4_auto_timeout_error():
    result = get_public_ipv4(api=IPv4API.AUTO, geo=True, timeout="5")
    assert not result["status"]


def test_public_ipv4_auto_net_error():
    with mock.patch.object(requests.Session, "get", side_effect=Exception("No Internet")):
        result = get_public_ipv4(api=IPv4API.AUTO)
        assert not result["status"]
        assert result["error"] == "All attempts failed."





def test_public_ipv4_auto_safe_timeout_error():
    result = get_public_ipv4(api=IPv4API.AUTO_SAFE, geo=True, timeout="5")
    assert not result["status"]


def test_public_ipv4_auto_safe_net_error():
    with mock.patch.object(requests.Session, "get", side_effect=Exception("No Internet")):
        result = get_public_ipv4(api=IPv4API.AUTO_SAFE)
        assert not result["status"]
        assert result["error"] == "All attempts failed."





def test_public_ipv4_ipapi_co_timeout_error():
    result = get_public_ipv4(api=IPv4API.IPAPI_CO, geo=True, timeout="5")
    assert not result["status"]


def test_public_ipv4_ipapi_co_net_error():
    with mock.patch.object(requests.Session, "get", side_effect=Exception("No Internet")):
        result = get_public_ipv4(api=IPv4API.IPAPI_CO)
        assert not result["status"]
        assert result["error"] == "No Internet"





def test_public_ipv4_ipleak_net_timeout_error():
    result = get_public_ipv4(api=IPv4API.IPLEAK_NET, geo=True, timeout="5")
    assert not result["status"]


def test_public_ipv4_ipleak_net_net_error():
    with mock.patch.object(requests.Session, "get", side_effect=Exception("No Internet")):
        result = get_public_ipv4(api=IPv4API.IPLEAK_NET)
        assert not result["status"]
        assert result["error"] == "No Internet"





def test_public_ipv4_my_ip_io_timeout_error():
    result = get_public_ipv4(api=IPv4API.MY_IP_IO, geo=True, timeout="5")
    assert not result["status"]


def test_public_ipv4_my_ip_io_net_error():
    with mock.patch.object(requests.Session, "get", side_effect=Exception("No Internet")):
        result = get_public_ipv4(api=IPv4API.MY_IP_IO)
        assert not result["status"]
        assert result["error"] == "No Internet"





def test_public_ipv4_ifconfig_co_timeout_error():
    result = get_public_ipv4(api=IPv4API.IFCONFIG_CO, geo=True, timeout="5")
    assert not result["status"]


def test_public_ipv4_ifconfig_co_net_error():
    with mock.patch.object(requests.Session, "get", side_effect=Exception("No Internet")):
        result = get_public_ipv4(api=IPv4API.IFCONFIG_CO)
        assert not result["status"]
        assert result["error"] == "No Internet"





def test_public_ipv4_myip_la_timeout_error():
    result = get_public_ipv4(api=IPv4API.MYIP_LA, geo=True, timeout="5")
    assert not result["status"]


def test_public_ipv4_myip_la_net_error():
    with mock.patch.object(requests.Session, "get", side_effect=Exception("No Internet")):
        result = get_public_ipv4(api=IPv4API.MYIP_LA)
        assert not result["status"]
        assert result["error"] == "No Internet"





def test_public_ipv4_ipquery_io_timeout_error():
    result = get_public_ipv4(api=IPv4API.IPQUERY_IO, geo=True, timeout="5")
    assert not result["status"]


def test_public_ipv4_ipquery_io_net_error():
    with mock.patch.object(requests.Session, "get", side_effect=Exception("No Internet")):
        result = get_public_ipv4(api=IPv4API.IPQUERY_IO)
        assert not result["status"]
        assert result["error"] == "No Internet"





def test_public_ipv4_ipwho_is_timeout_error():
    result = get_public_ipv4(api=IPv4API.IPWHO_IS, geo=True, timeout="5")
    assert not result["status"]


def test_public_ipv4_ipwho_is_net_error():
    with mock.patch.object(requests.Session, "get", side_effect=Exception("No Internet")):
        result = get_public_ipv4(api=IPv4API.IPWHO_IS)
        assert not result["status"]
        assert result["error"] == "No Internet"





def test_public_ipv4_freeipapi_com_timeout_error():
    result = get_public_ipv4(api=IPv4API.FREEIPAPI_COM, geo=True, timeout="5")
    assert not result["status"]


def test_public_ipv4_freeipapi_com_net_error():
    with mock.patch.object(requests.Session, "get", side_effect=Exception("No Internet")):
        result = get_public_ipv4(api=IPv4API.FREEIPAPI_COM)
        assert not result["status"]
        assert result["error"] == "No Internet"





def test_public_ipv4_ip_api_com_timeout_error():
    result = get_public_ipv4(api=IPv4API.IP_API_COM, geo=True, timeout="5")
    assert not result["status"]


def test_public_ipv4_ip_api_com_net_error():
    with mock.patch.object(requests.Session, "get", side_effect=Exception("No Internet")):
        result = get_public_ipv4(api=IPv4API.IP_API_COM)
        assert not result["status"]
        assert result["error"] == "No Internet"





def test_public_ipv4_ipinfo_io_timeout_error():
    result = get_public_ipv4(api=IPv4API.IPINFO_IO, geo=True, timeout="5")
    assert not result["status"]


def test_public_ipv4_ipinfo_io_net_error():
    with mock.patch.object(requests.Session, "get", side_effect=Exception("No Internet")):
        result = get_public_ipv4(api=IPv4API.IPINFO_IO)
        assert not result["status"]
        assert result["error"] == "No Internet"





def test_public_ipv4_ip_sb_timeout_error():
    result = get_public_ipv4(api=IPv4API.IP_SB, geo=True, timeout="5")
    assert not result["status"]



def test_public_ipv4_ip_sb_net_error():
    with mock.patch.object(requests.Session, "get", side_effect=Exception("No Internet")):
        result = get_public_ipv4(api=IPv4API.IP_SB)
        assert not result["status"]
        assert result["error"] == "No Internet"





def test_public_ipv4_ident_me_timeout_error():
    result = get_public_ipv4(api=IPv4API.IDENT_ME, geo=True, timeout="5")
    assert not result["status"]


def test_public_ipv4_ident_me_net_error():
    with mock.patch.object(requests.Session, "get", side_effect=Exception("No Internet")):
        result = get_public_ipv4(api=IPv4API.IDENT_ME)
        assert not result["status"]
        assert result["error"] == "No Internet"





def test_public_ipv4_tnedi_me_timeout_error():
    result = get_public_ipv4(api=IPv4API.TNEDI_ME, geo=True, timeout="5")
    assert not result["status"]


def test_public_ipv4_tnedi_me_net_error():
    with mock.patch.object(requests.Session, "get", side_effect=Exception("No Internet")):
        result = get_public_ipv4(api=IPv4API.TNEDI_ME)
        assert not result["status"]
        assert result["error"] == "No Internet"


def test_public_ipv4_api_error():
    result = get_public_ipv4(api="api1", geo=True)
    assert not result["status"]
    assert result["error"] == "Unsupported API: api1"





def test_public_ipv4_reallyfreegeoip_org_timeout_error():
    result = get_public_ipv4(api=IPv4API.REALLYFREEGEOIP_ORG, geo=True, timeout="5")
    assert not result["status"]


def test_public_ipv4_reallyfreegeoip_org_net_error():
    with mock.patch.object(requests.Session, "get", side_effect=Exception("No Internet")):
        result = get_public_ipv4(api=IPv4API.REALLYFREEGEOIP_ORG)
        assert not result["status"]
        assert result["error"] == "No Internet"




def test_public_ipv4_wtfismyip_com_timeout_error():
    result = get_public_ipv4(api=IPv4API.WTFISMYIP_COM, geo=True, timeout="5")
    assert not result["status"]


def test_public_ipv4_wtfismyip_com_net_error():
    with mock.patch.object(requests.Session, "get", side_effect=Exception("No Internet")):
        result = get_public_ipv4(api=IPv4API.WTFISMYIP_COM)
        assert not result["status"]
        assert result["error"] == "No Internet"
