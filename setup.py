#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages
import pandas
import numpy

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
    "pandas",
    "numpy"
    # TODO: put package requirements here
]

setup_requirements = [
    'pytest-runner'
    # TODO(BaileyGlen): put setup requirements (distutils extensions, etc.) here
]

test_requirements = [
    'pytest'
    # TODO: put package test requirements here
]

setup(
    name='genedb',
    version='0.1.0',
    description="Python Boilerplate contains all the boilerplate you need to create a Python package.",
    long_description=readme + '\n\n' + history,
    author="W. Bailey Glen Jr",
    author_email='glen@musc.edu',
    url='https://github.com/BaileyGlen/genedb',
    packages=find_packages(include=['genedb']),
    include_package_data=True,
    install_requires=requirements,
    license="MIT license",
    zip_safe=False,
    keywords='genedb',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    test_suite='tests',
    tests_require=test_requirements,
    setup_requires=setup_requirements,
)
