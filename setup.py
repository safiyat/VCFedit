#!/usr/bin/env python

from setuptools import setup

with open('requirements.txt') as f:
    required = f.read().splitlines()

setup(name='VCFEdit',
      version='0.1',
      description='vCard file editor',
      author='Md Safiyat Reza',
      author_email='reza.safiyat@acm.org',
      url='https://github.com/safiyat/VCFEdit',
      packages=['vcfedit'],
      install_requires=required,
      entry_points = {
        'console_scripts' : [
             'vcfedit = vcfedit.app:main'
           ]
      }
     )
