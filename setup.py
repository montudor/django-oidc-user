import os
from setuptools import (
    find_packages,
    setup,
)

# Allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

with open(os.path.join(os.path.abspath(os.path.dirname(__file__)), 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='django-oidc-user',
    packages=find_packages(),
    version='0.3.4',
    description='Creates an OpenID Connect compliant User model.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Monte Hellawell',
    author_email='monte@montudor.com',
    url='https://github.com/montudor/django-oidc-user',
    download_url='https://github.com/montudor/django-oidc-user/archive/v0.3.4.tar.gz',
    keywords=['django'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License"
    ],
)
