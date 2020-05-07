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
nsls2-catalogs does not support Python {0}.{1}.
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
    name='nsls2-catalogs',
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    description="databroker catalogs",
    long_description=readme,
    author="NSLS-II",
    author_email='gbischof@bnl.gov',
    url='https://github.com/NSLS-II/nsls2-catalogs',
    python_requires='>={}'.format('.'.join(str(n) for n in min_version)),
    packages=find_packages(exclude=['docs', 'tests']),
    entry_points={
        'console_scripts': [
            # 'command = some.module:some_function',
        ],
        'intake.catalogs': ['six = nsls2_catalogs.six.central:central',
                                'hxn = nsls2_catalogs.hxn.central:central',
                                'isr = nsls2_catalogs.isr.central:central',
                                'srx = nsls2_catalogs.srx.central:central',
                                'bmm = nsls2_catalogs.bmm.central:central',
                                'qas = nsls2_catalogs.qas.central:central',
                                'tes = nsls2_catalogs.tes.central:central',
                                'iss = nsls2_catalogs.iss.central:central',
                                'ixs = nsls2_catalogs.ixs.central:central',
                                'cms = nsls2_catalogs.cms.central:central',
                                'chx = nsls2_catalogs.chx.central:central',
                                'smi = nsls2_catalogs.smi.central:central',
                                'lix = nsls2_catalogs.lix.central:central',
                                'xfp = nsls2_catalogs.xfp.central:central',
                                'amx = nsls2_catalogs.amx.central:central',
                                'fmx = nsls2_catalogs.fmx.central:central',
                                'fxi = nsls2_catalogs.fxi.central:central',
                                'esm = nsls2_catalogs.esm.central:central',
                                'csx = nsls2_catalogs.csx.central:central',
                                'ios = nsls2_catalogs.ios.central:central',
                                'pdf = nsls2_catalogs.pdf.central:central',
                                'xfm = nsls2_catalogs.xfm.central:central',
                                'xpd = nsls2_catalogs.xpd.central:central',
                                'xpdd = nsls2_catalogs.xpdd.central:central',
                                'jpls = nsls2_catalogs.jpls.central:central',
                                'rsoxs = nsls2_catalogs.rsoxs.central:central'],
        'catalogs.v1': ['six = nsls2_catalogs.six.central:v1_central',
                                'hxn = nsls2_catalogs.hxn.central:v1_central',
                                'isr = nsls2_catalogs.isr.central:v1_central',
                                'srx = nsls2_catalogs.srx.central:v1_central',
                                'bmm = nsls2_catalogs.bmm.central:v1_central',
                                'qas = nsls2_catalogs.qas.central:v1_central',
                                'tes = nsls2_catalogs.tes.central:v1_central',
                                'iss = nsls2_catalogs.iss.central:v1_central',
                                'ixs = nsls2_catalogs.ixs.central:v1_central',
                                'cms = nsls2_catalogs.cms.central:v1_central',
                                'chx = nsls2_catalogs.chx.central:v1_central',
                                'smi = nsls2_catalogs.smi.central:v1_central',
                                'lix = nsls2_catalogs.lix.central:v1_central',
                                'xfp = nsls2_catalogs.xfp.central:v1_central',
                                'amx = nsls2_catalogs.amx.central:v1_central',
                                'fmx = nsls2_catalogs.fmx.central:v1_central',
                                'fxi = nsls2_catalogs.fxi.central:v1_central',
                                'esm = nsls2_catalogs.esm.central:v1_central',
                                'csx = nsls2_catalogs.csx.central:v1_central',
                                'ios = nsls2_catalogs.ios.central:v1_central',
                                'pdf = nsls2_catalogs.pdf.central:v1_central',
                                'xfm = nsls2_catalogs.xfm.central:v1_central',
                                'xpd = nsls2_catalogs.xpd.central:v1_central',
                                'xpdd = nsls2_catalogs.xpdd.central:v1_central',
                                'jpls = nsls2_catalogs.jpls.central:v1_central',
                                'rsoxs = nsls2_catalogs.rsoxs.central:v1_central'],
        'catalogs.v0': ['six = nsls2_catalogs.six.central:v0_central',
                                'hxn = nsls2_catalogs.hxn.central:v0_central',
                                'isr = nsls2_catalogs.isr.central:v0_central',
                                'srx = nsls2_catalogs.srx.central:v0_central',
                                'bmm = nsls2_catalogs.bmm.central:v0_central',
                                'qas = nsls2_catalogs.qas.central:v0_central',
                                'tes = nsls2_catalogs.tes.central:v0_central',
                                'iss = nsls2_catalogs.iss.central:v0_central',
                                'ixs = nsls2_catalogs.ixs.central:v0_central',
                                'cms = nsls2_catalogs.cms.central:v0_central',
                                'chx = nsls2_catalogs.chx.central:v0_central',
                                'smi = nsls2_catalogs.smi.central:v0_central',
                                'lix = nsls2_catalogs.lix.central:v0_central',
                                'xfp = nsls2_catalogs.xfp.central:v0_central',
                                'amx = nsls2_catalogs.amx.central:v0_central',
                                'fmx = nsls2_catalogs.fmx.central:v0_central',
                                'fxi = nsls2_catalogs.fxi.central:v0_central',
                                'esm = nsls2_catalogs.esm.central:v0_central',
                                'csx = nsls2_catalogs.csx.central:v0_central',
                                'ios = nsls2_catalogs.ios.central:v0_central',
                                'pdf = nsls2_catalogs.pdf.central:v0_central',
                                'xfm = nsls2_catalogs.xfm.central:v0_central',
                                'xpd = nsls2_catalogs.xpd.central:v0_central',
                                'xpdd = nsls2_catalogs.xpdd.central:v0_central',
                                'jpls = nsls2_catalogs.jpls.central:v0_central',
                                'rsoxs = nsls2_catalogs.rsoxs.central:v0_central'],
        },
    include_package_data=True,
    package_data={
        'nsls2-catalogs': [
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
