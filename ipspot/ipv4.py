# -*- coding: utf-8 -*-
"""ipspot ipv4 functions."""
import ipaddress
import socket
from typing import Union, Dict, List, Tuple
import requests
from requests.adapters import HTTPAdapter
from urllib3.poolmanager import PoolManager
from .utils import is_loopback, _get_json_standard, _attempt_with_retries
from .params import REQUEST_HEADERS, IPv4API


class IPv4HTTPAdapter(HTTPAdapter):
    """A custom HTTPAdapter that enforces the use of IPv4 for DNS resolution during HTTP(S) requests using the requests library."""

    def init_poolmanager(self, connections: int, maxsize: int, block: bool = False, **kwargs: dict) -> None:
        """
        Initialize the connection pool manager using a temporary override of socket.getaddrinfo to ensure only IPv4 addresses are used.

        :param connections: the number of connection pools to cache
        :param maxsize: the maximum number of connections to save in the pool
        :param block: whether the connections should block when reaching the max size
        :param kwargs: additional keyword arguments for the PoolManager
        """
        self.poolmanager = PoolManager(
            num_pools=connections,
            maxsize=maxsize,
            block=block,
            socket_options=self._ipv4_socket_options(),
            **kwargs
        )

    def _ipv4_socket_options(self) -> list:
        """
        Temporarily patches socket.getaddrinfo to filter only IPv4 addresses (AF_INET).

        :return: an empty list of socket options; DNS patching occurs here
        """
        original_getaddrinfo = socket.getaddrinfo

        def ipv4_only_getaddrinfo(*args: list, **kwargs: dict) -> List[Tuple]:
            results = original_getaddrinfo(*args, **kwargs)
            return [res for res in results if res[0] == socket.AF_INET]

        self._original_getaddrinfo = socket.getaddrinfo
        socket.getaddrinfo = ipv4_only_getaddrinfo

        return []

    def __del__(self) -> None:
        """Restores the original socket.getaddrinfo function upon adapter deletion."""
        if hasattr(self, "_original_getaddrinfo"):
            socket.getaddrinfo = self._original_getaddrinfo


def _get_json_ipv4_forced(url: str, timeout: Union[float, Tuple[float, float]]) -> dict:
    """
    Send GET request with forced IPv4 using IPv4HTTPAdapter that returns JSON response.

    :param url: API url
    :param timeout: timeout value for API
    """
    with requests.Session() as session:
        session.mount("http://", IPv4HTTPAdapter())
        session.mount("https://", IPv4HTTPAdapter())
        response = session.get(url, headers=REQUEST_HEADERS, timeout=timeout)
        response.raise_for_status()
        return response.json()


def is_ipv4(ip: str) -> bool:
    """
    Check if the given input is a valid IPv4 address.

    :param ip: input IP
    """
    if not isinstance(ip, str):
        return False
    try:
        _ = ipaddress.IPv4Address(ip)
        return True
    except Exception:
        return False


def get_private_ipv4() -> Dict[str, Union[bool, Dict[str, str], str]]:
    """Retrieve the private IPv4 address."""
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
            s.connect(('192.168.1.1', 1))
            private_ip = s.getsockname()[0]
        if is_ipv4(private_ip) and not is_loopback(private_ip):
            return {"status": True, "data": {"ip": private_ip}}
        return {"status": False, "error": "Could not identify a non-loopback IPv4 address for this system."}
    except Exception as e:
        return {"status": False, "error": str(e)}


def _ip_sb_ipv4(geo: bool=False, timeout: Union[float, Tuple[float, float]]
                =5) -> Dict[str, Union[bool, Dict[str, Union[str, float]], str]]:
    """
    Get public IP and geolocation using ip.sb.

    :param geo: geolocation flag
    :param timeout: timeout value for API
    """
    try:
        data = _get_json_standard(url="https://api-ipv4.ip.sb/geoip", timeout=timeout)
        result = {"status": True, "data": {"ip": data["ip"], "api": "ip.sb"}}
        if geo:
            geo_data = {
                "city": data.get("city"),
                "region": data.get("region"),
                "country": data.get("country"),
                "country_code": data.get("country_code"),
                "latitude": data.get("latitude"),
                "longitude": data.get("longitude"),
                "organization": data.get("organization"),
                "timezone": data.get("timezone")
            }
            result["data"].update(geo_data)
        return result
    except Exception as e:
        return {"status": False, "error": str(e)}


