# -*- coding: utf-8 -*-

import os
import setuptools
from setuptools.command.test import test as TestCommand
import sys

here = os.path.abspath(os.path.dirname(__file__))


class PyTest(TestCommand):
    user_options = [('pytest-args=', 'a', "Arguments to pass to py.test")]

    def initialize_options(self):
        TestCommand.initialize_options(self)
        self.pytest_args = []

    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        import pytest
        errno = pytest.main(self.pytest_args)
        sys.exit(errno)


requires = [
    'Scrapy>=2.1.0',
    'Flask>=1.1.2',
    'pyasn1',
    'crochet',
]

about = {}
with open(os.path.join(here, 'onefeed', '__version__.py'), 'r') as f:
    exec(f.read(), about)

with open("README.md", "r") as fh:
    readme = fh.read()

setuptools.setup(
    name=about['__title__'],
    version=about['__version__'],
    description=about['__description__'],
    long_description=readme,
    long_description_content_type='text/markdown',
    author=about['__author__'],
    author_email=about['__author_email__'],
    url=about['__url__'],
    license=about['__license__'],
    packages=setuptools.find_packages(),
    include_package_data=True,
    package_data={
        "": ["*.html"],
    },
    entry_points='''
            [console_scripts]
            onefeed=onefeed.cmdline:cli
        ''',
    classifiers=[
        "Programming Language :: Python :: 3.6",
        'Programming Language :: Python :: 3.7',
        'License :: OSI Approved :: Apache Software License',
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=requires,
    tests_require=['pytest'],
    cmdclass={'test': PyTest},
)
