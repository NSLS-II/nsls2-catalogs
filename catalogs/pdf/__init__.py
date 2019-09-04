from databroker import Broker
from .. import load_config

catalog = Broker.from_config(load_config('pdf/pdf.yml'))
