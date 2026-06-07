#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Setup script for ForestTale game.
"""

from setuptools import setup, find_packages

setup(
    name="ForestTale",
    version="1.0.0",
    author="В",
    author_email="your_email@example.com",
    description="Добрая консольная игра в стиле Undertale о выборе и сострадании",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/ваш_логин/ForestTale",
    packages=find_packages(),
    py_modules=["forest_tale"],
    entry_points={
        "console_scripts": [
            "foresttale = forest_tale:main",
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Environment :: Console",
        "Topic :: Games/Entertainment",
    ],
    python_requires=">=3.6",
    install_requires=[],   # только стандартная библиотека
)