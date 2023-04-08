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
        
        self.enemies.append(NSided(3, self.map, self.enemy_callback))
        
        self.tower = BaseTower(230, Vector2((300, 300)))
        
    def update(self):
        """Update the game this main loop itteration"""
        for enemy in self.enemies:
            enemy.update()
            
        if self.tick == 50:
            self.enemies.append(NSided((self.tick // 50)+3, self.map, self.enemy_callback))
            
        target = self.tower.get_target(self.enemies)
            
    def enemy_callback(self, enemy: BaseEnemy):
        self.enemies.remove(enemy)
        self.enemies.append(NSided(enemy.sides, self.map, self.enemy_callback))
        
    def draw_debug(self, screen: Surface):
        """Draw a skeleton of what is on the screen"""
        self.map.draw_path_line(screen)
        for enemy in self.enemies:
            enemy.draw(screen)
            
        self.tower.draw_box(screen)