#!/usr/bin/env python3
"""
Integer Conversion Utility
==========================

Int is a simple command line utility for converting integers between bases. It accepts an integer in its [b]inary, [o]ctal, [d]ecimal, or he[x]adecimal form, then prints it out in all four bases::

    $ int 64
    hex: 40
    dec: 64
    oct: 100
    bin: 01000000

You can specify the base of the input using a single letter prefix.
(Defaults to decimal if omitted.) Int also accepts multiple arguments::

    $ int b1001 o777 d256 x1EA

Leading zeros are ignored so integer literals in the form `0x123` are
also accepted.

"""

import os
import re
import io

from setuptools import setup


filepath = os.path.join(os.path.dirname(__file__), 'int.py')
with io.open(filepath, encoding='utf-8') as metafile:
    regex = r'''^__([a-z]+)__ = ["'](.*)["']'''
    meta = dict(re.findall(regex, metafile.read(), flags=re.MULTILINE))


setup(
    name = 'int',
    version = meta['version'],
    py_modules = ['int'],
    entry_points = {
        'console_scripts': [
            'int = int:main',
        ],
    },
    author = 'Darren Mulholland',
    url = 'https://github.com/dmulholl/int',
    license = 'Public Domain',
    description = (
        'Integer conversion utility.'
    ),
    long_description = __doc__,
    classifiers = [
        'Development Status :: 5 - Production/Stable',
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
        'License :: Public Domain',
        'Topic :: Utilities',
    ],
)
