from pygame.math import Vector2

from game.settings import SCREEN_SIZE


UP = Vector2((0, -1))
DOWN = Vector2((0, 1))
LEFT = Vector2((-1, 0))
RIGHT = Vector2((1, 0))

def get_direction(source: Vector2, dest: Vector2) -> Vector2:
    return (dest-source).normalize()

OFF_SCREEN_BUFFER = max(map(lambda x: 0.25*x, SCREEN_SIZE))

def off_screen(loc: Vector2) -> bool:
    return (loc.x < 0 - OFF_SCREEN_BUFFER or
            loc.x > SCREEN_SIZE[0] + OFF_SCREEN_BUFFER or
            loc.y < 0 - OFF_SCREEN_BUFFER or
            loc.y > SCREEN_SIZE[1] + OFF_SCREEN_BUFFER)