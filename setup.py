# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('README.md', encoding='utf-8') as f:
    readme = f.read()

with open('LICENSE', encoding='utf-8') as f:
    license = f.read()

setup(
    name='numbertotext',
    version='0.0.1',
    description='Convert a number to text',
    long_description=readme,
    author='Sylvain DANGIN',
    author_email='sylvain.dangin@gmail.com',
    url='https://github.com/Sylvaner/numbertotext',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)