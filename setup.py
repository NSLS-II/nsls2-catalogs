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
                        'six = catalogs.six:catalog',
                        'hxn = catalogs.hxn:catalog',
                        'isr = catalogs.isr:catalog',
                        'srx = catalogs.srx:catalog',
                        'bmm = catalogs.bmm:catalog',
                        'qas = catalogs.qas:catalog',
                        'tes = catalogs.tes:catalog',
                        'iss = catalogs.iss:catalog',
                        'ixs = catalogs.ixs:catalog',
                        'cms = catalogs.cms:catalog',
                        'chx = catalogs.chx:catalog',
                        'smi = catalogs.smi:catalog',
                        'lix = catalogs.lix:catalog',
                        'xfp = catalogs.xfp:catalog',
                        'amx = catalogs.amx:catalog',
                        'fmx = catalogs.fmx:catalog',
                        'fxi = catalogs.fxi:catalog',
                        'esm = catalogs.esm:catalog',
                        'csx = catalogs.csx:catalog',
                        'ios = catalogs.ios:catalog',
                        'pdf = catalogs.pdf:catalog',
                        'xfm = catalogs.xfm:catalog',
                        'xpd = catalogs.xpd:catalog',
                        'xpdd = catalogs.xpdd:catalog',
                        'jpls = catalogs.jpls:catalog',
                        'rsoxs = catalogs.rsoxs:catalog'],
        'intake.catalogs': ['local = catalogs.local:v1_catalog',
                            'six = catalogs.six:v1_catalog',
                            'hxn = catalogs.hxn:v1_catalog',
                            'isr = catalogs.isr:v1_catalog',
                            'srx = catalogs.srx:v1_catalog',
                            'bmm = catalogs.bmm:v1_catalog',
                            'qas = catalogs.qas:v1_catalog',
                            'tes = catalogs.tes:v1_catalog',
                            'iss = catalogs.iss:v1_catalog',
                            'ixs = catalogs.ixs:v1_catalog',
                            'cms = catalogs.cms:v1_catalog',
                            'chx = catalogs.chx:v1_catalog',
                            'smi = catalogs.smi:v1_catalog',
                            'lix = catalogs.lix:v1_catalog',
                            'xfp = catalogs.xfp:v1_catalog',
                            'amx = catalogs.amx:v1_catalog',
                            'fmx = catalogs.fmx:v1_catalog',
                            'fxi = catalogs.fxi:v1_catalog',
                            'esm = catalogs.esm:v1_catalog',
                            'csx = catalogs.csx:v1_catalog',
                            'ios = catalogs.ios:v1_catalog',
                            'pdf = catalogs.pdf:v1_catalog',
                            'xfm = catalogs.xfm:v1_catalog',
                            'xpd = catalogs.xpd:v1_catalog',
                            'xpdd = catalogs.xpdd:v1_catalog',
                            'jpls = catalogs.jpls:v1_catalog',
                            'rsoxs = catalogs.rsoxs:v0_catalog'],
        'catalogs.v0': ['local = catalogs.local:v0_catalog',
                        'six = catalogs.six:v0_catalog',
                        'hxn = catalogs.hxn:v0_catalog',
                        'isr = catalogs.isr:v0_catalog',
                        'srx = catalogs.srx:v0_catalog',
                        'bmm = catalogs.bmm:v0_catalog',
                        'qas = catalogs.qas:v0_catalog',
                        'tes = catalogs.tes:v0_catalog',
                        'iss = catalogs.iss:v0_catalog',
                        'ixs = catalogs.ixs:v0_catalog',
                        'cms = catalogs.cms:v0_catalog',
                        'chx = catalogs.chx:v0_catalog',
                        'smi = catalogs.smi:v0_catalog',
                        'lix = catalogs.lix:v0_catalog',
                        'xfp = catalogs.xfp:v0_catalog',
                        'amx = catalogs.amx:v0_catalog',
                        'fmx = catalogs.fmx:v0_catalog',
                        'fxi = catalogs.fxi:v0_catalog',
                        'esm = catalogs.esm:v0_catalog',
                        'csx = catalogs.csx:v0_catalog',
                        'ios = catalogs.ios:v0_catalog',
                        'pdf = catalogs.pdf:v0_catalog',
                        'xfm = catalogs.xfm:v0_catalog',
                        'xpd = catalogs.xpd:v0_catalog',
                        'xpdd = catalogs.xpdd:v0_catalog',
                        'jpls = catalogs.jpls:v0_catalog',
                        'rsoxs = catalogs.rsoxs:v0_catalog'],
        'catalogs.central.v2': ['six = catalogs.six.central:central',
                                'hxn = catalogs.hxn.central:central',
                                'isr = catalogs.isr.central:central',
                                'srx = catalogs.srx.central:central',
                                'bmm = catalogs.bmm.central:central',
                                'qas = catalogs.qas.central:central',
                                'tes = catalogs.tes.central:central',
                                'iss = catalogs.iss.central:central',
                                'ixs = catalogs.ixs.central:central',
                                'cms = catalogs.cms.central:central',
                                'chx = catalogs.chx.central:central',
                                'smi = catalogs.smi.central:central',
                                'lix = catalogs.lix.central:central',
                                'xfp = catalogs.xfp.central:central',
                                'amx = catalogs.amx.central:central',
                                'fmx = catalogs.fmx.central:central',
                                'fxi = catalogs.fxi.central:central',
                                'esm = catalogs.esm.central:central',
                                'csx = catalogs.csx.central:central',
                                'ios = catalogs.ios.central:central',
                                'pdf = catalogs.pdf.central:central',
                                'xfm = catalogs.xfm.central:central',
                                'xpd = catalogs.xpd.central:central',
                                'xpdd = catalogs.xpdd.central:central',
                                'jpls = catalogs.jpls.central:central',
                                'rsoxs = catalogs.rsoxs.central:central'],
        'catalogs.central.v1': ['six = catalogs.six.central:v1_central',
                                'hxn = catalogs.hxn.central:v1_central',
                                'isr = catalogs.isr.central:v1_central',
                                'srx = catalogs.srx.central:v1_central',
                                'bmm = catalogs.bmm.central:v1_central',
                                'qas = catalogs.qas.central:v1_central',
                                'tes = catalogs.tes.central:v1_central',
                                'iss = catalogs.iss.central:v1_central',
                                'ixs = catalogs.ixs.central:v1_central',
                                'cms = catalogs.cms.central:v1_central',
                                'chx = catalogs.chx.central:v1_central',
                                'smi = catalogs.smi.central:v1_central',
                                'lix = catalogs.lix.central:v1_central',
                                'xfp = catalogs.xfp.central:v1_central',
                                'amx = catalogs.amx.central:v1_central',
                                'fmx = catalogs.fmx.central:v1_central',
                                'fxi = catalogs.fxi.central:v1_central',
                                'esm = catalogs.esm.central:v1_central',
                                'csx = catalogs.csx.central:v1_central',
                                'ios = catalogs.ios.central:v1_central',
                                'pdf = catalogs.pdf.central:v1_central',
                                'xfm = catalogs.xfm.central:v1_central',
                                'xpd = catalogs.xpd.central:v1_central',
                                'xpdd = catalogs.xpdd.central:v1_central',
                                'jpls = catalogs.jpls.central:v1_central',
                                'rsoxs = catalogs.rsoxs.central:v0_central'],
        'catalogs.central.v0': ['six = catalogs.six.central:v0_central',
                                'hxn = catalogs.hxn.central:v0_central',
                                'isr = catalogs.isr.central:v0_central',
                                'srx = catalogs.srx.central:v0_central',
                                'bmm = catalogs.bmm.central:v0_central',
                                'qas = catalogs.qas.central:v0_central',
                                'tes = catalogs.tes.central:v0_central',
                                'iss = catalogs.iss.central:v0_central',
                                'ixs = catalogs.ixs.central:v0_central',
                                'cms = catalogs.cms.central:v0_central',
                                'chx = catalogs.chx.central:v0_central',
                                'smi = catalogs.smi.central:v0_central',
                                'lix = catalogs.lix.central:v0_central',
                                'xfp = catalogs.xfp.central:v0_central',
                                'amx = catalogs.amx.central:v0_central',
                                'fmx = catalogs.fmx.central:v0_central',
                                'fxi = catalogs.fxi.central:v0_central',
                                'esm = catalogs.esm.central:v0_central',
                                'csx = catalogs.csx.central:v0_central',
                                'ios = catalogs.ios.central:v0_central',
                                'pdf = catalogs.pdf.central:v0_central',
                                'xfm = catalogs.xfm.central:v0_central',
                                'xpd = catalogs.xpd.central:v0_central',
                                'xpdd = catalogs.xpdd.central:v0_central',
                                'jpls = catalogs.jpls.central:v0_central']
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
