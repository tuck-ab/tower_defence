from pygame.math import Vector2
from pygame.draw import line, circle

from game.utils.directions import UP, off_screen
from game.utils.colours import DEBUG


class BaseProjectile:
    def __init__(self, loc: Vector2, vel: Vector2):
        self.loc = loc
        self.vel = vel
        
        self.angle = UP.angle_to(self.vel)
        
    def update(self):
        self.loc += self.vel
        
        if off_screen(self.loc):
            self.off_screen_callback(self)
        
    def draw_box(self, screen):
        line(screen, DEBUG, self.loc, self.loc + self.vel*10)
        circle(screen, DEBUG, self.loc, 5)
