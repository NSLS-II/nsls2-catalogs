import entrypoints

def test_one_plus_one_is_two():
    for key, entry in entrypoints.get_group_named('intake.catalogs'):
        entry.load()
