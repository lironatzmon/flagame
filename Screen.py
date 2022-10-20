import consts
import MineField
import pygame
import random

screen = pygame.display.set_mode(
    (consts.WINDOW_WIDTH, consts.WINDOW_HEIGHT))

field = []


def create():
    global field
    for i in range(consts.SQUARE_GRID_ROWS):
        row = []
        for j in range(consts.SQUARE_GRID_COLS):
            row.append(0)
        field.append(row)


def draw_game(state):
    screen.fill(consts.BACKGROUND_COLOR)


def create_grass():
    grass = pygame.image.load("grass.png")
    grass_size = pygame.transform.scale(grass, (
        consts.GRASS_WIDTH, consts.GRASS_HEIGHT))
    grass_box = pygame.Surface(
        (consts.GRASS_WIDTH, consts.GRASS_HEIGHT * 2), )
    grass_box.fill(consts.BACKGROUND_COLOR)
    grass_box.blit(grass_size, (0, 0))
    return grass_box


def put_grass_in_field():
    for i in range(20):
        row_random = random.randrange(consts.SQUARE_GRID_ROWS)
        col_random = random.randrange(consts.SQUARE_GRID_COLS)
        field[row_random][col_random] = create_grass()
