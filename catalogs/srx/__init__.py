from databroker.v1 import from_config
from .. import load_config

v1_catalog = from_config(load_config('srx/srx.yml'))
catalog = from_config(load_config('srx/srx.yml')).v2
