#!/usr/bin/env python
"""
Setup script
"""
import os
import sys

from distutils.core import setup

setup(
    name = 'testa',
    description = 'Module for testing fedwatch',
    version = '0.1',
    license = 'LGPLv2+',
    py_modules = ['testa'],
    entry_points={
        'console_scripts': [ 'testa = testa:run' ],
    },
    url = 'https://github.com/gregswift/testa',
    maintainer  = 'Greg Swift',
    maintainer_email = 'gregswift@gmail.com'
)
