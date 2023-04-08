from __future__ import annotations

from enum import Enum
from typing import Callable, List, Optional

from pygame.draw import circle, line
from pygame.math import Vector2
from pygame.surface import Surface

from game.enemy import BaseEnemy
from game.utils.colours import RED
from game.utils.sprite import Sprite


class TargetMode(Enum):
    FIRST = 0
    LAST = 1
    NEAREST = 2
    STRONGEST = 3
    
TARGET_FUNCS: List[Callable[[BaseTower, BaseEnemy], float]] = [
    lambda _, e: -e.map_step,
    lambda _, e: e.map_step,
    lambda t, e: -t.loc.distance_to(e.loc),
    lambda _, e: e.map_step ## HACK Change this when enemies have strengths
]

class BaseTower(Sprite):
    def __init__(self, tower_range: int, loc: Vector2):
        super().__init__(loc)
        
        self.range = tower_range
        self.target_mode = TargetMode.FIRST
        self.target: Optional[BaseEnemy] = None

    def get_target(self, enemies: List[BaseEnemy]) -> Optional[BaseEnemy]:
        """Gets a target using the `target_mode` attribute.

        Args:
            enemies (List[BaseEnemy]): List of all the enemies to select a target from.

        Returns:
            Optional[BaseEnemy]: The target or None if none in range.
        """
        in_range = list(filter(lambda x: x.loc.distance_to(self.loc) <= self.range, enemies))
        
        if len(in_range) > 0:
            key = lambda e: TARGET_FUNCS[self.target_mode.value](self, e)
            self.target = sorted(in_range, key=key)[0]
        else:
            self.target = None

        return self.target
        
    def draw_box(self, screen: Surface):
        super().draw_box(screen)
        
        circle(screen, RED, self.loc, self.range, width=5)
        
        if self.target:
            line(screen, RED, self.loc, self.target.loc)
        