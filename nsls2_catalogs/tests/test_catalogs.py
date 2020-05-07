import entrypoints
from databroker import Broker

def test_load_catalogs():
    # Loads all of the catalogs and checks that they are of type Broker.
    for key, entry in entrypoints.get_group_named('intake.catalogs').items():
        assert isinstance(entry.load(), Broker)
