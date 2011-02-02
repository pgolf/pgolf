import os, sys

from setuptools import setup, find_packages

version = u'1.0'

def read(*rnames):
    return open(
        os.path.join('.', *rnames)
    ).read()

long_description = "\n\n".join(
    [read('README.txt'),
     read('docs', 'INSTALL.txt'),
     read('docs', 'HISTORY.txt'),
    ]
)

classifiers = [
    "Programming Language :: Python",
    "Topic :: Software Development",]

name = 'pgolf.skin'
setup(
    name=name,
    namespace_packages=[                'pgolf', 'pgolf.skin',],  
    version=version,
    description='Project pgolf skin product',
    long_description=long_description,
    classifiers=classifiers,
    keywords='',
    author='mpa <mpa@makina-corpus.com>',
    author_email='mpa@makina-corpus.com',
    url='http://pypi.python.org/pypi/%s' % name,
    license='GPL',
    packages=find_packages('src'),
    package_dir = {'': 'src'},
    include_package_data=True,
    install_requires=[
        'setuptools',
        # -*- Extra requirements: -*-
    ],
    entry_points="""
    # -*- Entry points: -*-
    """,
)
# vim:set ft=python:
