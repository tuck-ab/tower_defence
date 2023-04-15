from typing import List

from pygame.math import Vector2
from pygame.surface import Surface

from game.enemy import BaseEnemy
from game.maps import Map
from game.spawner import Spawner
from game.towers import BaseTower, BaseProjectile, AlphaTower


class Game:
    def __init__(self, level: int):
        self.map = Map(level)
        
        self.tick = 0
        self.running = True
        
        self.enemies: List[BaseEnemy] = []
        self.projectiles: List[BaseProjectile] = []
        self.towers: List[BaseTower] = []
        
        self.spawner = Spawner(1, self.map, self.spawner_callback, self.enemy_callback)
        
        self.towers.append(AlphaTower(Vector2((350, 150)), self.add_projectile_callback))
        
    def update(self):
        """Update the game this main loop itteration"""
        for enemy in self.enemies:
            enemy.update()
            
        for tower in self.towers:
            tower.get_target(self.enemies)
            tower.update()
            
        for proj in self.projectiles:
            proj.update()
            
        print(len(self.projectiles))
            
        self.spawner.update()
            
    def enemy_callback(self, enemy: BaseEnemy):
        self.enemies.remove(enemy)
        
    def spawner_callback(self, enemy: BaseEnemy):
        self.enemies.append(enemy)
        
    def add_projectile_callback(self, projectile: BaseProjectile):
        self.projectiles.append(projectile)
        projectile.off_screen_callback = lambda x: self.projectiles.remove(x)
        
    def draw_debug(self, screen: Surface):
        """Draw a skeleton of what is on the screen"""
        self.map.draw_path_line(screen)
        
        for tower in self.towers:
            tower.draw_box(screen)
        
        for enemy in self.enemies:
            enemy.draw(screen)
            
        for proj in self.projectiles:
            proj.draw_box(screen)
            
        