from __future__ import annotations

from typing import Callable

from pygame.draw import rect
from pygame.rect import Rect
from pygame.surface import Surface

from game.maps import Map
from game.utils.colours import RED
from game.utils.sprite import Sprite


class BaseEnemy(Sprite):
    """Default class for an enemy. This can be inherited by other classes
    to create more enemies of different types
    """
    def __init__(self, curr_map: Map, speed: int,
                 at_goal_callback: Callable[[BaseEnemy], None]):
        super().__init__(curr_map.start_coord.copy())
        
        self.map = curr_map
        self.map_step = 0
        
        self.speed = speed
        
        self.at_goal = False
        self.at_goal_callback = at_goal_callback
        
    def update(self):
        """Update function to be run once every iteration of the main loop. Starts by
        updating the position of the enemy using the map path. If the enemy gets to
        the end of the path then it calls the `at_goal_callback` callback passed during 
        the construction of the object.
        """
        for _ in range(0, self.speed):
            if self.map_step < len(self.map.path):
                self.loc += self.map.path[self.map_step]
            else:
                self.at_goal = True
                break
            
            self.map_step += 1
            
        if self.at_goal:
            self.at_goal_callback(self)
