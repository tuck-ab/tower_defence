import contextlib

with contextlib.redirect_stdout(None):
    import pygame

def run():
    """Runs the game"""
    ## Initialise pygame
    pygame.init()

    ## Create the screen and the clock
    screen = pygame.display.set_mode((1280, 720))
    clock = pygame.time.Clock()