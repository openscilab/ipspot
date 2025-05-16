# -*- coding: utf-8 -*-
"""ipspot functions."""
import argparse
import ipaddress
import socket
from typing import Union, Dict, List, Tuple, Any
import requests
from requests.adapters import HTTPAdapter
from urllib3.poolmanager import PoolManager
from art import tprint
from .ipv4 import get_public_ipv4, get_private_ipv4
from .params import REQUEST_HEADERS, IPv4API, PARAMETERS_NAME_MAP
from .params import IPSPOT_OVERVIEW, IPSPOT_REPO, IPSPOT_VERSION



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
