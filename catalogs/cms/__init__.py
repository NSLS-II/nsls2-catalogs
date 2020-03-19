from databroker.v1 import from_config
from databroker.v0 import Broker
from .. import load_config, load_config_central

name = 'cms'
v0_catalog = Broker.from_config(load_config(f'{name}/{name}.yml'))
v1_catalog = from_config(load_config(f'{name}/{name}.yml'))
catalog = from_config(load_config(f'{name}/{name}.yml')).v2
v0_central = Broker.from_config(load_config_central(f'{name}/{name}.yml', name))
v1_central = from_config(load_config_central(f'{name}/{name}.yml', name))
central = from_config(load_config_central(f'{name}/{name}.yml', name)).v2
