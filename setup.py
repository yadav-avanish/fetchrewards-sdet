#!/usr/bin/env python

from setuptools import setup, find_packages


setup(
    name="FetchRewards",
    version="1.0",
    description="FetchRewards testing",
    author="Avanish Kumar Yadav",
    author_email="<email_id>",
    # url="https://github.hpe.com/CSI-Automation/storage/wiki",
    platforms="any",
	classifiers=[
        "Development Status :: 3 - Alpha",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
		"Programming Language :: Python :: 3.7",
		"Programming Language :: Python :: 3.8",
        "Topic :: Software Development :: Testing"
    ],
    install_requires=[
        "pytest",
        "pytest-dependency",
		"selenium"
    ],
	packages=find_packages(exclude=("tests", "webdrivers"))
)