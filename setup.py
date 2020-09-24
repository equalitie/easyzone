#!/usr/bin/env python3
#
# setup.py for easyzone3 package
#
# Copyright (c) 2015 trdcaz.
#
# Permission to use, copy, modify, and distribute this software and its
# documentation for any purpose with or without fee is hereby granted,
# provided that the above copyright notice and this permission notice
# appear in all copies.
#
# THE SOFTWARE IS PROVIDED "AS IS" AND NOMINUM DISCLAIMS ALL WARRANTIES
# WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
# MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL NOMINUM BE LIABLE FOR
# ANY SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGE
# WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
# ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT
# OF OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.

import os
import sys
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.txt')).read()

setup_args = dict(
    name = 'easyzone3',
    version = '1.2.3',
    description = 'Easy Zone - DNS Zone abstraction module',
    long_description = README,
    author = 'trdcaz',
    author_email = 'trdcaz@gmail.com',
    license='MIT',
    url = 'https://github.com/trdcaz/easyzone3/',
    packages = ['easyzone'],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "License :: OSI Approved :: MIT License",
        "Topic :: Internet :: Name Service (DNS)",
        "Topic :: System :: Systems Administration",
    ], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
    install_requires=["dnspython3",],
)

setup(**setup_args)
