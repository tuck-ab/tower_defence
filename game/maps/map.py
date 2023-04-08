from importlib import import_module
from typing import List, Tuple

from pygame.draw import line
from pygame.math import Vector2
from pygame.surface import Surface

from game.utils.colours import WHITE

DIRECTION_UP = Vector2([0, -1])
DIRECTION_DOWN = Vector2([0, 1])
DIRECTION_LEFT = Vector2([-1, 0])
DIRECTION_RIGHT = Vector2([1, 0])

DIRECTIONS = [DIRECTION_UP, DIRECTION_RIGHT, DIRECTION_DOWN, DIRECTION_LEFT]

class Map:
    def __init__(self, level: int):        
        self.path, self.start_coord = self.load(level)
        
    def load(self, level: int) -> Tuple[List[Vector2], Vector2]:
        """Loads a level.

        Args:
            level (int): The level to load.

        Returns:
            Tuple[List[np.ndarray], np.ndarray]: Tuple returning the path the enemies take and 
            the coordinate the enemies start from.
        """
        level_module = import_module(f"game.maps.levels.level{level}")
        path = []
        for direction, num in level_module.path:
            for _ in range(0, num):
                path.append(direction)
                
        
        return path, Vector2(level_module.start_coord)
    
    def draw_path_line(self, screen: Surface):
        """Draws a basic skeleton of the map's path.

        Args:
            screen (Surface): The surface to draw the path on.
        """
        curr_coord = self.start_coord.copy()
        
        for step in self.path:
            end_step = curr_coord + step
            
            line(screen, WHITE, curr_coord, end_step, width=10)
            
            curr_coord = end_step
    