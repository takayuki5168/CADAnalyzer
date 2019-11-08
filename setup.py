#!/usr/bin/env python

from setuptools import find_packages
from setuptools import setup

__version__ = '0.0.1'


setup(
    name='cad_analyzer',
    version=__version__,
    packages=find_packages(),
    description="cad analyzer",
    long_description=open('README.md').read(),
    author='Takayuki Murooka',
    author_email='takayuki5168@gmail.com',
    url='https://github.com/takayuki5168/CADAnalyzer',
    install_requires=open('requirements.txt').readlines(),
    license='MIT',
    keywords='utility'
)