def _ipleak_net_ipv4(geo: bool=False, timeout: Union[float, Tuple[float, float]]
                     =5) -> Dict[str, Union[bool, Dict[str, Union[str, float]], str]]:
    """
    Get public IP and geolocation using ipleak.net.

    :param geo: geolocation flag
    :param timeout: timeout value for API
    """
    try:
        data = _get_json_standard(url="https://ipv4.ipleak.net/json/", timeout=timeout)
        result = {"status": True, "data": {"ip": data["ip"], "api": "ipleak.net"}}
        if geo:
            geo_data = {
                "city": data.get("city_name"),
                "region": data.get("region_name"),
                "country": data.get("country_name"),
                "country_code": data.get("country_code"),
                "latitude": data.get("latitude"),
                "longitude": data.get("longitude"),
                "organization": data.get("isp_name"),
                "timezone": data.get("time_zone")
            }
            result["data"].update(geo_data)
        return result
    except Exception as e:
        return {"status": False, "error": str(e)}


def _my_ip_io_ipv4(geo: bool=False, timeout: Union[float, Tuple[float, float]]
                   =5) -> Dict[str, Union[bool, Dict[str, Union[str, float]], str]]:
    """
    Get public IP and geolocation using my-ip.io.

    :param geo: geolocation flag
    :param timeout: timeout value for API
    """
    try:
        data = _get_json_standard(url="https://api4.my-ip.io/v2/ip.json", timeout=timeout)
        result = {"status": True, "data": {"ip": data["ip"], "api": "my-ip.io"}}
        if geo:
            geo_data = {
                "city": data.get("city"),
                "region": data.get("region"),
                "country": data.get("country", {}).get("name"),
                "country_code": data.get("country", {}).get("code"),
                "latitude": data.get("location", {}).get("lat"),
                "longitude": data.get("location", {}).get("lon"),
                "organization": data.get("asn", {}).get("name"),
                "timezone": data.get("timeZone")
            }
            result["data"].update(geo_data)
        return result
    except Exception as e:
        return {"status": False, "error": str(e)}


def _ifconfig_co_ipv4(geo: bool=False, timeout: Union[float, Tuple[float, float]]
                      =5) -> Dict[str, Union[bool, Dict[str, Union[str, float]], str]]:
    """
    Get public IP and geolocation using ifconfig.co.

    :param geo: geolocation flag
    :param timeout: timeout value for API
    """
    try:
        data = _get_json_ipv4_forced(url="https://ifconfig.co/json", timeout=timeout)
        result = {"status": True, "data": {"ip": data["ip"], "api": "ifconfig.co"}}
        if geo:
            geo_data = {
                "city": data.get("city"),
                "region": data.get("region_name"),
                "country": data.get("country"),
                "country_code": data.get("country_iso"),
                "latitude": data.get("latitude"),
                "longitude": data.get("longitude"),
                "organization": data.get("asn_org"),
                "timezone": data.get("time_zone")
            }
            result["data"].update(geo_data)
        return result
    except Exception as e:
        return {"status": False, "error": str(e)}


def _ipapi_co_ipv4(geo: bool=False, timeout: Union[float, Tuple[float, float]]
                   =5) -> Dict[str, Union[bool, Dict[str, Union[str, float]], str]]:
    """
    Get public IP and geolocation using ipapi.co.

    :param geo: geolocation flag
    :param timeout: timeout value for API
    """
    try:
        data = _get_json_ipv4_forced(url="https://ipapi.co/json/", timeout=timeout)
        result = {"status": True, "data": {"ip": data["ip"], "api": "ipapi.co"}}
        if geo:
            geo_data = {
                "city": data.get("city"),
                "region": data.get("region"),
                "country": data.get("country_name"),
                "country_code": data.get("country_code"),
                "latitude": data.get("latitude"),
                "longitude": data.get("longitude"),
                "organization": data.get("org"),
                "timezone": data.get("timezone")
            }
            result["data"].update(geo_data)
        return result
    except Exception as e:
        return {"status": False, "error": str(e)}


def _ip_api_com_ipv4(geo: bool=False, timeout: Union[float, Tuple[float, float]]
                     =5) -> Dict[str, Union[bool, Dict[str, Union[str, float]], str]]:
    """
    Get public IP and geolocation using ip-api.com.

    :param geo: geolocation flag
    :param timeout: timeout value for API
    """
    try:
        data = _get_json_ipv4_forced(url="http://ip-api.com/json/", timeout=timeout)
        if data.get("status") != "success":
            return {"status": False, "error": "ip-api lookup failed"}
        result = {"status": True, "data": {"ip": data["query"], "api": "ip-api.com"}}
        if geo:
            geo_data = {
                "city": data.get("city"),
                "region": data.get("regionName"),
                "country": data.get("country"),
                "country_code": data.get("countryCode"),
                "latitude": data.get("lat"),
                "longitude": data.get("lon"),
                "organization": data.get("org"),
                "timezone": data.get("timezone")
            }
            result["data"].update(geo_data)
        return result
    except Exception as e:
        return {"status": False, "error": str(e)}


