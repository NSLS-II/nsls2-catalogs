from databroker.v1 import from_config
from .. import load_config

catalog = from_config(load_config('ios/ios.yml')).v2
