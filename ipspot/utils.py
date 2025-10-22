# -*- coding: utf-8 -*-
"""ipspot utils."""
import time
import ipaddress
import socket
import requests
from requests.adapters import HTTPAdapter
from urllib3.poolmanager import PoolManager
from typing import Callable, Dict
from typing import Union, Tuple, Any, Literal
from .params import REQUEST_HEADERS


class ForceIPHTTPAdapter(HTTPAdapter):
    """A custom HTTPAdapter that enforces IPv4 or IPv6 DNS resolution for HTTP(S) requests."""

    def __init__(self, version: Literal["ipv4", "ipv6"] = "ipv4", *args, **kwargs):
        """
        Initialize the adapter with the desired IP version.

        :param version: 'ipv4' or 'ipv6'
        """
        self.version = version.lower()
        if self.version not in ("ipv4", "ipv6"):
            raise ValueError("version must be either 'ipv4' or 'ipv6'")
        super().__init__(*args, **kwargs)

    def init_poolmanager(self, connections: int, maxsize: int, block: bool = False, **kwargs: dict) -> None:
        """
        Initialize the connection pool manager with DNS filtering based on the selected IP version.
        """
        self.poolmanager = PoolManager(
            num_pools=connections,
            maxsize=maxsize,
            block=block,
            socket_options=self._ip_socket_options(),
            **kwargs
        )

    def _ip_socket_options(self) -> list:
        """
        Temporarily patches socket.getaddrinfo to filter addresses based on the selected IP version.

        :return: an empty list of socket options; DNS patching occurs here
        """
        original_getaddrinfo = socket.getaddrinfo
        family = socket.AF_INET if self.version == "ipv4" else socket.AF_INET6

        def filtered_getaddrinfo(*args: list, **kwargs: dict) -> List[Tuple]:
            results = original_getaddrinfo(*args, **kwargs)
            return [res for res in results if res[0] == family]

        self._original_getaddrinfo = socket.getaddrinfo
        socket.getaddrinfo = filtered_getaddrinfo

        return []

    def __del__(self) -> None:
        """Restores the original socket.getaddrinfo function upon adapter deletion."""
        if hasattr(self, "_original_getaddrinfo"):
            socket.getaddrinfo = self._original_getaddrinfo


def _get_json_ip_forced(url: str, timeout: Union[float, Tuple[float, float]],
                        version: Literal["ipv4", "ipv6"] = "ipv4") -> dict:
    """
    Send GET request with forced IPv4/IPv6 using ForceIPHTTPAdapter that returns JSON response.

    :param url: API url
    :param timeout: timeout value for API
    :param version: 'ipv4' or 'ipv6' to select address family
    """
    with requests.Session() as session:
        session.mount("http://", ForceIPHTTPAdapter(version=version))
        session.mount("https://", ForceIPHTTPAdapter(version=version))
        response = session.get(url, headers=REQUEST_HEADERS, timeout=timeout)
        response.raise_for_status()
        return response.json()


def _attempt_with_retries(
        func: Callable,
        max_retries: int,
        retry_delay: float, **kwargs: dict) -> Dict[str, Union[bool, Dict[str, Union[str, float]], str]]:
    """
    Attempt a function call with retries and delay.

    :param func: function to execute
    :param max_retries: number of retries
    :param retry_delay: delay between retries (in seconds)
    :param kwargs: keyword arguments to pass to the function
    """
    max_retries = max(0, max_retries)
    result = {"status": False, "error": ""}
    for attempt in range(max_retries + 1):
        result = func(**kwargs)
        if result["status"]:
            break
        time.sleep(retry_delay)
    return result


def is_loopback(ip: str) -> bool:
    """
    Check if the given input IP is a loopback address.

    :param ip: input IP
    """
    try:
        ip_object = ipaddress.ip_address(ip)
        return ip_object.is_loopback
    except Exception:
        return False


def _filter_parameter(parameter: Any) -> Any:
    """
    Filter input parameter.

    :param parameter: input parameter
    """
    if parameter is None:
        return "N/A"
    if isinstance(parameter, str) and len(parameter.strip()) == 0:
        return "N/A"
    return parameter


def _get_json_standard(url: str, timeout: Union[float, Tuple[float, float]]) -> dict:
    """
    Send standard GET request that returns JSON response.

    :param url: API url
    :param timeout: timeout value for API
    """
    with requests.Session() as session:
        response = session.get(url, headers=REQUEST_HEADERS, timeout=timeout)
        response.raise_for_status()
        return response.json()