def _ipinfo_io_ipv4(geo: bool=False, timeout: Union[float, Tuple[float, float]]
                    =5) -> Dict[str, Union[bool, Dict[str, Union[str, float]], str]]:
    """
    Get public IP and geolocation using ipinfo.io.

    :param geo: geolocation flag
    :param timeout: timeout value for API
    """
    try:
        data = _get_json_ipv4_forced(url="https://ipinfo.io/json", timeout=timeout)
        result = {"status": True, "data": {"ip": data["ip"], "api": "ipinfo.io"}}
        if geo:
            loc = data.get("loc", "").split(",")
            geo_data = {
                "city": data.get("city"),
                "region": data.get("region"),
                "country": None,
                "country_code": data.get("country"),
                "latitude": float(loc[0]) if len(loc) == 2 else None,
                "longitude": float(loc[1]) if len(loc) == 2 else None,
                "organization": data.get("org"),
                "timezone": data.get("timezone")
            }
            result["data"].update(geo_data)
        return result
    except Exception as e:
        return {"status": False, "error": str(e)}


def _reallyfreegeoip_org_ipv4(geo: bool=False, timeout: Union[float, Tuple[float, float]]
                              =5) -> Dict[str, Union[bool, Dict[str, Union[str, float]], str]]:
    """
    Get public IP and geolocation using reallyfreegeoip.org.

    :param geo: geolocation flag
    :param timeout: timeout value for API
    """
    try:
        data = _get_json_ipv4_forced(url="https://reallyfreegeoip.org/json/", timeout=timeout)
        result = {"status": True, "data": {"ip": data["ip"], "api": "reallyfreegeoip.org"}}
        if geo:
            geo_data = {
                "city": data.get("city"),
                "region": data.get("region_name"),
                "country": data.get("country_name"),
                "country_code": data.get("country_code"),
                "latitude": data.get("latitude"),
                "longitude": data.get("longitude"),
                "organization": None,  # does not provide organization
                "timezone": data.get("time_zone")
            }
            result["data"].update(geo_data)
        return result
    except Exception as e:
        return {"status": False, "error": str(e)}


def _ident_me_ipv4(geo: bool=False, timeout: Union[float, Tuple[float, float]]
                   =5) -> Dict[str, Union[bool, Dict[str, Union[str, float]], str]]:
    """
    Get public IP and geolocation using ident.me.

    :param geo: geolocation flag
    :param timeout: timeout value for API
    """
    try:
        data = _get_json_standard(url="https://4.ident.me/json", timeout=timeout)
        result = {"status": True, "data": {"ip": data["ip"], "api": "ident.me"}}
        if geo:
            geo_data = {
                "city": data.get("city"),
                "region": None,
                "country": data.get("country"),
                "country_code": data.get("cc"),
                "latitude": data.get("latitude"),
                "longitude": data.get("longitude"),
                "organization": data.get("aso"),
                "timezone": data.get("tz")
            }
            result["data"].update(geo_data)
        return result
    except Exception as e:
        return {"status": False, "error": str(e)}


def _tnedi_me_ipv4(geo: bool=False, timeout: Union[float, Tuple[float, float]]
                   =5) -> Dict[str, Union[bool, Dict[str, Union[str, float]], str]]:
    """
    Get public IP and geolocation using tnedi.me.

    :param geo: geolocation flag
    :param timeout: timeout value for API
    """
    try:
        data = _get_json_standard(url="https://4.tnedi.me/json", timeout=timeout)
        result = {"status": True, "data": {"ip": data["ip"], "api": "tnedi.me"}}
        if geo:
            geo_data = {
                "city": data.get("city"),
                "region": None,
                "country": data.get("country"),
                "country_code": data.get("cc"),
                "latitude": data.get("latitude"),
                "longitude": data.get("longitude"),
                "organization": data.get("aso"),
                "timezone": data.get("tz")
            }
            result["data"].update(geo_data)
        return result
    except Exception as e:
        return {"status": False, "error": str(e)}


def _myip_la_ipv4(geo: bool=False, timeout: Union[float, Tuple[float, float]]=5
                  ) -> Dict[str, Union[bool, Dict[str, Union[str, float]], str]]:
    """
    Get public IP and geolocation using myip.la.

    :param geo: geolocation flag
    :param timeout: timeout value for API
    """
    try:
        data = _get_json_ipv4_forced(url="https://api.myip.la/en?json", timeout=timeout)
        result = {"status": True, "data": {"ip": data["ip"], "api": "myip.la"}}
        if geo:
            loc = data.get("location", {})
            geo_data = {
                "city": loc.get("city"),
                "region": loc.get("province"),
                "country": loc.get("country_name"),
                "country_code": loc.get("country_code"),
                "latitude": float(loc.get("latitude")) if loc.get("latitude") else None,
                "longitude": float(loc.get("longitude")) if loc.get("longitude") else None,
                "organization": None,
                "timezone": None
            }
            result["data"].update(geo_data)
        return result
    except Exception as e:
        return {"status": False, "error": str(e)}


