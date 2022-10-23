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
    pygame.display.set_caption("The Flag")
    put_grass_in_field(state["grass_places"])
    pygame.display.flip()


def put_grass_in_field(grass_img):
    for i in range(20):
        row_random = random.randint(0, consts.SQUARE_GRID_ROWS-3)
        col_random = random.randint(0, consts.SQUARE_GRID_COLS-3)
        cord_y = int(row_random * 20)
        cord_x = int(col_random * 20)
        grass = pygame.image.load(grass_img)
        grass_size = pygame.transform.scale(grass, (
            consts.GRASS_WIDTH, consts.GRASS_HEIGHT))
        screen.blit(grass_size, (cord_x, cord_y))
        pygame.display.update()




