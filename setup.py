from setuptools import setup, find_packages
from os import path

DESCRIPTION = """ \
"""

setup(
    name='fenril',
    version='0.1.0',

    description='',
    long_description=DESCRIPTION,

    url='https://github.com/ixjlyons/fenril',

    author='Kenneth Lyons',
    author_email='ixjlyons@gmail.com',

    license='BSD',

    classifiers = [
        'Development Status :: 4 - Beta',
        'Environment :: X11 Applications :: Qt',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3'
    ],

    keywords='reference management bibtex vi vim',

    packages=find_packages(),

    install_requires=[
        'bibtexparser',
        'python-poppler-qt5'
    ],

    extras_require={},

    package_data={},

    entry_points={
        'gui_scripts': [
            'fenril=fenril.fenril:main'
         ],
    },
)
