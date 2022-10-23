import Soldier
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
    draw_grass(state["grass_places"])
    Soldier.create_soldier(state["player_place_x"], state["player_place_y"])
    draw_flag(state["flag_place_x"], state["flag_place_y"])
    pygame.display.flip()


def draw_grass(cord_list):
    grass = pygame.image.load(consts.GRASS_IMAGE)
    grass_size = pygame.transform.scale(grass, (
        consts.GRASS_WIDTH, consts.GRASS_HEIGHT))
    for cord in cord_list:
        cord_x = cord[0]
        cord_y = cord[1]
        screen.blit(grass_size, (cord_x, cord_y))
    pygame.display.update()


def put_grass_in_field():
    cord_list = []
    for i in range(20):
        row_random = random.randint(0, consts.SQUARE_GRID_ROWS - 3)
        col_random = random.randint(0, consts.SQUARE_GRID_COLS - 3)
        cord_y = int(row_random * 20)
        cord_x = int(col_random * 20)
        cords = [cord_x, cord_y]
        cord_list.append(cords)
    return cord_list


def draw_grid():
    block_size = 20
    for x in range(0, consts.WINDOW_WIDTH, block_size):
        for y in range(0, consts.WINDOW_HEIGHT, block_size):
            rect = pygame.Rect(x, y, block_size, block_size)
            pygame.draw.rect(screen, consts.WHITE, rect, 1)


def draw_mine():
    mine = pygame.image.load(consts.MINE_IMAGE)
    mine_size = pygame.transform.scale(mine, (
        consts.MINE_WIDTH, consts.MINE_HEIGHT))
    return mine, mine_size


def draw_flag(left_corner_x, left_corner_y):
    flag = pygame.image.load(consts.FLAG_IMAGE)
    flag_size = pygame.transform.scale(flag, (
        consts.FLAG_WIDTH, consts.FLAG_HEIGHT))
    screen.blit(flag_size, (left_corner_x, left_corner_y))
    pygame.display.update()
