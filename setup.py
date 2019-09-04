from os import path
from setuptools import setup, find_packages
import sys
import versioneer


# NOTE: This file must remain Python 2 compatible for the foreseeable future,
# to ensure that we error out properly for people with outdated setuptools
# and/or pip.
min_version = (3, 6)
if sys.version_info < min_version:
    error = """
catalogs does not support Python {0}.{1}.
Python {2}.{3} and above is required. Check your Python version like so:

python3 --version

This may be due to an out-of-date pip. Make sure you have pip >= 9.0.1.
Upgrade pip like so:

pip install --upgrade pip
""".format(*(sys.version_info[:2] + min_version))
    sys.exit(error)

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.rst'), encoding='utf-8') as readme_file:
    readme = readme_file.read()

with open(path.join(here, 'requirements.txt')) as requirements_file:
    # Parse requirements.txt, ignoring any commented-out lines.
    requirements = [line for line in requirements_file.read().splitlines()
                    if not line.startswith('#')]


setup(
    name='catalogs',
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    description="intake catalogs",
    long_description=readme,
    author="NSLS-II",
    author_email='gbischof@bnl.gov',
    url='https://github.com/gwbischof/catalogs',
    python_requires='>={}'.format('.'.join(str(n) for n in min_version)),
    packages=find_packages(exclude=['docs', 'tests']),
    entry_points={
        'console_scripts': [
            # 'command = some.module:some_function',
        ],
        'intake.catalogs': [
                            'SIX = catalogs.six:catalog',
                            'HXN = catalogs.hxn:catalog',
                            'ISR = catalogs.isr:catalog',
                            'SRX = catalogs.srx:catalog',
                            'BMM = catalogs.bmm:catalog',
                            'QAS = catalogs.qas:catalog',
                            'SST1 = catalogs.sst1:catalog',
                            'SST2 = catalogs.sst2:catalog',
                            'TES = catalogs.tes:catalog',
                            'ISS = catalogs.iss:catalog',
                            'IXS = catalogs.ixs:catalog',
                            'CMS = catalogs.cms:catalog',
                            'CHS = catalogs.chs:catalog',
                            'SMI = catalogs.smi:catalog',
                            'LIX = catalogs.lix:catalog',
                            'XFP = catalogs.xfp:catalog',
                            'AMX = catalogs.amx:catalog',
                            'FMX = catalogs.fmx:catalog',
                            'FXI = catalogs.fxi:catalog',
                            'NYX = catalogs.nyx:catalog',
                            'ESM = catalogs.esm:catalog',
                            'FIS = catalogs.fis:catalog',
                            'MET = catalogs.met:catalog',
                            'CSX = catalogs.csx:catalog',
                            'IOS = catalogs.ios:catalog',
                            'PDF = catalogs.pdf:catalog',
                            'XPD = catalogs.xpd:catalog',
                            'HEX = catalogs.hex:catalog'
        ]
    },
    include_package_data=True,
    package_data={
        'catalogs': [
            # When adding files here, remember to update MANIFEST.in as well,
            # or else they will not be included in the distribution on PyPI!
            # 'path/to/data_file',
        ]
    },
    install_requires=requirements,
    license="BSD (3-clause)",
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
    ],
)
