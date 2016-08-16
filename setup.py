#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" Setup script for sw_delta """
from setuptools import setup, find_packages

setup(
    name='sw_delta',
    version='0.0.1',
    url='https://github.com/alexcasalboni/sw-delta-python',
    packages=find_packages(),
    scripts=['manage.py'],
    install_requires=[
        'diff-match-patch-python',
    ],
)
