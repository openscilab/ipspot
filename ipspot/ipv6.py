# -*- coding: utf-8 -*-
"""ipspot ipv6 functions."""
import ipaddress
import socket
from typing import Union, Dict, List, Tuple
from .params import IPv6API
from .utils import is_loopback, _get_json_standard


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


IPV6_API_MAP = {
    IPv6API.IP_SB: {
        "thread_safe": True,
        "geo": True,
        "function": _ip_sb_ipv6
    }
}
