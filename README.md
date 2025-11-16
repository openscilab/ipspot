<div align="center">
<img src="https://github.com/openscilab/ipspot/raw/main/otherfiles/logo.png" width="350">
<h1>IPSpot: A Python Tool to Fetch the System's IP Address</h1>
<br/>
<a href="https://codecov.io/gh/openscilab/ipspot"><img src="https://codecov.io/gh/openscilab/ipspot/graph/badge.svg?token=XCFKASULS8"></a>
<a href="https://badge.fury.io/py/ipspot"><img src="https://badge.fury.io/py/ipspot.svg" alt="PyPI version"></a>
<a href="https://www.python.org/"><img src="https://img.shields.io/badge/built%20with-Python3-green.svg" alt="built with Python3"></a>
<a href="https://github.com/openscilab/ipspot"><img alt="GitHub repo size" src="https://img.shields.io/github/repo-size/openscilab/ipspot"></a>
<a href="https://discord.gg/yyDV3T4cwU"><img src="https://img.shields.io/discord/1064533716615049236.svg" alt="Discord Channel"></a>
</div>			
				
## Overview	

<p align="justify">					
<b>IPSpot</b> is a Python library for retrieving the current system's IP address and location information. It currently supports public and private <b>IPv4</b> detection using multiple API providers with a fallback mechanism for reliability. Designed with simplicity and modularity in mind, <b>IPSpot</b> offers quick IP and geolocation lookups directly from your machine.
</p>

<table>
	<tr>
		<td align="center">PyPI Counter</td>
		<td align="center"><a href="http://pepy.tech/project/ipspot"><img src="http://pepy.tech/badge/ipspot"></a></td>
	</tr>
	<tr>
		<td align="center">Github Stars</td>
		<td align="center"><a href="https://github.com/openscilab/ipspot"><img src="https://img.shields.io/github/stars/openscilab/ipspot.svg?style=social&label=Stars"></a></td>
	</tr>
</table>



<table>
	<tr> 
		<td align="center">Branch</td>
		<td align="center">main</td>	
		<td align="center">dev</td>	
	</tr>
	<tr>
		<td align="center">CI</td>
		<td align="center"><img src="https://github.com/openscilab/ipspot/actions/workflows/test.yml/badge.svg?branch=main"></td>
		<td align="center"><img src="https://github.com/openscilab/ipspot/actions/workflows/test.yml/badge.svg?branch=dev"></td>
	</tr>
</table>

<table>
	<tr> 
		<td align="center">Code Quality</td>
		<td align="center"><a href="https://app.codacy.com/gh/openscilab/ipspot/dashboard?utm_source=gh&utm_medium=referral&utm_content=&utm_campaign=Badge_grade"><img src="https://app.codacy.com/project/badge/Grade/cb2ab6584eb443b8a33da4d4252480bc"/></a></td>
		<td align="center"><a href="https://www.codefactor.io/repository/github/openscilab/ipspot"><img src="https://www.codefactor.io/repository/github/openscilab/ipspot/badge" alt="CodeFactor"></a></td>
	</tr>
</table>


## Installation		

