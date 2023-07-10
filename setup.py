# -*- coding: utf-8 -*-
# Copyright IRT Antoine de Saint Exupéry et Université Paul Sabatier Toulouse III - All
# rights reserved. DEEL is a research program operated by IVADO, IRT Saint Exupéry,
# CRIAQ and ANITI - https://www.deel.ai/
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
# -*- encoding: utf-8 -*-
from os import path

from setuptools import find_namespace_packages
from setuptools import setup

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

requirements = [
    "numpy"
]

dev_requirements = [
    "tox",
    "black",
    "flake8",
    "flake8-black",
    "pylint",
    "pytest"
]

docs_requirements = [
    "mkdocs",
    "mkdocs-material",
    "mkdocstrings",
    # only if you want to generate notebooks in documentation website
    "mknotebooks",
    "ipython",
]

setup(
    # Name of the package:
    name="lib-name",
    # Version of the package:
    version="0.0.4",
    # Find the package automatically (include everything):
    packages=find_namespace_packages(include=["deel.*"]),
    # Author information:
    author="DEEL",
    author_email="collaborateurs.du.projet.deel@irt-saintexupery.com",
    # Description of the package:
    description="Short description",
    long_description=long_description,
    long_description_content_type="text/markdown",
    # Plugins entry point
    
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
    ],
    
    install_requires=requirements,
    
    extras_require={
        "dev": dev_requirements, 
        "docs": docs_requirements,
    },

)
