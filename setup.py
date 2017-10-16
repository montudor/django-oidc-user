import os
from setuptools import (
	find_packages,
	setup,
)

# Allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
	name = 'django-cross-project-accounts',
	packages = find_packages(),
	version = '0.0.1',
	description = 'Use a custom User model between projects easily.',
	author = 'Monte Hellawell',
	author_email = 'hellawell@monte.me.uk',
	url = 'https://github.com/montudor/django-cross-project-accounts',
	download_url = 'https://github.com/montudor/django-cross-project-accounts/archive/v0.0.1.tar.gz',
	keywords = ['testing', 'logging', 'example'],
	classifiers = [],
)