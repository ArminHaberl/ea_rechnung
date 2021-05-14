# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in ea_rechnung/__init__.py
from ea_rechnung import __version__ as version

setup(
	name='ea_rechnung',
	version=version,
	description='Einnahmen-Ausgaben-Rechnung für Österreichische Kleinunternehmen',
	author='Armin Haberl',
	author_email='office@haberldesign.at',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
