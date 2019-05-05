# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='sample',
    version='0.1.0',
    description='NBA Play by Play with Vector',
    long_description=readme,
    author='Randy Forbes',
    author_email='randy.forbes@gmail.com',
    url='https://github.com/rforbes/vector-nba',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)

