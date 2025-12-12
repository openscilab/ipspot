# -*- coding: utf-8 -*-
"""Setup module."""
from typing import List
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


def get_requires() -> List[str]:
    """Read requirements.txt."""
    requirements = open("requirements.txt", "r").read()
    return list(filter(lambda x: x != "", requirements.split()))


def read_description() -> str:
    """Read README.md and CHANGELOG.md."""
    try:
        with open("README.md") as r:
            description = "\n"
            description += r.read()
        with open("CHANGELOG.md") as c:
            description += "\n"
            description += c.read()
        return description
    except Exception:
        return '''IPSpot is a Python library for retrieving the current system's IP data and detailed location information such as region, longitude, and latitude.
        It supports both public and private IPv4 and IPv6 detection through multiple API providers, using a fallback mechanism for improved reliability.
        It has a simple and modular design, making it easy to perform fast IP, geolocation, provider, and regional lookups directly from your machine.'''


setup(
    name='ipspot',
    packages=['ipspot'],
    version='0.7',
    description='IPSpot: Retrieve Public & Private IPv4/IPv6 System Data',
    long_description=read_description(),
    long_description_content_type='text/markdown',
    include_package_data=True,
    author='IPSpot Development Team',
    author_email='ipspot@openscilab.com',
    url='https://github.com/openscilab/ipspot',
    download_url='https://github.com/openscilab/ipspot/tarball/v0.7',
    keywords="ip ipv4 geo geolocation network location ipspot cli",
    project_urls={
        'Source': 'https://github.com/openscilab/ipspot'
    },
    install_requires=get_requires(),
    python_requires='>=3.7',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Natural Language :: English',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Programming Language :: Python :: 3.13',
        'Programming Language :: Python :: 3.14',
        'Intended Audience :: Developers',
        'Intended Audience :: Education',
        'Intended Audience :: End Users/Desktop',
        'Topic :: System :: Monitoring',
        'Topic :: System :: Networking :: Monitoring',
        'Topic :: Utilities',
    ],
    license='MIT',
    entry_points={
            'console_scripts': [
                'ipspot = ipspot.cli:main',
            ]
    }
)
