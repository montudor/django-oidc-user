import os
from setuptools import (
	find_packages,
	setup,
)

# Allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
	name = 'django-oidc-user',
	packages = find_packages(),
	version = '0.3.0',
	description = 'Creates an OpenID Connect compliant User model.',
	author = 'Monte Hellawell',
	author_email = 'hellawell@monte.me.uk',
	url = 'https://github.com/montudor/django-oidc-user',
	download_url = 'https://github.com/montudor/django-oidc-user/archive/v0.3.0.tar.gz',
	keywords = ['django'],
	classifiers = [],
)