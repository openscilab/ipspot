# -*- coding: utf-8 -*-
"""ipspot params."""
from enum import Enum

IPSPOT_VERSION = "0.7"

IPSPOT_OVERVIEW = '''
IPSpot is a Python library for retrieving the current system's IP data and detailed location information such as region, longitude, and latitude.
It supports both public and private IPv4 and IPv6 detection through multiple API providers, using a fallback mechanism for improved reliability.
It has a simple and modular design, making it easy to perform fast IP, geolocation, provider, and regional lookups directly from your machine.
'''

IPSPOT_REPO = "https://github.com/openscilab/ipspot"

REQUEST_HEADERS = {
    'User-Agent': 'IPSpot/{version} ({repo})'.format(version=IPSPOT_VERSION, repo=IPSPOT_REPO),
    'Accept': 'application/json'
}


class IPv4API(Enum):
    """Public IPv4 API enum."""

    AUTO = "auto"
    AUTO_SAFE = "auto-safe"
    IP_API_COM = "ip-api.com"
    IPAPI_CO = "ipapi.co"
    IPINFO_IO = "ipinfo.io"
    IP_SB = "ip.sb"
    IDENT_ME = "ident.me"
    TNEDI_ME = "tnedi.me"
    IPLEAK_NET = "ipleak.net"
    MY_IP_IO = "my-ip.io"
    IFCONFIG_CO = "ifconfig.co"
    REALLYFREEGEOIP_ORG = "reallyfreegeoip.org"
    MYIP_LA = "myip.la"
    FREEIPAPI_COM = "freeipapi.com"
    IPQUERY_IO = "ipquery.io"
    IPWHO_IS = "ipwho.is"
    WTFISMYIP_COM = "wtfismyip.com"
    MYIP_WTF = "myip.wtf"
    WHOER_NET = "whoer.net"


class IPv6API(Enum):
    """Public IPv6 API enum."""

    AUTO = "auto"
    AUTO_SAFE = "auto-safe"
    IP_SB = "ip.sb"
    IDENT_ME = "ident.me"
    TNEDI_ME = "tnedi.me"
    IPLEAK_NET = "ipleak.net"
    MY_IP_IO = "my-ip.io"
    IFCONFIG_CO = "ifconfig.co"
    REALLYFREEGEOIP_ORG = "reallyfreegeoip.org"
    MYIP_LA = "myip.la"
    FREEIPAPI_COM = "freeipapi.com"
    WTFISMYIP_COM = "wtfismyip.com"
    MYIP_WTF = "myip.wtf"


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

PUBLIC_IPV4_ERROR = "Unable to retrieve public IPv4 information."
PRIVATE_IPV4_ERROR = "Unable to retrieve private IPv4 address."
PUBLIC_IPV6_ERROR = "Unable to retrieve public IPv6 information."
PRIVATE_IPV6_ERROR = "Unable to retrieve private IPv6 address."
