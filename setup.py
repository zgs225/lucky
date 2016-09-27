# -*- coding: utf-8 -*-

import os
from setuptools import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "lucky",
    version = "0.0.1",
    author = "Yuez",
    author_email = "i@yuez.me",
    description = "A static site generator.",
    license = "BSD",
    keywords = "static site generator, blog generator",
    url = "https://github.com/zgs225/lucky",
    packages = ["lucky"],
    long_description = read("README.markdown"),
    classifiers = [
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: BSD License",
        "Programming Language :: Python :: 3"
    ],
    entry_points= {
        "console_scripts": [
            "lucky = lucky.cli:main"
        ]
    }
)
