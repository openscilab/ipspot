# -*- coding: utf-8 -*-
"""ipspot utils."""
import time
import ipaddress
import requests
from typing import Callable, Dict
from typing import Union, Tuple, Any
from .params import REQUEST_HEADERS


def _attempt_with_retries(
    func: Callable,
    max_retries: int = 0,
    retry_delay: float = 1.0, **kwargs: dict) -> Dict[str, Union[bool, Dict[str, Union[str, float]], str]]:
    """
    Attempt a function call with retries and delay.

    :param func: function to execute
    :param max_retries: number of retries
    :param retry_delay: initial delay between retries (in seconds)
    :param kwargs: keyword arguments to pass to the function
    """
    max_retries = max(0, max_retries)
    result = {"status": False, "error": ""}
    for attempt in range(max_retries + 1):
        result = func(**kwargs)
        if result["status"]:
            break
        if attempt < max_retries:
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
