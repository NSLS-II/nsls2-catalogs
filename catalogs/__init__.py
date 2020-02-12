import entrypoints
import os
import yaml

from databroker.discovery import EntrypointsCatalog
from ._version import get_versions

__version__ = get_versions()['version']
del get_versions


v0_catalog = entrypoints.get_group_named('catalogs.v0')
v1_catalog = entrypoints.get_group_named('catalogs.v1')
catalog = EntrypointsCatalog(entrypoints_group='intake.catalogs')


def load_config(filename):
    package_directory = os.path.dirname(os.path.abspath(__file__))
    filename = os.path.join(package_directory, filename)
    with open(filename) as f:
        return yaml.load(f, Loader=getattr(yaml, 'FullLoader', yaml.Loader))
