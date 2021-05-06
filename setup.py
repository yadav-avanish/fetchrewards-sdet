#!/usr/bin/env python

from setuptools import setup, find_packages


setup(
    name="FetchRewards",
    version="1.0",
    description="Excercise for SDET role at FetchRewards",
    author="Avanish Yadav",
    platforms="any",

    install_requires=[
        "pytest",
        "pytest-dependency",
		"selenium"
    ],
	packages=find_packages(exclude=("tests", "webdrivers"))
)