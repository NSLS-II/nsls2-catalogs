from databroker.v0 import Broker
from databroker.v1 import from_config
from .. import load_config

v0_catalog = Broker.from_config(load_config('six/six.yml'))
v1_catalog = from_config(load_config('six/six.yml'))
catalog = from_config(load_config('six/six.yml')).v2