def _freeipapi_com_ipv4(geo: bool=False, timeout: Union[float, Tuple[float, float]]=5
                        ) -> Dict[str, Union[bool, Dict[str, Union[str, float]], str]]:
    """
    Get public IP and geolocation using freeipapi.com.

    :param geo: geolocation flag
    :param timeout: timeout value for API
    """
    try:
        data = _get_json_ipv4_forced(url="https://freeipapi.com/api/json", timeout=timeout)
        result = {"status": True, "data": {"ip": data["ipAddress"], "api": "freeipapi.com"}}
        if geo:
            geo_data = {
                "city": data.get("cityName"),
                "region": data.get("regionName"),
                "country": data.get("countryName"),
                "country_code": data.get("countryCode"),
                "latitude": data.get("latitude"),
                "longitude": data.get("longitude"),
                "organization": None,
                "timezone": data.get("timeZone")
            }
            result["data"].update(geo_data)
        return result
    except Exception as e:
        return {"status": False, "error": str(e)}


IPV4_API_MAP = {
    IPv4API.IFCONFIG_CO: {
        "thread_safe": False,
        "geo": True,
        "function": _ifconfig_co_ipv4
    },
    IPv4API.IDENT_ME: {
        "thread_safe": True,
        "geo": True,
        "function": _ident_me_ipv4
    },
    IPv4API.TNEDI_ME: {
        "thread_safe": True,
        "geo": True,
        "function": _tnedi_me_ipv4
    },
    IPv4API.IP_SB: {
        "thread_safe": True,
        "geo": True,
        "function": _ip_sb_ipv4
    },
    IPv4API.IPLEAK_NET: {
        "thread_safe": True,
        "geo": True,
        "function": _ipleak_net_ipv4
    },
    IPv4API.MY_IP_IO: {
        "thread_safe": True,
        "geo": True,
        "function": _my_ip_io_ipv4
    },
    IPv4API.IP_API_COM: {
        "thread_safe": False,
        "geo": True,
        "function": _ip_api_com_ipv4
    },
    IPv4API.IPINFO_IO: {
        "thread_safe": False,
        "geo": True,
        "function": _ipinfo_io_ipv4
    },
    IPv4API.IPAPI_CO: {
        "thread_safe": False,
        "geo": True,
        "function": _ipapi_co_ipv4
    },
    IPv4API.REALLYFREEGEOIP_ORG: {
        "thread_safe": False,
        "geo": True,
        "function": _reallyfreegeoip_org_ipv4
    },
    IPv4API.FREEIPAPI_COM: {
        "thread_safe": False,
        "geo": True,
        "function": _freeipapi_com_ipv4,
    },
    IPv4API.MYIP_LA: {
        "thread_safe": False,
        "geo": True,
        "function": _myip_la_ipv4,
    },
}


def get_public_ipv4(api: IPv4API=IPv4API.AUTO_SAFE, geo: bool=False,
                    timeout: Union[float, Tuple[float, float]]=5,
                    max_retries: int = 0,
                    retry_delay: float = 1.0) -> Dict[str, Union[bool, Dict[str, Union[str, float]], str]]:
    """
    Get public IPv4 and geolocation info based on the selected API.

    :param api: public IPv4 API
    :param geo: geolocation flag
    :param timeout: timeout value for API
    :param max_retries: number of retries
    :param retry_delay: delay between retries (in seconds)
    """
    if api in [IPv4API.AUTO, IPv4API.AUTO_SAFE]:
        for _, api_data in IPV4_API_MAP.items():
            if api == IPv4API.AUTO_SAFE and not api_data["thread_safe"]:
                continue
            func = api_data["function"]
            result = _attempt_with_retries(
                func=func,
                max_retries=max_retries,
                retry_delay=retry_delay,
                geo=geo,
                timeout=timeout)
            if result["status"]:
                return result
        return {"status": False, "error": "All attempts failed."}
    else:
        api_data = IPV4_API_MAP.get(api)
        if api_data:
            func = api_data["function"]
            return _attempt_with_retries(
                func=func,
                max_retries=max_retries,
                retry_delay=retry_delay,
                geo=geo,
                timeout=timeout)
        return {"status": False, "error": "Unsupported API: {api}".format(api=api)}
