import consts
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
        row_random = random.randint(0, consts.SQUARE_GRID_ROWS - 3)
        col_random = random.randint(0, consts.SQUARE_GRID_COLS - 3)
        cord_y = int(row_random * 20)
        cord_x = int(col_random * 20)
        grass = pygame.image.load(grass_img)
        grass_size = pygame.transform.scale(grass, (
            consts.GRASS_WIDTH, consts.GRASS_HEIGHT))
        screen.blit(grass_size, (cord_x, cord_y))
        pygame.display.update()


def draw_grid():
    block_size = 20
    for x in range(0, consts.WINDOW_WIDTH, block_size):
        for y in range(0, consts.WINDOW_HEIGHT, block_size):
            rect = pygame.Rect(x, y, block_size, block_size)
            pygame.draw.rect(consts.SCREEN, consts.WHITE, rect, 1)


def draw_mine():
    mine = pygame.image.load(consts.MINE_IMAGE)
    mine_size = pygame.transform.scale(mine, (
        consts.MINE_WIDTH, consts.MINE_HEIGHT))
    return mine, mine_size


def draw_flag():
    flag = pygame.image.load(consts.FLAG_IMAGE)
    flag_size = pygame.transform.scale(flag, (
        consts.FLAG_WIDTH, consts.FLAG_HEIGHT))
    return flag, flag_size
