# -*- coding: utf-8 -*-
"""ipspot CLI."""
import argparse
from typing import Union, Tuple
from art import tprint
from .ipv4 import get_public_ipv4, get_private_ipv4
from .ipv6 import get_public_ipv6, get_private_ipv6
from .utils import _filter_parameter
from .params import IPv4API, IPv6API, PARAMETERS_NAME_MAP
from .params import IPSPOT_OVERVIEW, IPSPOT_REPO, IPSPOT_VERSION


def ipspot_info() -> None:  # pragma: no cover
    """Print ipspot details."""
    tprint("IPSpot")
    tprint("V:" + IPSPOT_VERSION)
    print(IPSPOT_OVERVIEW)
    print("Repo : " + IPSPOT_REPO)


def display_ip_info(ipv4_api: IPv4API = IPv4API.AUTO_SAFE,
                    ipv6_api: IPv6API = IPv6API.AUTO_SAFE,
                    geo: bool=False,
                    timeout: Union[float, Tuple[float, float]]=5,
                    max_retries: int = 0, retry_delay: float = 1.0) -> None:  # pragma: no cover
    """
    Print collected IP and location data.

    :param ipv4_api: public IPv4 API
    :param ipv6_api: public IPv6 API
    :param geo: geolocation flag
    :param timeout: timeout value for API
    :param max_retries: number of retries
    :param retry_delay: delay between retries (in seconds)
    """
    print("Private IP:\n")
    private_ipv4_result = get_private_ipv4()
    if private_ipv4_result["status"]:
        private_ipv4 = private_ipv4_result["data"]["ip"]
    else:
        private_ipv4 = private_ipv4_result["error"]
    print("  IPv4: {private_ipv4}\n".format(private_ipv4=private_ipv4))

    private_ipv6_result = get_private_ipv6()
    if private_ipv6_result["status"]:
        private_ipv6 = private_ipv6_result["data"]["ip"]
    else:
        private_ipv6 = private_ipv6_result["error"]
    print("  IPv6: {private_ipv6}".format(private_ipv6=private_ipv6))

    public_title = "\nPublic IP"
    if geo:
        public_title += " and Location Info"
    public_title += ":\n"
    print(public_title)
    print("  IPv4:\n")
    public_ipv4_result = get_public_ipv4(
        ipv4_api,
        geo=geo,
        timeout=timeout,
        max_retries=max_retries,
        retry_delay=retry_delay)
    if public_ipv4_result["status"]:
        for name, parameter in sorted(public_ipv4_result["data"].items()):
            print(
                "    {name}: {parameter}".format(
                    name=PARAMETERS_NAME_MAP[name],
                    parameter=_filter_parameter(parameter)))
    else:
        print("    Error: {public_ipv4_result[error]}".format(public_ipv4_result=public_ipv4_result))

    print("\n  IPv6:\n")
    public_ipv6_result = get_public_ipv6(
        ipv6_api,
        geo=geo,
        timeout=timeout,
        max_retries=max_retries,
        retry_delay=retry_delay)
    if public_ipv6_result["status"]:
        for name, parameter in sorted(public_ipv6_result["data"].items()):
            print(
                "    {name}: {parameter}".format(
                    name=PARAMETERS_NAME_MAP[name],
                    parameter=_filter_parameter(parameter)))
    else:
        print("    Error: {public_ipv6_result[error]}".format(public_ipv6_result=public_ipv6_result))


def main() -> None:  # pragma: no cover
    """CLI main function."""
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--ipv4-api',
        help='public IPv4 API',
        type=str.lower,
        choices=[
            x.value for x in IPv4API],
        default=IPv4API.AUTO_SAFE.value)
    parser.add_argument(
        '--ipv6-api',
        help='public IPv6 API',
        type=str.lower,
        choices=[
            x.value for x in IPv6API],
        default=IPv6API.AUTO_SAFE.value)
    parser.add_argument('--info', help='info', nargs="?", const=1)
    parser.add_argument('--version', help='version', nargs="?", const=1)
    parser.add_argument('--no-geo', help='no geolocation data', nargs="?", const=1, default=False)
    parser.add_argument('--timeout', help='timeout for the API request', type=float, default=5.0)
    parser.add_argument('--max-retries', help='number of retries', type=int, default=0)
    parser.add_argument('--retry-delay', help='delay between retries (in seconds)', type=float, default=1.0)

    args = parser.parse_args()
    if args.version:
        print(IPSPOT_VERSION)
    elif args.info:
        ipspot_info()
    else:
        ipv4_api = IPv4API(args.ipv4_api)
        ipv6_api = IPv6API(args.ipv6_api)
        geo = not args.no_geo
        display_ip_info(
            ipv4_api=ipv4_api,
            ipv6_api=ipv6_api,
            geo=geo,
            timeout=args.timeout,
            max_retries=args.max_retries,
            retry_delay=args.retry_delay)
