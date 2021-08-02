try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

import setuptools

setup(
    name="itertypes",
    version="1.3.1",
    author="Kreusada",
    author_email="kreusadaprojects@gmail.com",
    description="A small library used to obtain types for various builtin iterators.",
    long_description="A small library used to obtain types for various builtin iterators.",
    long_description_content_type="text/markdown",
    url="https://github.com/Kreusada/arrayfilters",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
    package_data={"": ["*.json", "*.rst", "*.txt", "*.yaml"]},
)
