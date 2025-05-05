# -*- coding: utf-8 -*-
"""ipspot params."""
from enum import Enum

IPSPOT_VERSION = "0.2"

IPSPOT_OVERVIEW = '''
IPSpot is a Python library for retrieving the current system's IP address and location information.
It currently supports public and private IPv4 detection using multiple API providers with a fallback mechanism for reliability.
Designed with simplicity and modularity in mind, IPSpot offers quick IP and geolocation lookups directly from your machine.
'''

IPSPOT_REPO = "https://github.com/openscilab/ipspot"

REQUEST_HEADERS = {
    'User-Agent': 'IPSpot/{version} ({repo})'.format(version=IPSPOT_VERSION, repo=IPSPOT_REPO),
    'Accept': 'application/json'
}


class IPv4API(Enum):
    """Public IPv4 API enum."""

    AUTO = "auto"
    IPAPI = "ipapi"
    IPINFO = "ipinfo"
    IPSB = "ipsb"
    IDENTME = "identme"


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
