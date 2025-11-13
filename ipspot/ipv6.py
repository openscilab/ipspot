# -*- coding: utf-8 -*-
"""ipspot ipv6 functions."""
import ipaddress
import socket
from typing import Union, Dict, List, Tuple
from .params import IPv6API
from .utils import is_loopback, _attempt_with_retries
from .utils import _get_json_standard, _get_json_force_ip


def is_ipv6(ip: str) -> bool:
    """
    Check if the given input is a valid IPv6 address.

    :param ip: input IP
    """
    if not isinstance(ip, str):
        return False
    try:
        _ = ipaddress.IPv6Address(ip)
        return True
    except Exception:
        return False


def get_private_ipv6() -> Dict[str, Union[bool, Dict[str, str], str]]:
    """Retrieve the private IPv6 address."""
    try:
        with socket.socket(socket.AF_INET6, socket.SOCK_DGRAM) as s:
            s.connect(("2001:4860:4860::8888", 80))
            private_ip = s.getsockname()[0]
            private_ip = private_ip.split("%")[0]
        if is_ipv6(private_ip) and not is_loopback(private_ip):
            return {"status": True, "data": {"ip": private_ip}}
        return {"status": False, "error": "Could not identify a non-loopback IPv6 address for this system."}
    except Exception as e:
        return {"status": False, "error": str(e)}


def _ip_sb_ipv6(geo: bool=False, timeout: Union[float, Tuple[float, float]]
                =5) -> Dict[str, Union[bool, Dict[str, Union[str, float]], str]]:
    """
    Get public IP and geolocation using ip.sb.

    :param geo: geolocation flag
    :param timeout: timeout value for API
    """
    try:
        data = _get_json_standard(url="https://api-ipv6.ip.sb/geoip", timeout=timeout)
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


def _ident_me_ipv6(geo: bool=False, timeout: Union[float, Tuple[float, float]]
                   =5) -> Dict[str, Union[bool, Dict[str, Union[str, float]], str]]:
    """
    Get public IP and geolocation using ident.me.

    :param geo: geolocation flag
    :param timeout: timeout value for API
    """
    try:
        data = _get_json_standard(url="https://6.ident.me/json", timeout=timeout)
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


def _tnedi_me_ipv6(geo: bool=False, timeout: Union[float, Tuple[float, float]]
                   =5) -> Dict[str, Union[bool, Dict[str, Union[str, float]], str]]:
    """
    Get public IP and geolocation using tnedi.me.

    :param geo: geolocation flag
    :param timeout: timeout value for API
    """
    try:
        data = _get_json_standard(url="https://6.tnedi.me/json", timeout=timeout)
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


def _ipleak_net_ipv6(geo: bool=False, timeout: Union[float, Tuple[float, float]]
                     =5) -> Dict[str, Union[bool, Dict[str, Union[str, float]], str]]:
    """
    Get public IP and geolocation using ipleak.net.

    :param geo: geolocation flag
    :param timeout: timeout value for API
    """
    try:
        data = _get_json_standard(url="https://ipv6.ipleak.net/json/", timeout=timeout)
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


def _my_ip_io_ipv6(geo: bool=False, timeout: Union[float, Tuple[float, float]]
                   =5) -> Dict[str, Union[bool, Dict[str, Union[str, float]], str]]:
    """
    Get public IP and geolocation using my-ip.io.

    :param geo: geolocation flag
    :param timeout: timeout value for API
    """
    try:
        data = _get_json_standard(url="https://api6.my-ip.io/v2/ip.json", timeout=timeout)
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


def _ifconfig_co_ipv6(geo: bool=False, timeout: Union[float, Tuple[float, float]]  # very low rate limit
                      =5) -> Dict[str, Union[bool, Dict[str, Union[str, float]], str]]:
    """
    Get public IP and geolocation using ifconfig.co.

    :param geo: geolocation flag
    :param timeout: timeout value for API
    """
    try:
        data = _get_json_force_ip(url="https://ifconfig.co/json", timeout=timeout, version="ipv6")
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


def _reallyfreegeoip_org_ipv6(geo: bool=False, timeout: Union[float, Tuple[float, float]]
                              =5) -> Dict[str, Union[bool, Dict[str, Union[str, float]], str]]:
    """
    Get public IP and geolocation using reallyfreegeoip.org.

    :param geo: geolocation flag
    :param timeout: timeout value for API
    """
    try:
        data = _get_json_force_ip(url="https://reallyfreegeoip.org/json/", timeout=timeout, version="ipv6")
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


