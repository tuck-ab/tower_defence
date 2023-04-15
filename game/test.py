from pygame.math import Vector2

from game.towers import BaseProjectile

def test():
    thing = BaseProjectile(Vector2((500, 500)), Vector2((1, 0)))