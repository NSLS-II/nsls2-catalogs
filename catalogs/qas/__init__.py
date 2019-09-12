from databroker.v1 import Broker
from .. import load_config

catalog = from_config(load_config('qas/qas.yml')).v2
