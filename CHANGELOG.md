# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](http://keepachangelog.com/en/1.0.0/)
and this project adheres to [Semantic Versioning](http://semver.org/spec/v2.0.0.html).

## [Unreleased]
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

[Unreleased]: https://github.com/openscilab/ipspot/compare/v0.3...dev
[0.3]: https://github.com/openscilab/ipspot/compare/v0.2...v0.3
[0.2]: https://github.com/openscilab/ipspot/compare/v0.1...v0.2
[0.1]: https://github.com/openscilab/ipspot/compare/3216fb7...v0.1



