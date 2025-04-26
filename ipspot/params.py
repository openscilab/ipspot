# -*- coding: utf-8 -*-
"""ipspot params."""
from enum import Enum

IPSPOT_VERSION = "0.1"

IPSPOT_OVERVIEW = '''
IPSpot is a Python library for retrieving the current system's IP address and location information.
It currently supports public and private IPv4 detection using multiple API providers with a fallback mechanism for reliability.
Designed with simplicity and modularity in mind, IPSpot offers quick IP and geolocation lookups directly from your machine.
'''

REQUEST_HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/123.0.0.0 Safari/537.36"
}

IPSPOT_REPO = "Repo : https://github.com/openscilab/ipspot"


class IPv4API(Enum):
    """Public IPv4 API enum."""

    AUTO = "auto"
    IPAPI = "ipapi"
    IPINFO = "ipinfo"
    IPSB = "ipsb"


PARAMETERS_NAME_MAP = {
    "ip": "IP",
    "city": "City",
    "region": "Region",
    "country": "Country",
    "country_code": "Country Code",
    "timezone": "Timezone",
    "latitude": "Latitude",
    "longitude": "Longitude",
    "organization": "Organization",
    "api": "API"
}
