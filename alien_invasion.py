import sys  # exit
import pygame

from pygame.sprite import Group
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
    pygame.display.set_caption("Dush Dush!")

    # Make a ship, a group of bullets, a group of aliens
    ship = Ship(ai_settings, screen)

    # Make a group to store bullets in
    bullets = Group()

    # Make a group to store aliens in
    aliens = Group()

    # Create a fleet of aliens
    gf.create_fleet(ai_settings, screen, aliens, ship)

    # set background color
    bg_color = (230, 230, 230)

    # Start the loop for the game.
    while True:
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        gf.update_bullets(bullets)
        gf.update_screen(ai_settings, screen, ship, bullets, aliens)
        gf.update_aliens(ai_settings, aliens)


run_game()
