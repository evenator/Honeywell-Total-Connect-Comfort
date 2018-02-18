#!/usr/bin/env python

from setuptools import setup

setup(name='Honeywell Total Connect Comfort',
      version='0.0.2',
      description='Tools to enhance the Honeywell Total Connect Comfort thermostat',
      author='Ed Venator',
      author_email='evenator@gmail.com',
      url='https://github.com/evenator/Honeywell-Total-Connect-Comfort',
      scripts=['honeywell_cli'],
      packages=['honeywell_total_connect_comfort'],
      install_requires=[
          'lxml',
          'requests',
          'SQLAlchemy',
      ],
)
