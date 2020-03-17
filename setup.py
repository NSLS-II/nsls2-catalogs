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
        'catalogs.v2': ['local = catalogs.local:catalog',
                            'SIX = catalogs.six:catalog',
                            'HXN = catalogs.hxn:catalog',
                            'ISR = catalogs.isr:catalog',
                            'SRX = catalogs.srx:catalog',
                            'BMM = catalogs.bmm:catalog',
                            'QAS = catalogs.qas:catalog',
                            'TES = catalogs.tes:catalog',
                            'ISS = catalogs.iss:catalog',
                            'IXS = catalogs.ixs:catalog',
                            'CMS = catalogs.cms:catalog',
                            'CHX = catalogs.chx:catalog',
                            'SMI = catalogs.smi:catalog',
                            'LIX = catalogs.lix:catalog',
                            'XFP = catalogs.xfp:catalog',
                            'AMX = catalogs.amx:catalog',
                            'FMX = catalogs.fmx:catalog',
                            'FXI = catalogs.fxi:catalog',
                            'ESM = catalogs.esm:catalog',
                            'CSX = catalogs.csx:catalog',
                            'IOS = catalogs.ios:catalog',
                            'PDF = catalogs.pdf:catalog',
                            'XFM = catalogs.xfm:catalog',
                            'XPD = catalogs.xpd:catalog',
                            'XPDD = catalogs.xpdd:catalog',
                            'JPLS = catalogs.jpls:catalog',
                            'RSOXS = catalogs.rsoxs:catalog'],
        'catalogs.v1': [    'local = catalogs.local:v1_catalog',
                            'SIX = catalogs.six:v1_catalog',
                            'HXN = catalogs.hxn:v1_catalog',
                            'ISR = catalogs.isr:v1_catalog',
                            'SRX = catalogs.srx:v1_catalog',
                            'BMM = catalogs.bmm:v1_catalog',
                            'QAS = catalogs.qas:v1_catalog',
                            'TES = catalogs.tes:v1_catalog',
                            'ISS = catalogs.iss:v1_catalog',
                            'IXS = catalogs.ixs:v1_catalog',
                            'CMS = catalogs.cms:v1_catalog',
                            'CHX = catalogs.chx:v1_catalog',
                            'SMI = catalogs.smi:v1_catalog',
                            'LIX = catalogs.lix:v1_catalog',
                            'XFP = catalogs.xfp:v1_catalog',
                            'AMX = catalogs.amx:v1_catalog',
                            'FMX = catalogs.fmx:v1_catalog',
                            'FXI = catalogs.fxi:v1_catalog',
                            'ESM = catalogs.esm:v1_catalog',
                            'CSX = catalogs.csx:v1_catalog',
                            'IOS = catalogs.ios:v1_catalog',
                            'PDF = catalogs.pdf:v1_catalog',
                            'XFM = catalogs.xfm:v1_catalog',
                            'XPD = catalogs.xpd:v1_catalog',
                            'XPDD = catalogs.xpdd:v1_catalog',
                            'JPLS = catalogs.jpls:v1_catalog',
                            'RSOXS = catalogs.rsoxs:v0_catalog'],
        'catalogs.v0': [    'local = catalogs.local:v0_catalog',
                            'SIX = catalogs.six:v0_catalog',
                            'HXN = catalogs.hxn:v0_catalog',
                            'ISR = catalogs.isr:v0_catalog',
                            'SRX = catalogs.srx:v0_catalog',
                            'BMM = catalogs.bmm:v0_catalog',
                            'QAS = catalogs.qas:v0_catalog',
                            'TES = catalogs.tes:v0_catalog',
                            'ISS = catalogs.iss:v0_catalog',
                            'IXS = catalogs.ixs:v0_catalog',
                            'CMS = catalogs.cms:v0_catalog',
                            'CHX = catalogs.chx:v0_catalog',
                            'SMI = catalogs.smi:v0_catalog',
                            'LIX = catalogs.lix:v0_catalog',
                            'XFP = catalogs.xfp:v0_catalog',
                            'AMX = catalogs.amx:v0_catalog',
                            'FMX = catalogs.fmx:v0_catalog',
                            'FXI = catalogs.fxi:v0_catalog',
                            'ESM = catalogs.esm:v0_catalog',
                            'CSX = catalogs.csx:v0_catalog',
                            'IOS = catalogs.ios:v0_catalog',
                            'PDF = catalogs.pdf:v0_catalog',
                            'XFM = catalogs.xfm:v0_catalog',
                            'XPD = catalogs.xpd:v0_catalog',
                            'XPDD = catalogs.xpdd:v0_catalog',
                            'JPLS = catalogs.jpls:v0_catalog',
                            'RSOXS = catalogs.rsoxs:v0_catalog']
        'catalogs.central.v2': ['local = catalogs.local:central',
                                'SIX = catalogs.six:central',
                                'HXN = catalogs.hxn:central',
                                'ISR = catalogs.isr:central',
                                'SRX = catalogs.srx:central',
                                'BMM = catalogs.bmm:central',
                                'QAS = catalogs.qas:central',
                                'TES = catalogs.tes:central',
                                'ISS = catalogs.iss:central',
                                'IXS = catalogs.ixs:central',
                                'CMS = catalogs.cms:central',
                                'CHX = catalogs.chx:central',
                                'SMI = catalogs.smi:central',
                                'LIX = catalogs.lix:central',
                                'XFP = catalogs.xfp:central',
                                'AMX = catalogs.amx:central',
                                'FMX = catalogs.fmx:central',
                                'FXI = catalogs.fxi:central',
                                'ESM = catalogs.esm:central',
                                'CSX = catalogs.csx:central',
                                'IOS = catalogs.ios:central',
                                'PDF = catalogs.pdf:central',
                                'XFM = catalogs.xfm:central',
                                'XPD = catalogs.xpd:central',
                                'XPDD = catalogs.xpdd:central',
                                'JPLS = catalogs.jpls:central',
                                'RSOXS = catalogs.rsoxs:central'],
        'catalogs.central.v1': ['local = catalogs.local:v1_central',
                                'SIX = catalogs.six:v1_central',
                                'HXN = catalogs.hxn:v1_central',
                                'ISR = catalogs.isr:v1_central',
                                'SRX = catalogs.srx:v1_central',
                                'BMM = catalogs.bmm:v1_central',
                                'QAS = catalogs.qas:v1_central',
                                'TES = catalogs.tes:v1_central',
                                'ISS = catalogs.iss:v1_central',
                                'IXS = catalogs.ixs:v1_central',
                                'CMS = catalogs.cms:v1_central',
                                'CHX = catalogs.chx:v1_central',
                                'SMI = catalogs.smi:v1_central',
                                'LIX = catalogs.lix:v1_central',
                                'XFP = catalogs.xfp:v1_central',
                                'AMX = catalogs.amx:v1_central',
                                'FMX = catalogs.fmx:v1_central',
                                'FXI = catalogs.fxi:v1_central',
                                'ESM = catalogs.esm:v1_central',
                                'CSX = catalogs.csx:v1_central',
                                'IOS = catalogs.ios:v1_central',
                                'PDF = catalogs.pdf:v1_central',
                                'XFM = catalogs.xfm:v1_central',
                                'XPD = catalogs.xpd:v1_central',
                                'XPDD = catalogs.xpdd:v1_central',
                                'JPLS = catalogs.jpls:v1_central',
                                'RSOXS = catalogs.rsoxs:v0_central'],
        'catalogs.central.v0': ['local = catalogs.local:v0_central',
                                'SIX = catalogs.six:v0_central',
                                'HXN = catalogs.hxn:v0_central',
                                'ISR = catalogs.isr:v0_central',
                                'SRX = catalogs.srx:v0_central',
                                'BMM = catalogs.bmm:v0_central',
                                'QAS = catalogs.qas:v0_central',
                                'TES = catalogs.tes:v0_central',
                                'ISS = catalogs.iss:v0_central',
                                'IXS = catalogs.ixs:v0_central',
                                'CMS = catalogs.cms:v0_central',
                                'CHX = catalogs.chx:v0_central',
                                'SMI = catalogs.smi:v0_central',
                                'LIX = catalogs.lix:v0_central',
                                'XFP = catalogs.xfp:v0_central',
                                'AMX = catalogs.amx:v0_central',
                                'FMX = catalogs.fmx:v0_central',
                                'FXI = catalogs.fxi:v0_central',
                                'ESM = catalogs.esm:v0_central',
                                'CSX = catalogs.csx:v0_central',
                                'IOS = catalogs.ios:v0_central',
                                'PDF = catalogs.pdf:v0_central',
                                'XFM = catalogs.xfm:v0_central',
                                'XPD = catalogs.xpd:v0_central',
                                'XPDD = catalogs.xpdd:v0_central',
                                'JPLS = catalogs.jpls:v0_central']
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
