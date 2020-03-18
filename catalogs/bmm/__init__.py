from databroker.v0 import Broker
from databroker.v1 import from_config
from .. import load_config

v0_catalog = Broker.from_config(load_config('bmm/bmm.yml'))
v1_catalog = from_config(load_config('bmm/bmm.yml'))
catalog = from_config(load_config('bmm/bmm.yml')).v2
v0_central = Broker.from_config(load_config_central('bmm/bmm.yml', 'BMM'))
v1_central = from_config(load_config_central('bmm/bmm.yml', 'BMM'))
central = from_config(load_config_central('bmm/bmm.yml', 'BMM')).v2
