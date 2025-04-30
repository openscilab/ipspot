<div align="center">
<img src="https://github.com/openscilab/ipspot/raw/main/otherfiles/logo.png" width="350">
<h1>IPSpot: A Python Tool to Fetch the System's IP Address</h1>
<br/>
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
- Download [Version 0.1](https://github.com/openscilab/ipspot/archive/v0.1.zip) or [Latest Source](https://github.com/openscilab/ipspot/archive/dev.zip)
- `pip install .`				

### PyPI

- Check [Python Packaging User Guide](https://packaging.python.org/installing/)     
- `pip install ipspot==0.1`						


## Usage

### Library

#### Public IPv4

```pycon
>>> from ipspot import get_public_ipv4, IPv4API
>>> get_public_ipv4(api=IPv4API.IPAPI)
{'status': True, 'data': {'ip': 'xx.xx.xx.xx', 'api': 'ip-api.com'}}
>>> get_public_ipv4(api=IPv4API.IPAPI, geo=True, timeout=10)
{'data': {'country_code': 'GB', 'latitude': 50.9097, 'longitude': -1.4043, 'api': 'ip-api.com', 'country': 'United Kingdom', 'timezone': 'Europe/London', 'organization': '', 'region': 'England', 'ip': 'xx.xx.xx.xx', 'city': 'Southampton'}, 'status': True}
```

#### Private IPv4

```pycon
>>> from ipspot import get_private_ipv4
>>> get_private_ipv4()
{'status': True, 'data': {'ip': '10.36.18.154'}}
```

### CLI

ℹ️ You can use `ipspot` or `python -m ipspot` to run this program

#### Version

```console
> ipspot --version

0.1
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

__     __     ___      _
\ \   / / _  / _ \    / |
 \ \ / / (_)| | | |   | |
  \ V /   _ | |_| | _ | |
   \_/   (_) \___/ (_)|_|



IPSpot is a Python library for retrieving the current system's IP address and location information.
It currently supports public and private IPv4 detection using multiple API providers with a fallback mechanism for reliability.
Designed with simplicity and modularity in mind, IPSpot offers quick IP and geolocation lookups directly from your machine.

Repo : https://github.com/openscilab/ipspot

```

#### Basic

```console
> ipspot
Private IP:

  10.36.18.154

Public IP and Location Info:

  API: ip-api.com
  City: Southampton
  Country: United Kingdom
  Country Code: GB
  IP: xx.xx.xx.xx
  Latitude: 50.9097
  Longitude: -1.4043
  Organization: N/A
  Region: England
  Timezone: Europe/London
```

#### IPv4 API

ℹ️ `ipv4-api` valid choices: [`auto`, `ipapi`, `ipinfo`, `ipsb`]

ℹ️ The default value: `auto`

```console
> ipspot --ipv4-api="ipinfo"
Private IP:

  10.36.18.154

Public IP and Location Info:

  API: ipinfo.io
  City: Leatherhead
  Country: N/A
  Country Code: GB
  IP: xx.xx.xx.xx
  Latitude: 51.2965
  Longitude: -0.3338
  Organization: AS212238 Datacamp Limited
  Region: England
  Timezone: Europe/London
```

#### No Geolocation

```console
> ipspot --no-geo
Private IP:

  IP: 10.36.18.154

Public IP:

  API: ipinfo.io
  IP: xx.xx.xx.xx
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

