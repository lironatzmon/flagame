import consts
import pygame

screen = pygame.display.set_mode(
    (consts.WINDOW_WIDTH, consts.WINDOW_HEIGHT))


def draw_game(state):
    screen.fill(consts.BACKGROUND_COLOR)
