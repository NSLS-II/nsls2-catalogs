from databroker.v1 import from_config
from databroker.v0 import Broker
from .. import load_config

v0_catalog = Broker.from_config(load_config('amx/amx.yml'))
v1_catalog = from_config(load_config('amx/amx.yml'))
catalog = from_config(load_config('amx/amx.yml')).v2
