# -*- coding: utf-8 -*-

import os
import setuptools

here = os.path.abspath(os.path.dirname(__file__))

requires = [
    'Scrapy>=2.1.0',
    'Flask>=1.1.2',
    'pyasn1'
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
)
