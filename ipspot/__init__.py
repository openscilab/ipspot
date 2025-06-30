# -*- coding: utf-8 -*-
"""ipspot modules."""
from .params import IPSPOT_VERSION, IPv4API, IPv6API
from .ipv4 import get_private_ipv4, get_public_ipv4, is_ipv4
from .ipv6 import get_private_ipv6, get_public_ipv6, is_ipv6
from .utils import is_loopback
__version__ = IPSPOT_VERSION
