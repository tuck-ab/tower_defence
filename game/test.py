from .maps import BaseMap

def test():
    thing = BaseMap(1)
    print(thing.start_coord, type(thing.start_coord))
    print(thing.path)