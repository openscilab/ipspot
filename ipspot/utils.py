# -*- coding: utf-8 -*-
"""ipspot utils."""
import time
import ipaddress
import socket
import requests
from requests.adapters import HTTPAdapter
from typing import Callable, Dict
from typing import Union, Tuple, Any, List
from .params import REQUEST_HEADERS


class ForceIPHTTPAdapter(HTTPAdapter):
    """A custom HTTPAdapter that enforces IPv4 or IPv6 DNS resolution for HTTP(S) requests."""

    def __init__(self, version: str = "ipv4", *args: list, **kwargs: dict) -> None:
        """
        Initialize the adapter with the desired IP version.

        :param version: 'ipv4' or 'ipv6' to select address family
        :param args: additional list arguments for the HTTPAdapter
        :param kwargs: additional keyword arguments for the HTTPAdapter
        """
        self.version = version.lower()
        if self.version not in ("ipv4", "ipv6"):
            raise ValueError("version must be either 'ipv4' or 'ipv6'")
        super().__init__(*args, **kwargs)

    def send(self, *args: list, **kwargs: dict) -> Any:
        """
        Override send method to apply the monkey patch only during the request.

        :param args: additional list arguments for the send method
        :param kwargs: additional keyword arguments for the send method
        """
        family = socket.AF_INET if self.version == "ipv4" else socket.AF_INET6
        original_getaddrinfo = socket.getaddrinfo

        def filtered_getaddrinfo(*gargs: list, **gkwargs: dict) -> List[Tuple]:
            """
            Filter getaddrinfo.

            :param gargs: additional list arguments for the original_getaddrinfo function
            :param gkwargs: additional keyword arguments for the original_getaddrinfo function
            """
            results = original_getaddrinfo(*gargs, **gkwargs)
            return [res for res in results if res[0] == family]

        socket.getaddrinfo = filtered_getaddrinfo
        try:
            response = super().send(*args, **kwargs)
        finally:
            socket.getaddrinfo = original_getaddrinfo
        return response


def _get_json_force_ip(url: str, timeout: Union[float, Tuple[float, float]],
                       version: str = "ipv4") -> dict:
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
