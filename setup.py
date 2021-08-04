try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

import setuptools

with open("README.md", "r", encoding="utf-8") as fp:
    long_description = fp.read()

setup(
    name="itertypes",
    version="1.3.4",
    author="Kreusada",
    author_email="kreusadaprojects@gmail.com",
    description="A small library used to obtain types for various builtin iterators.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Kreusada/itertypes",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_data={"": ["*.json", "*.rst", "*.txt", "*.yaml"]},
)
