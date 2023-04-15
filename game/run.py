import contextlib

with contextlib.redirect_stdout(None):
    import pygame

from game.game import Game
from game.utils.colours import BLACK
from game.settings import FPS, SCREEN_SIZE

def run():
    """Runs the game"""
    ## Initialise pygame
    pygame.init()

    ## Create the screen and the clock
    screen = pygame.display.set_mode(SCREEN_SIZE)
    clock = pygame.time.Clock()
    
    game = Game(1)
    
    while game.running:
        game.tick += 1
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game.running = False
        
        game.update()
        
        screen.fill(BLACK)
        
        game.draw_debug(screen)
        
        pygame.display.flip()
        
        clock.tick(FPS)
        
    pygame.quit()
