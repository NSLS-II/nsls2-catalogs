from databroker.v1 import from_config
from databroker.v0 import Broker
from .. import load_config, load_config_central

name = 'amx'
v0_central = Broker.from_config(load_config_central(f'{name}/{name}.yml', name))
v1_central = from_config(load_config_central(f'{name}/{name}.yml', name))
central = from_config(load_config_central(f'{name}/{name}.yml', name)).v2