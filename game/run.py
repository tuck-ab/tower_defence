import contextlib

with contextlib.redirect_stdout(None):
    import pygame

from .maps import BaseMap
from .utils.colours import BLACK

FPS = 60
SCREEN_SIZE = (1280, 720)

def run():
    """Runs the game"""
    ## Initialise pygame
    pygame.init()

    ## Create the screen and the clock
    screen = pygame.display.set_mode(SCREEN_SIZE)
    clock = pygame.time.Clock()
    
    game_map = BaseMap(1)
    
    for tick in range(0, 2*FPS):
        screen.fill(BLACK)
        
        game_map.draw_path_line(screen)
        
        pygame.display.flip()
        
        clock.tick(FPS)
        