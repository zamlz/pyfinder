#!/usr/bin/env python3

from setuptools import setup, find_packages

# Get __version__
with open('src/pyfinder/version.py') as f:
    exec(f.read())

# Get contents of markdown file
with open('README.md', 'r') as f:
    long_description = f.read()

setup(
    name='pyfinder',
    version=__version__,
    author='Amlesh Sivanantham',
    author_email='samlesh@gmail.com',
    maintainer='Amlesh Sivanantham',
    url='https://github.com/zamlz/pyfinder',
    description='Simple PathFinder Interactive Shell',
    long_description=long_description,
    long_description_content_type='text/markdown',
    package_dir={'': 'src'},
    packages=find_packages('src'),
    entry_points={
        'console_scripts': [
            'pyfinder=pyfinder.shell:start_shell'
        ]
    }
)
