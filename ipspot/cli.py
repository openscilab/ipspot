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


def ipspot_info() -> None:  # pragma: no cover
    """Print ipspot details."""
    tprint("IPSpot")
    tprint("V:" + IPSPOT_VERSION)
    print(IPSPOT_OVERVIEW)
    print("Repo : " + IPSPOT_REPO)


def display_ip_info(ipv4_api: IPv4API = IPv4API.AUTO, geo: bool=False,
                    timeout: Union[float, Tuple[float, float]]=5) -> None:  # pragma: no cover
    """
    Print collected IP and location data.

    :param ipv4_api: public IPv4 API
    :param geo: geolocation flag
    :param timeout: timeout value for API
    """
    private_result = get_private_ipv4()
    print("Private IP:\n")
    print("  IP: {private_result[data][ip]}".format(private_result=private_result) if private_result["status"]
          else "  Error: {private_result[error]}".format(private_result=private_result))

    public_title = "\nPublic IP"
    if geo:
        public_title += " and Location Info"
    public_title += ":\n"
    print(public_title)
    public_result = get_public_ipv4(ipv4_api, geo=geo, timeout=timeout)
    if public_result["status"]:
        for name, parameter in sorted(public_result["data"].items()):
            print(
                "  {name}: {parameter}".format(
                    name=PARAMETERS_NAME_MAP[name],
                    parameter=filter_parameter(parameter)))
    else:
        print("  Error: {public_result[error]}".format(public_result=public_result))


def main() -> None:  # pragma: no cover
    """CLI main function."""
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--ipv4-api',
        help='public IPv4 API',
        type=str.lower,
        choices=[
            x.value for x in IPv4API],
        default=IPv4API.AUTO.value)
    parser.add_argument('--info', help='info', nargs="?", const=1)
    parser.add_argument('--version', help='version', nargs="?", const=1)
    parser.add_argument('--no-geo', help='no geolocation data', nargs="?", const=1, default=False)
    parser.add_argument('--timeout', help='timeout for the API request', type=float, default=5.0)

    args = parser.parse_args()
    if args.version:
        print(IPSPOT_VERSION)
    elif args.info:
        ipspot_info()
    else:
        ipv4_api = IPv4API(args.ipv4_api)
        geo = not args.no_geo
        display_ip_info(ipv4_api=ipv4_api, geo=geo, timeout=args.timeout)
