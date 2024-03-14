"""
from setuptools import setup, find_packages

setup(
    name='vimai',
    version='0.1',
    packages=find_packages(),
    license='MIT',
    description='A Python tool that executes Vim commands based on natural language input, which are applied on target file.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Pavel Larionov',
    author_email='p@1ar.io',
    url='https://github.com/pa1ar/vimai',
    install_requires=[
        'openai',
    ],
)
"""