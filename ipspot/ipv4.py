# -*- coding: utf-8 -*-
"""ipspot ipv4 functions."""
import ipaddress
import socket
from typing import Union, Dict, List, Tuple
import requests
from requests.adapters import HTTPAdapter
from urllib3.poolmanager import PoolManager
from .utils import is_loopback
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


def _ipsb_ipv4(geo: bool=False, timeout: Union[float, Tuple[float, float]]
               =5) -> Dict[str, Union[bool, Dict[str, Union[str, float]], str]]:
    """
    Get public IP and geolocation using ip.sb.

    :param geo: geolocation flag
    :param timeout: timeout value for API
    """
    try:
        with requests.Session() as session:
            response = session.get("https://api-ipv4.ip.sb/geoip", headers=REQUEST_HEADERS, timeout=timeout)
            response.raise_for_status()
            data = response.json()
            result = {"status": True, "data": {"ip": data.get("ip"), "api": "ip.sb"}}
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


def _ipapi_ipv4(geo: bool=False, timeout: Union[float, Tuple[float, float]]
                =5) -> Dict[str, Union[bool, Dict[str, Union[str, float]], str]]:
    """
    Get public IP and geolocation using ip-api.com.

    :param geo: geolocation flag
    :param timeout: timeout value for API
    """
    try:
        with requests.Session() as session:
            session.mount("http://", IPv4HTTPAdapter())
            session.mount("https://", IPv4HTTPAdapter())
            response = session.get("http://ip-api.com/json/", headers=REQUEST_HEADERS, timeout=timeout)
            response.raise_for_status()
            data = response.json()
            if data.get("status") != "success":
                return {"status": False, "error": "ip-api lookup failed"}
            result = {"status": True, "data": {"ip": data.get("query"), "api": "ip-api.com"}}
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


def _ipinfo_ipv4(geo: bool=False, timeout: Union[float, Tuple[float, float]]
                 =5) -> Dict[str, Union[bool, Dict[str, Union[str, float]], str]]:
    """
    Get public IP and geolocation using ipinfo.io.

    :param geo: geolocation flag
    :param timeout: timeout value for API
    """
    try:
        with requests.Session() as session:
            session.mount("http://", IPv4HTTPAdapter())
            session.mount("https://", IPv4HTTPAdapter())
            response = session.get("https://ipinfo.io/json", headers=REQUEST_HEADERS, timeout=timeout)
            response.raise_for_status()
            data = response.json()
            result = {"status": True, "data": {"ip": data.get("ip"), "api": "ipinfo.io"}}
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


def _ident_me_ipv4(geo: bool=False, timeout: Union[float, Tuple[float, float]]
                   =5) -> Dict[str, Union[bool, Dict[str, Union[str, float]], str]]:
    """
    Get public IP and geolocation using ident.me.

    :param geo: geolocation flag
    :param timeout: timeout value for API
    """
    try:
        with requests.Session() as session:
            response = session.get("https://4.ident.me/json", headers=REQUEST_HEADERS, timeout=timeout)
            response.raise_for_status()
            data = response.json()
            result = {"status": True, "data": {"ip": data.get("ip"), "api": "ident.me"}}
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


def _tnedime_ipv4(geo: bool=False, timeout: Union[float, Tuple[float, float]]
                  =5) -> Dict[str, Union[bool, Dict[str, Union[str, float]], str]]:
    """
    Get public IP and geolocation using tnedi.me.

    :param geo: geolocation flag
    :param timeout: timeout value for API
    """
    try:
        with requests.Session() as session:
            response = session.get("https://4.tnedi.me/json", headers=REQUEST_HEADERS, timeout=timeout)
            response.raise_for_status()
            data = response.json()
            result = {"status": True, "data": {"ip": data.get("ip"), "api": "tnedi.me"}}
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


def get_public_ipv4(api: IPv4API=IPv4API.AUTO, geo: bool=False,
                    timeout: Union[float, Tuple[float, float]]=5) -> Dict[str, Union[bool, Dict[str, Union[str, float]], str]]:
    """
    Get public IPv4 and geolocation info based on the selected API.

    :param api: public IPv4 API
    :param geo: geolocation flag
    :param timeout: timeout value for API
    """
    api_map = {
        IPv4API.IDENTME: _ident_me_ipv4,
        IPv4API.TNEDIME: _tnedime_ipv4,
        IPv4API.IPSB: _ipsb_ipv4,
        IPv4API.IPAPI: _ipapi_ipv4,
        IPv4API.IPINFO: _ipinfo_ipv4,
    }

    if api == IPv4API.AUTO:
        for _, func in api_map.items():
            result = func(geo=geo, timeout=timeout)
            if result["status"]:
                return result
        return {"status": False, "error": "All attempts failed."}
    else:
        func = api_map.get(api)
        if func:
            return func(geo=geo, timeout=timeout)
        return {"status": False, "error": "Unsupported API: {api}".format(api=api)}
