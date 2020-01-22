import os
import yaml

from ._version import get_versions
__version__ = get_versions()['version']
del get_versions

v0_catalog = EntrypointsCatalog(entrypoints_group='catalogs.v0')
v1_catalog = EntrypointsCatalog(entrypoints_group='catalogs.v1'
catalog = EntrypointsCatalog(entrypoints_group='catalogs')

def load_config(filename):
    package_directory = os.path.dirname(os.path.abspath(__file__))
    filename = os.path.join(package_directory, filename)
    with open(filename) as f:
        return yaml.load(f, Loader=getattr(yaml, 'FullLoader', yaml.Loader))
