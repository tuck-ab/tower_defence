from typing import Callable

from pygame.math import Vector2

from game.towers import BaseTower, BaseProjectile
from game.utils.directions import get_direction


ALPHA_TOWER_RANGE = 500
ALPHA_TOWER_COOLDOWN = 50

class AlphaTower(BaseTower):
    def __init__(self, loc: Vector2, add_proj_callback: Callable[[BaseProjectile], None]):
        super().__init__(ALPHA_TOWER_RANGE, loc)
        
        self.add_projectile_callback = add_proj_callback
        self.projectile_speed = 15
        
        self.cooldown = ALPHA_TOWER_COOLDOWN
        self.curr_cooldown = 0
            
    def update(self):
        if self.curr_cooldown > 0:
            self.curr_cooldown -= 1
        
        ## Shooting logic
        if self.target and self.curr_cooldown <= 0:
            proj_vel = get_direction(self.loc, self.target.loc) * self.projectile_speed
            new_proj = BaseProjectile(self.loc.copy(), proj_vel)
            
            self.add_projectile_callback(new_proj)
            self.curr_cooldown = self.cooldown
        
