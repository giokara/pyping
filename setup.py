#!/usr/bin/env python
# coding: utf-8

import os
import sys

try:
	from setuptools import setup
except ImportError:
	from distutils.core import setup

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    sys.exit()

setup(
	name='pyping3',
	version='0.0.1',
	description='A pure python ICMP ping implementation using raw sockets',
	long_description=open('README.rst').read() + '\n\n' +
                     open('HISTORY.rst').read(),
	license=open("LICENSE").read(),
	author="giokara",
	author_email="giokara.pyping@gmail.com",
	url='https://github.com/giokara/pyping/',
	keywords="ping icmp network latency",
	packages = ['pyping'],
	scripts=["bin/pyping"]
)