### Source Code
- Download [Version 0.6](https://github.com/openscilab/ipspot/archive/v0.6.zip) or [Latest Source](https://github.com/openscilab/ipspot/archive/dev.zip)
- `pip install .`				

### PyPI

- Check [Python Packaging User Guide](https://packaging.python.org/installing/)     
- `pip install ipspot==0.6`						


## Usage

### Library

#### Public IPv4

```pycon
>>> from ipspot import get_public_ipv4, IPv4API
>>> get_public_ipv4(api=IPv4API.IP_API_COM)
{'status': True, 'data': {'ip': 'xx.xx.xx.xx', 'api': 'ip-api.com'}}
>>> get_public_ipv4(api=IPv4API.IP_API_COM, geo=True, timeout=10)
{'data': {'country_code': 'GB', 'latitude': 50.9097, 'longitude': -1.4043, 'api': 'ip-api.com', 'country': 'United Kingdom', 'timezone': 'Europe/London', 'organization': '', 'region': 'England', 'ip': 'xx.xx.xx.xx', 'city': 'Southampton'}, 'status': True}
>>> get_public_ipv4(api=IPv4API.IP_API_COM, geo=True, timeout=10, max_retries=5, retry_delay=4)
{'data': {'country_code': 'GB', 'latitude': 50.9097, 'longitude': -1.4043, 'api': 'ip-api.com', 'country': 'United Kingdom', 'timezone': 'Europe/London', 'organization': '', 'region': 'England', 'ip': 'xx.xx.xx.xx', 'city': 'Southampton'}, 'status': True}
```

#### Private IPv4

```pycon
>>> from ipspot import get_private_ipv4
>>> get_private_ipv4()
{'status': True, 'data': {'ip': '10.36.18.154'}}
```

#### Public IPv6

```pycon
>>> from ipspot import get_public_ipv6, IPv6API
>>> get_public_ipv6(api=IPv6API.IP_SB)
{'data': {'api': 'ip.sb', 'ip': 'xx:xx:xx:xx::xx'}, 'status': True}
>>> get_public_ipv6(api=IPv6API.IP_SB, geo=True, timeout=10)
{'data': {'latitude': 51.2993, 'region': None, 'city': None, 'country_code': 'DE', 'api': 'ip.sb', 'longitude': 9.491, 'country': 'Germany', 'organization': 'Hetzner Online', 'timezone': 'Europe/Berlin', 'ip': 'xx:xx:xx:xx::xx'}, 'status': True}
>>> get_public_ipv6(api=IPv6API.IP_SB, geo=True, timeout=10, max_retries=5, retry_delay=4)
{'data': {'latitude': 51.2993, 'region': None, 'city': None, 'country_code': 'DE', 'api': 'ip.sb', 'longitude': 9.491, 'country': 'Germany', 'organization': 'Hetzner Online', 'timezone': 'Europe/Berlin', 'ip': 'xx:xx:xx:xx::xx'}, 'status': True}
```

#### Private IPv6

```pycon
>>> from ipspot import get_private_ipv6
>>> get_private_ipv6()
{'status': True, 'data': {'ip': 'fe80::e1bd:f78:b233:21c9'}}
```

### CLI

ℹ️ You can use `ipspot` or `python -m ipspot` to run this program

#### Version

```console
> ipspot --version

0.6
```

#### Info

```console
> ipspot --info

 ___  ____   ____                 _
|_ _||  _ \ / ___|  _ __    ___  | |_
 | | | |_) |\___ \ | '_ \  / _ \ | __|
 | | |  __/  ___) || |_) || (_) || |_
|___||_|    |____/ | .__/  \___/  \__|
                   |_|

__     __     ___       __
\ \   / / _  / _ \     / /_
 \ \ / / (_)| | | |   | '_ \
  \ V /   _ | |_| | _ | (_) |
   \_/   (_) \___/ (_) \___/



IPSpot is a Python library for retrieving the current system's IP address and location information.
It currently supports public and private IPv4 detection using multiple API providers with a fallback mechanism for reliability.
Designed with simplicity and modularity in mind, IPSpot offers quick IP and geolocation lookups directly from your machine.

Repo : https://github.com/openscilab/ipspot

```

#### Basic

```console
> ipspot
Private IP:

  IPv4: 192.168.1.35

  IPv6: fe80::e1bd:f78:b233:21c9

Public IP and Location Info:

  IPv4:

    API: ipinfo.io
    City: Nuremberg
    Country: Germany
    Country Code: DE
    IP: xx.xx.xx.xx
    Latitude: 49.4527
    Longitude: 11.0783
    Organization: Hetzner Online GmbH
    Region: Bavaria
    Timezone: Europe/Berlin

  IPv6:

    API: ip.sb
    City: N/A
    Country: Germany
    Country Code: DE
    IP: xx:xx:xx:xx::xx
    Latitude: 51.2993
    Longitude: 9.491
    Organization: Hetzner Online
    Region: N/A
    Timezone: Europe/Berlin
```

#### IPv4 API

ℹ️ `ipv4-api` valid choices: [`auto-safe`, `auto`, `ip-api.com`, `ipinfo.io`, `ip.sb`, `ident.me`, `tnedi.me`, `ipapi.co`, `ipleak.net`, `my-ip.io`, `ifconfig.co`, `reallyfreegeoip.org`, `freeipapi.com`, `myip.la`, `ipquery.io`, `ipwho.is`, `wtfismyip.com`]

ℹ️ The default value: `auto-safe`

```console
> ipspot --ipv4-api="ipinfo.io"
Private IP:

  IPv4: 192.168.1.35

  IPv6: fe80::e1bd:f78:b233:21c9

Public IP and Location Info:

  IPv4:

    API: ipinfo.io
    City: Nuremberg
    Country: Germany
    Country Code: DE
    IP: xx.xx.xx.xx
    Latitude: 49.4527
    Longitude: 11.0783
    Organization: Hetzner Online GmbH
    Region: Bavaria
    Timezone: Europe/Berlin

  IPv6:

    API: ip.sb
    City: N/A
    Country: Germany
    Country Code: DE
    IP: xx:xx:xx:xx::xx
    Latitude: 51.2993
    Longitude: 9.491
    Organization: Hetzner Online
    Region: N/A
    Timezone: Europe/Berlin
```

#### IPv6 API

ℹ️ `ipv6-api` valid choices: [`auto-safe`, `auto`, `ip.sb`, `ident.me`, `tnedi.me`, `ipleak.net`, `my-ip.io`, `ifconfig.co`, `reallyfreegeoip.org`, `myip.la`, `freeipapi.com`]

ℹ️ The default value: `auto-safe`

```console
> ipspot --ipv6-api="ip.sb"
Private IP:

  IPv4: 192.168.1.35

  IPv6: fe80::e1bd:f78:b233:21c9

Public IP and Location Info:

  IPv4:

    API: ipinfo.io
    City: Nuremberg
    Country: Germany
    Country Code: DE
    IP: xx.xx.xx.xx
    Latitude: 49.4527
    Longitude: 11.0783
    Organization: Hetzner Online GmbH
    Region: Bavaria
    Timezone: Europe/Berlin

  IPv6:

    API: ip.sb
    City: N/A
    Country: Germany
    Country Code: DE
    IP: xx:xx:xx:xx::xx
    Latitude: 51.2993
    Longitude: 9.491
    Organization: Hetzner Online
    Region: N/A
    Timezone: Europe/Berlin
```

#### No Geolocation

```console
> ipspot --no-geo
Private IP:

  IPv4: 192.168.1.35

  IPv6: fe80::5c40:769f:22de:c196

Public IP:

  IPv4:

    API: tnedi.me
    IP: xx.xx.xx.xx

  IPv6:

    API: ip.sb
    IP: xx:xx:xx:xx::xx
```

## Issues & Bug Reports			

Just fill an issue and describe it. We'll check it ASAP!

- Please complete the issue template

You can also join our discord server

<a href="https://discord.gg/yyDV3T4cwU">
  <img src="https://img.shields.io/discord/1064533716615049236.svg?style=for-the-badge" alt="Discord Channel">
</a>

## Show Your Support
								
<h3>Star This Repo</h3>					

Give a ⭐️ if this project helped you!

<h3>Donate to Our Project</h3>	

If you do like our project and we hope that you do, can you please support us? Our project is not and is never going to be working for profit. We need the money just so we can continue doing what we do ;-)			

<a href="https://openscilab.com/#donation" target="_blank"><img src="https://github.com/openscilab/ipspot/raw/main/otherfiles/donation.png" height="90px" width="270px" alt="IPSpot Donation"></a>

