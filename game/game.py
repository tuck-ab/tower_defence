from pygame.surface import Surface

from .enemy import BaseEnemy
from .maps import BaseMap

class Game:
    def __init__(self, level: int):
        self.map = BaseMap(level)
        
        self.enemy = BaseEnemy(self.map, 3, lambda x: None)
        
    def update(self):
        self.enemy.update()
        
    def draw_debug(self, screen: Surface):
        self.map.draw_path_line(screen)
        self.enemy.draw_box(screen)