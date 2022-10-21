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
            row.append("")
        field.append(row)


def draw_game(state):
    screen.fill(consts.BACKGROUND_COLOR)
    put_grass_in_field(state["grass_places"])
    pygame.display.flip()


def put_grass_in_field(grass_img):
    for i in range(20):
        row_random = random.randint(0, consts.WINDOW_WIDTH)
        col_random = random.randint(0, consts.WINDOW_HEIGHT)
        grass = pygame.image.load(grass_img)
        grass_size = pygame.transform.scale(grass, (
            consts.GRASS_WIDTH, consts.GRASS_HEIGHT))
        screen.blit(grass_size, (row_random, col_random))
        pygame.display.update()
