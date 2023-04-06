from pygame.draw import rect
from pygame.mask import from_surface
from pygame.math import Vector2
from pygame.rect import Rect
from pygame.surface import Surface

from .colours import RED


class Sprite:
    """Custom sprite object to deal with locations and collisions.
    """
    def __init__(self, start_loc: Vector2):
        self.loc = start_loc
        
    def draw_box(self, screen: Surface, size: int=50):
        """Draws a box where the sprite is on the screen using the `loc` as a
        center point.

        Args:
            screen (Surface): Screen to draw the sprite to
            size (int, optional): Size of the box. Defaults to 50.
        """
   
        box = Rect(self.loc[0] - size//2, self.loc[1] - size//2, size, size)

        rect(screen, RED, box)