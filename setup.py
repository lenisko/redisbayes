# -*- coding: utf-8 -*-
# this is not a love song
# http://packages.python.org/distribute/setuptools.html
# http://diveintopython3.org/packaging.html
# http://wiki.python.org/moin/CheeseShopTutorial
# http://pypi.python.org/pypi?:action=list_classifiers

from ez_setup import use_setuptools
use_setuptools(version="0.6c11")

import os
from setuptools import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name                 = "redisbayes",
    version              = __import__("redisbayes").__version__,
    description          = "Naïve Bayesian Text Classifier on Redis",
    long_description     = read("README.md"),
    author               = "Justine Tunney",
    author_email         = "jtunney@gmail.com",
    url                  = "https://github.com/jart/redisbayes",
    license              = "MIT",
    install_requires     = ["redis"],
    py_modules           = ["redisbayes", "ez_setup"],
    classifiers = [
        "Development Status :: 5 - Production/Stable",
        "License :: OSI Approved :: MIT License",
        "Intended Audience :: Developers",
        "Programming Language :: Python",
        "Topic :: Database",
        "Topic :: Communications :: Email",
    ],
)
