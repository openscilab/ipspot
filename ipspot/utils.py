# -*- coding: utf-8 -*-
"""ipspot utils."""
import ipaddress
from typing import Any



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