def _myip_la_ipv6(geo: bool=False, timeout: Union[float, Tuple[float, float]]
                  =5) -> Dict[str, Union[bool, Dict[str, Union[str, float]], str]]:
    """
    Get public IP and geolocation using myip.la.

    :param geo: geolocation flag
    :param timeout: timeout value for API
    """
    try:
        data = _get_json_force_ip(url="https://api.myip.la/en?json", timeout=timeout, version="ipv6")
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


def _freeipapi_com_ipv6(geo: bool=False, timeout: Union[float, Tuple[float, float]]
                        =5) -> Dict[str, Union[bool, Dict[str, Union[str, float]], str]]:
    """
    Get public IP and geolocation using freeipapi.com.

    :param geo: geolocation flag
    :param timeout: timeout value for API
    """
    try:
        data = _get_json_force_ip(url="https://free.freeipapi.com/api/json", timeout=timeout, version="ipv6")
        result = {"status": True, "data": {"ip": data["ipAddress"], "api": "freeipapi.com"}}
        tzs = data.get("timeZones", [])
        if geo:
            geo_data = {
                "city": data.get("cityName"),
                "region": data.get("regionName"),
                "country": data.get("countryName"),
                "country_code": data.get("countryCode"),
                "latitude": data.get("latitude"),
                "longitude": data.get("longitude"),
                "organization": data.get("asnOrganization"),
                "timezone": tzs[0] if len(tzs) > 0 else None
            }
            result["data"].update(geo_data)
        return result
    except Exception as e:
        return {"status": False, "error": str(e)}


IPV6_API_MAP = {
    IPv6API.IP_SB: {
        "thread_safe": True,
        "geo": True,
        "function": _ip_sb_ipv6
    },
    IPv6API.IDENT_ME: {
        "thread_safe": True,
        "geo": True,
        "function": _ident_me_ipv6
    },
    IPv6API.TNEDI_ME: {
        "thread_safe": True,
        "geo": True,
        "function": _tnedi_me_ipv6
    },
    IPv6API.IPLEAK_NET: {
        "thread_safe": True,
        "geo": True,
        "function": _ipleak_net_ipv6
    },
    IPv6API.MY_IP_IO: {
        "thread_safe": True,
        "geo": True,
        "function": _my_ip_io_ipv6
    },
    IPv6API.IFCONFIG_CO: {
        "thread_safe": False,
        "geo": True,
        "function": _ifconfig_co_ipv6
    },
    IPv6API.REALLYFREEGEOIP_ORG: {
        "thread_safe": False,
        "geo": True,
        "function": _reallyfreegeoip_org_ipv6
    },
    IPv6API.MYIP_LA: {
        "thread_safe": False,
        "geo": True,
        "function": _myip_la_ipv6
    },
    IPv6API.FREEIPAPI_COM: {
        "thread_safe": False,
        "geo": True,
        "function": _freeipapi_com_ipv6
    }
}


def get_public_ipv6(api: IPv6API=IPv6API.AUTO_SAFE, geo: bool=False,
                    timeout: Union[float, Tuple[float, float]]=5,
                    max_retries: int = 0,
                    retry_delay: float = 1.0) -> Dict[str, Union[bool, Dict[str, Union[str, float]], str]]:
    """
    Get public IPv6 and geolocation info based on the selected API.

    :param api: public IPv6 API
    :param geo: geolocation flag
    :param timeout: timeout value for API
    :param max_retries: number of retries
    :param retry_delay: delay between retries (in seconds)
    """
    if api in [IPv6API.AUTO, IPv6API.AUTO_SAFE]:
        for _, api_data in IPV6_API_MAP.items():
            if api == IPv6API.AUTO_SAFE and not api_data["thread_safe"]:
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
        api_data = IPV6_API_MAP.get(api)
        if api_data:
            func = api_data["function"]
            return _attempt_with_retries(
                func=func,
                max_retries=max_retries,
                retry_delay=retry_delay,
                geo=geo,
                timeout=timeout)
        return {"status": False, "error": "Unsupported API: {api}".format(api=api)}
