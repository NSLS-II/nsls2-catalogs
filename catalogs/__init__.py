import entrypoints
import os
import yaml

from databroker.discovery import EntrypointsCatalog
from ._version import get_versions

__version__ = get_versions()['version']
del get_versions


catalog_v0 = entrypoints.get_group_named('catalogs.v0')
catalog_v1 = entrypoints.get_group_named('intake.catalogs')
catalog = EntrypointsCatalog(entrypoints_group='catalogs.v2')
central_v0 = entrypoints.get_group_named('catalogs.central.v0')
central_v1 = entrypoints.get_group_named('catalogs.central.v1')
central = EntrypointsCatalog(entrypoints_group='catalogs.central.v2')


def load_config(filename):
    package_directory = os.path.dirname(os.path.abspath(__file__))
    filename = os.path.join(package_directory, filename)
    with open(filename) as f:
        return yaml.load(f, Loader=getattr(yaml, 'FullLoader', yaml.Loader))


def load_config_central(filename, beamline):
    config = load_config(filename)
    beamline_database = f"{beamline}-bluesky-documents"

    # Each beamline has its own account for the central mongo.
    username = beamline
    password = os.enviorn.get('{beamline}_mongo_password')s
    central_uri = (f'mongodb://{username}:{password}@mongo01.cs.nsls2.local:27212,'
                   'mongo02.cs.nsls2.local:27213,mongo03.cs.nsls2.local:27214')

    # Remove host and port, because we need to connect with a uri to the central database.
    config['metadatastore']['config'].pop('host', None)
    config['metadatastore']['config'].pop('port', None)
    config['assets']['config'].pop('host', None)
    config['assets']['config'].pop('port', None)

    # Add the uri, and update the database name.
    config['metadatastore']['config']['uri'] = central_uri
    config['metadatastore']['config']['database'] = beamline_database
    config['assets']['config']['uri'] = central_uri
    config['assets']['config']['database'] = beamline_database

    return config
