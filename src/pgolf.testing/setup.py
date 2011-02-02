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

name = 'pgolf.testing'
setup(
    name=name,
    namespace_packages=[                'pgolf', 'pgolf.testing',],  
    version=version,
    description='Project pgolf testing product',
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
        'zope.interface',
        'zope.component',
        #'plone.reload',
        'zope.testing',
        # -*- Extra requirements: -*-
    ],
    extras_require={'test': ['IPython', 'zope.testing', 'mocker']},
    entry_points="""
    # -*- Entry points: -*-
    """,
)
# vim:set ft=python:
