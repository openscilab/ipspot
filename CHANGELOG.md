# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](http://keepachangelog.com/en/1.0.0/)
and this project adheres to [Semantic Versioning](http://semver.org/spec/v2.0.0.html).

## [Unreleased]
## [0.6] - 2025-11-18
### Added
- `ForceIPHTTPAdapter` class
- `_get_json_force_ip` function
- Support [ifconfig.co](https://ifconfig.co/json) IPv6 API
- Support [reallyfreegeoip.org](https://reallyfreegeoip.org/json/) IPv6 API
- Support [myip.la](https://api.myip.la/en?json) IPv6 API
- Support [freeipapi.com](https://freeipapi.com/api/json) IPv6 API
### Changed
- [freeipapi.com](https://freeipapi.com/api/json) IPv4 API bug fixed
- `README.md` updated
### Removed
- `IPv4HTTPAdapter` class
- `_get_json_ipv4_forced` function
## [0.5] - 2025-10-17
### Added
- `setup-warp` action
- Support [ipwho.is](https://ipwho.is/)
- Support [ipquery.io](http://api.ipquery.io/?format=json)
- Support [wtfismyip.com](https://wtfismyip.com/json)
- Support [ident.me](https://ident.me/json) IPv6 API
- Support [tnedi.me](https://tnedi.me/json) IPv6 API
- Support [ip.sb](https://api.ip.sb/geoip) IPv6 API
- Support [ipleak.net](https://ipleak.net/json/) IPv6 API
- Support [my-ip.io](https://www.my-ip.io/) IPv6 API
- `is_ipv6` function
- `get_private_ipv6` function
- `get_public_ipv6` function
- `IPv6API` enum
- `--ipv6-api` argument
### Changed
- Test system modified
- `README.md` updated
## [0.4] - 2025-06-09
### Added
- Support [ipapi.co](https://ipapi.co/json/)
- Support [ipleak.net](https://ipleak.net/json/)
- Support [my-ip.io](https://www.my-ip.io/)
- Support [ifconfig.co](https://ifconfig.co/json)
- Support [reallyfreegeoip.org](https://reallyfreegeoip.org/json/)
- Support [myip.la](https://api.myip.la/en?json)
- Support [freeipapi.com](https://freeipapi.com/api/json/)
- `AUTO_SAFE` mode
- `_get_json_standard` function
- `_get_json_ipv4_forced` function
- `--max-retries` argument
- `--retry-delay` argument
### Changed
- `IPv4API.IPAPI` renamed to `IPv4API.IP_API_COM`
- `IPv4API.IPINFO` renamed to `IPv4API.IPINFO_IO`
- `IPv4API.IPSB` renamed to `IPv4API.IP_SB`
- `IPv4API.IDENTME` renamed to `IPv4API.IDENT_ME`
- `IPv4API.TNEDIME` renamed to `IPv4API.TNEDI_ME`
- `get_public_ipv4` function modified
- `filter_parameter` function renamed to `_filter_parameter`
- `README.md` updated
## [0.3] - 2025-05-19
### Added
- `is_ipv4` function
- `is_loopback` function
- `IPv4HTTPAdapter` class
- Support [ident.me](https://ident.me/json)
- Support [tnedi.me](https://tnedi.me/json)
### Changed
- `get_private_ipv4` function modified
- `get_public_ipv4` function modified
- `_ipsb_ipv4` function modified
- `_ipapi_ipv4` function modified
- `_ipinfo_ipv4` function modified
- `functions.py` renamed to `utils.py` 
- CLI functions moved to `cli.py`
- IPv4 functions moved to `ipv4.py`
- Test system modified
## [0.2] - 2025-05-04
### Added
- Support [ip.sb](https://api.ip.sb/geoip)
- `--timeout` argument
### Changed
- `README.md` updated
- Requests header updated
- Test system modified
## [0.1] - 2025-04-25
### Added
- Support [ipinfo.io](https://ipinfo.io)
- Support [ip-api.com](https://ip-api.com)
- `get_private_ipv4` function
- `get_public_ipv4` function
- `--info` and `--version` arguments
- `--ipv4-api` argument
- `--no-geo` argument
- Logo

[Unreleased]: https://github.com/openscilab/ipspot/compare/v0.6...dev
[0.6]: https://github.com/openscilab/ipspot/compare/v0.5...v0.6
[0.5]: https://github.com/openscilab/ipspot/compare/v0.4...v0.5
[0.4]: https://github.com/openscilab/ipspot/compare/v0.3...v0.4
[0.3]: https://github.com/openscilab/ipspot/compare/v0.2...v0.3
[0.2]: https://github.com/openscilab/ipspot/compare/v0.1...v0.2
[0.1]: https://github.com/openscilab/ipspot/compare/3216fb7...v0.1



