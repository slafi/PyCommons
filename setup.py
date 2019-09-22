from setuptools import setup

with open("README.md", 'r') as f:
    long_description = f.read()

setup(
   name='PyCommons',
   version='0.1',
   description='A module which gathers helper functions that can be used in different Python projects',
   author='Sabeur Lafi',
   author_email='lafi.saber@gmail.com',
   url="https://github.com/slafi",
   license="MIT",
   long_description=long_description,
   packages=['PyCommons'],
)