"""
shortly

A URL shortener.
"""
from setuptools import setup, find_packages


setup(
    name='shortly',
    version='0.1',
    long_description=__doc__,
    packages=find_packages(), # packages=['application'],
    include_package_data=True, # look for a MANIFEST.in file
    zip_safe=False,
    install_requires=[
        'Flask==0.10.1',
        'redis==2.8.0'
    ]
)

# $> python setup.py install
# $> python setup.py develop
# develop just installing a link to the site-packages folder
