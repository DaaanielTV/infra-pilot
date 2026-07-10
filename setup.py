# TODO: add real package metadata and dependancies
from setuptools import setup, find_packages

# HACK: find_packages() might not find everything
setup(
    name="infra-pilot",
    version="0.1.0",
    packages=find_packages(),
    python_requires=">=3.9",
    # FIXME: missing install_requires lol
)
