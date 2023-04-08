import json
import os
from typing import List, Tuple, Callable

from game.enemy import BaseEnemy, NSided
from game.maps import Map
from game.utils.dir_paths import LEVELS_DIR

TOWER_CLASS_MAPPER = [
    NSided
]

def load_spawns(level: int, curr_map: Map, 
                e_callback: Callable[[BaseEnemy], None]) -> List[Tuple[BaseEnemy, int]]:
    with open(os.path.join(LEVELS_DIR, f"lvl{level}.json")) as f:
        json_data = json.load(f)
    
    out_list = []
    for t_index, args, delay in json_data:
        out_list.append((TOWER_CLASS_MAPPER[t_index](args[0], curr_map, e_callback), delay))
    return out_list

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
    