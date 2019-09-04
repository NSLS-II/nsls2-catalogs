from databroker import Broker
import yaml

def load_config(filename):
    with open(filename) as f:
        return yaml.load(f, Loader=getattr(yaml, 'FullLoader', yaml.Loader))

catalog = Broker.from_config(load_config('fxi.yml'))
