from typing import Callable

from pygame.draw import polygon
from pygame.math import Vector2
from pygame.surface import Surface

from game.enemy import BaseEnemy
from game.maps import Map
from game.utils.colours import RED

SIZE = 30
ROT_SPEED = 3

class NSided(BaseEnemy):
    def __init__(self, sides: int, curr_map: Map, 
                 default_callback: Callable[[BaseEnemy], None]):
        self.sides = sides
        
        super().__init__(curr_map, 3, default_callback)
        
        self.angle = 0
        
    def update(self):
        super().update()
        
        self.angle += ROT_SPEED
        
    def draw(self, screen: Surface):
        """Draw the enemy on the screen.

        Args:
            screen (Surface): The screen to draw on.
        """
        up_vec = Vector2((0, -SIZE)).rotate(self.angle)
        angle = 360 / self.sides
        
        points = [self.loc + up_vec]
        
        for i in range(1, self.sides):
            points.append(self.loc + up_vec.rotate(i * angle))
            
        polygon(screen, RED, points)