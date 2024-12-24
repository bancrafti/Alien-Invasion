import sys  # exit
import pygame

from settings import Settings
from ship import Ship
import game_functions as gf


def run_game():
    # initialize the game, settings, and screen object.
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height)
    )  # 1200 pixels by 800 pixels
    pygame.display.set_caption("Alien Invasion")

    # Make a ship
    ship = Ship(screen)

    # set background color
    bg_color = (230, 230, 230)

    # Start the loop for the game.
    while True:
        gf.check_events(ship)
        gf.update_screen(ai_settings, screen, ship)


run_game()
