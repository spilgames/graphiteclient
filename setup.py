#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    sys.exit()

readme = open('README.md').read()
history = """ This is kinda new """
# open('HISTORY.rst').read().replace('.. :changelog:', '')

setup(
    name='graphiteclient',
    version='0.0.1',
    description='Graphite client library which fetches data from a graphite target',
    long_description=readme + '\n\n' + history,
    author='Jasper Capel, Thijs de Zoete',
    author_email='infrastructure@spilgames.com',
    url='https://github.com/spilgames/graphiteclient',
    packages=[
        'graphiteclient',
    ],
    package_dir={'graphiteclient': 'src'},
    include_package_data=True,
    install_requires=[
    ],
    license="BSD",
    zip_safe=False,
    keywords='graphite',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
    ],
    test_suite='tests',
)
