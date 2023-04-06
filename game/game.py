from pygame.surface import Surface

from .enemy import BaseEnemy
from .maps import BaseMap

class Game:
    def __init__(self, level: int):
        self.map = BaseMap(level)
        
        self.tick = 0
        self.running = True
        def enemy_callback(enemy):
            self.running = False
        
        self.enemy = BaseEnemy(self.map, 3, enemy_callback)
        
    def update(self):
        """Update the game this main loop itteration"""
        self.enemy.update()
        
    def draw_debug(self, screen: Surface):
        """Draw a skeleton of what is on the screen"""
        self.map.draw_path_line(screen)
        self.enemy.draw_box(screen)