from typing import List

from pygame.math import Vector2
from pygame.surface import Surface

from game.enemy import BaseEnemy, NSided
from game.maps import Map
from game.towers import BaseTower


class Game:
    def __init__(self, level: int):
        self.map = Map(level)
        
        self.tick = 0
        self.running = True
        
        self.enemies: List[BaseEnemy] = []
        
        self.tower = BaseTower(2, Vector2((100, 50)))
        
    def update(self):
        """Update the game this main loop itteration"""
        for enemy in self.enemies:
            enemy.update()
            
        if self.tick % 50 == 0:
            self.enemies.append(NSided((self.tick // 50)+2, self.map, self.enemy_callback))
            
    def enemy_callback(self, enemy: BaseEnemy):
        self.enemies.remove(enemy)
        
    def draw_debug(self, screen: Surface):
        """Draw a skeleton of what is on the screen"""
        self.map.draw_path_line(screen)
        for enemy in self.enemies:
            enemy.draw(screen)
            
        self.tower.draw_box(screen)