# -*- coding: utf-8 -*-
"""ipspot utils."""
import ipaddress
import requests
from typing import Union, Tuple, Any
from .params import REQUEST_HEADERS


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


def filter_parameter(parameter: Any) -> Any:
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
