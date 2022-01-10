# coding: utf-8
from setuptools import setup, find_packages  # noqa: H301

NAME = "edenai"
VERSION = "1.1.5"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = ["urllib3 >= 1.15", "six >= 1.10", "certifi", "python-dateutil"]

setup_requires=[
  'setuptools>=41.0.1',
  'wheel>=0.33.4']

setup(
    name=NAME,
    version=VERSION,
    description="Eden AI API Documentation",
    author_email="contact@edenai.co",
    keywords=["Swagger", "Eden AI API Documentation"],
    install_requires=REQUIRES,
    packages=find_packages(),
    include_package_data=True,
    long_description=open("README.md").read(),
    long_description_content_type='text/markdown',
    url="https://github.com/edenai/edenai-python/"
)
