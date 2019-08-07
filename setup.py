"""
Spyder coala plugin
======================
"""

# Standard library imports
import ast
import os

# Third party imports
from setuptools import find_packages, setup

HERE = os.path.abspath(os.path.dirname(__file__))


def get_version(module='spyder_coala'):
    """Get version."""
    with open(os.path.join(HERE, module, '_version.py'), 'r') as f:
        data = f.read()
    lines = data.split('\n')
    for line in lines:
        if line.startswith('VERSION_INFO'):
            version_tuple = ast.literal_eval(line.split('=')[-1].strip())
            version = '.'.join(map(str, version_tuple))
            break
    return version


REQUIREMENTS = ['spyder>=3.2.0',
                'qtpy', 'requests', 'psutil', 'nbformat']

setup(
    name='spyder-coala',
    version=get_version(),
    keywords='spyder coala linter',
    url='https://github.com/RohanVB/spyder-coala',
    license='MIT',
    author='RohanVB',
    description='coala integration with Spyder',
    long_description="This package allows coala "
                     "to run inside Spyder as a plugin.",
    packages=find_packages(exclude=['contrib', 'docs', 'tests*']),
    install_requires=REQUIREMENTS,
    include_package_data=True,
    classifiers=['Intended Audience :: Developers',
                 'License :: OSI Approved :: MIT License',
                 'Operating System :: OS Independent',
                 'Programming Language :: Python :: 3']
)