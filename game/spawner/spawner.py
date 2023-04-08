from typing import List, Tuple, Callable

from game.enemy import BaseEnemy, NSided
from game.maps.map import Map

def load_spawns(level: int, curr_map: Map, 
                e_callback: Callable[[BaseEnemy], None]) -> List[Tuple[BaseEnemy, int]]:
    return [
        (NSided(3, curr_map, e_callback), 50),
        (NSided(4, curr_map, e_callback), 100),
        (NSided(5, curr_map, e_callback), 150),
        (NSided(6, curr_map, e_callback), 200)
    ]

class Spawner:
    def __init__(self, level: int, curr_map:Map, 
                 spawn_callback: Callable[[BaseEnemy], None],
                 enemy_callback: Callable[[BaseEnemy], None]):
        self.level_tick = -1
        
        self.spawns = load_spawns(level, curr_map, enemy_callback)
        self.spawn_func = spawn_callback
        
    def update(self):
        self.level_tick += 1
        
        while self.spawns and self.level_tick >= self.spawns[0][1]:
            self.spawn_func(self.spawns.pop(0)[0])
    