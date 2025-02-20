#!/usr/bin/env python

from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="py-solc-ast",
    version="1.2.8",
    description="A tool for exploring the abstract syntax tree generated by solc.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Ben Hauser",
    author_email="ben@hauser.id",
    url="https://github.com/iamdefinitelyahuman/py-solc-ast",
    include_package_data=True,
    py_modules=["solcast"],
    setup_requires=[],
    python_requires=">=3.6, <4",
    install_requires=[],
    license="MIT",
    zip_safe=False,
    keywords=["ethereum", "solidity", "solc", "ast"],
    packages=find_packages(exclude=["tests", "tests.*"]),
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
)
