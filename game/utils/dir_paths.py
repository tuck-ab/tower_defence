import pathlib
import os

MODULE_DIR = pathlib.Path(__file__).parent.parent
MAPS_DIR = os.path.join(MODULE_DIR, "maps", "levels")
LEVELS_DIR = os.path.join(MODULE_DIR, "spawner", "levels")