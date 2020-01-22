from databroker.v0 import Broker
from databroker.v1 import from_config
from .. import load_config

v0_catalog = Broker.from_config(load_config('qas/qas.yml'))
v1_catalog = from_config(load_config('qas/qas.yml'))
catalog = from_config(load_config('qas/qas.yml')).v2
