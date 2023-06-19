from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in topal_changes/__init__.py
from topal_changes import __version__ as version

setup(
	name="topal_changes",
	version=version,
	description="topal_changes",
	author="Shahzadnaser",
	author_email="shahzadnaser1122@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
