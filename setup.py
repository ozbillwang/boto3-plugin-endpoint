#!/usr/bin/env python
import sys
from setuptools import setup

requires = ['awscli>=1.11.0']

setup(
    name='boto3-plugin-endpoint',
    packages=['plugin_endpoint'],
    version='0.1',
    description='Endpoint plugin for python boto3 SDK',
    long_description=open('README.md').read(),
    author='Bill Wang & Wenbing Li',
    author_email='ozbillwang@gmail.com',
    url='https://github.com/ozbillwang/boto3-plugin-endpoint',
    keywords=['python', 'boto3', 'plugin', 'endpoint', 'endpoint_url', 'aws', 'aws sdk'],
    install_requires=requires,
    classifiers = []
)
