from .maps import Map

def test():
    thing = Map(1)
    print(thing.start_coord, type(thing.start_coord))
    print(thing.path)