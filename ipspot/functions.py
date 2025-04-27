# -*- coding: utf-8 -*-
"""ipspot functions."""
import argparse
import socket
from typing import Union, Dict, Tuple, Any
import requests
from art import tprint
from .params import REQUEST_HEADERS, IPv4API, PARAMETERS_NAME_MAP
from .params import IPSPOT_OVERVIEW, IPSPOT_REPO, IPSPOT_VERSION


def ipspot_info() -> None:
    """Print ipspot details."""
    tprint("IPSpot")
    tprint("V:" + IPSPOT_VERSION)
    print(IPSPOT_OVERVIEW)
    print(IPSPOT_REPO)


def get_private_ipv4() -> Dict[str, Union[bool, Dict[str, str], str]]:
    """Retrieve the private IPv4 address."""
    try:
        hostname = socket.gethostname()
        private_ip = socket.gethostbyname(hostname)
        return {"status": True, "data": {"ip": private_ip}}
    except Exception as e:
        return {"status": False, "error": str(e)}


def _ipsb_ipv4(geo: bool=False, timeout: Union[float, Tuple[float, float]]=5) -> Dict[str, Union[bool, Dict[str, Union[str, float]], str]]:
    """
    Get public IP and geolocation using ip.sb.

    :param geo: geolocation flag
    :param timeout: timeout value for API
    """
    try:
        response = requests.get("https://api.ip.sb/geoip", headers=REQUEST_HEADERS, timeout=timeout)
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


def _ipapi_ipv4(geo: bool=False, timeout: Union[float, Tuple[float, float]]=5) -> Dict[str, Union[bool, Dict[str, Union[str, float]], str]]:
    """
    Get public IP and geolocation using ip-api.com.

    :param geo: geolocation flag
    :param timeout: timeout value for API
    """
    try:
        response = requests.get("http://ip-api.com/json/", timeout=timeout)
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


def _ipinfo_ipv4(geo: bool=False, timeout: Union[float, Tuple[float, float]]=5) -> Dict[str, Union[bool, Dict[str, Union[str, float]], str]]:
    """
    Get public IP and geolocation using ipinfo.io.

    :param geo: geolocation flag
    :param timeout: timeout value for API
    """
    try:
        response = requests.get("https://ipinfo.io/json", timeout=timeout)
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


def get_public_ipv4(api: IPv4API=IPv4API.AUTO,
                    geo: bool=False,
                    timeout: Union[float, Tuple[float, float]]=5) -> Dict[str, Union[bool, Dict[str, Union[str, float]], str]]:
    """
    Get public IPv4 and geolocation info based on the selected API.

    :param api: public IPv4 API
    :param geo: geolocation flag
    :param timeout: timeout value for API
    """
    api_map = {
        IPv4API.IPAPI: _ipapi_ipv4,
        IPv4API.IPINFO: _ipinfo_ipv4,
        IPv4API.IPSB: _ipsb_ipv4
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


def display_ip_info(ipv4_api: IPv4API = IPv4API.AUTO, geo: bool=False, timeout: Union[float, Tuple[float, float]]=5) -> None:
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


def main() -> None:
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
