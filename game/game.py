from typing import List

from pygame.math import Vector2
from pygame.surface import Surface

from game.enemy import BaseEnemy
from game.maps import Map
from game.maps.spawner import Spawner
from game.towers import BaseTower


class Game:
    def __init__(self, level: int):
        self.map = Map(level)
        
        self.tick = 0
        self.running = True
        
        self.enemies: List[BaseEnemy] = []
        self.spawner = Spawner(1, self.map, self.spawner_callback, self.enemy_callback)
        
        self.tower = BaseTower(230, Vector2((300, 300)))
        
    def update(self):
        """Update the game this main loop itteration"""
        for enemy in self.enemies:
            enemy.update()
            
        self.spawner.update()
            
        target = self.tower.get_target(self.enemies)
            
    def enemy_callback(self, enemy: BaseEnemy):
        self.enemies.remove(enemy)
        
    def spawner_callback(self, enemy: BaseEnemy):
        self.enemies.append(enemy)
        
    def draw_debug(self, screen: Surface):
        """Draw a skeleton of what is on the screen"""
        self.map.draw_path_line(screen)
        for enemy in self.enemies:
            enemy.draw(screen)
            
        self.tower.draw_box(screen)