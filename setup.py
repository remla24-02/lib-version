from setuptools import setup, find_packages
from lib_version_remla24_team02 import VersionUtil, PACKAGE_NAME

setup(
    name=PACKAGE_NAME,
    version='{{VERSION}}',
    description="A version-aware library that can can be asked for the version of the library.",
    author="REMLA 2024 Team 02",
    author_email="example@example.com",
    url='https://github.com/remla24-02/lib-version',
    packages=find_packages()
)
