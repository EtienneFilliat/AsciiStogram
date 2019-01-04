#!/usr/bin/env python

from setuptools import find_packages, setup

setup(
    name="AsciiStogram",
    version="0.1.2",
    author="Etienne FILLIAT",
    author_email="etienne.filliat@gmail.com",
    url="https://github.com/EtienneFilliat/AsciiStogram",
    packages=find_packages(),
    description="Histogram in terminal",
    keywords=['ascii', 'histogram', 'shell', 'plot'],
    classifiers=[
        'Environment :: Console',
        'Intended Audience :: End Users/Desktop',
        'Programming Language :: Python :: 3',
    ],
)
