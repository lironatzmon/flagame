import time
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
    Soldier.create_soldier(consts.SOLDIER_IMAGE, state["player_place_x"], state["player_place_y"])
    draw_flag(state["flag_place_x"], state["flag_place_y"])

    if state["state"] == consts.LOSE_STATE:
        draw_lose_message()
    elif state["state"] == consts.WIN_STATE:
        draw_win_message()
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


def create_mine_screen(mines_list, left_corner_x, left_corner_y):
    pygame.init()
    window_size = [consts.WINDOW_WIDTH, consts.WINDOW_HEIGHT]
    scr = pygame.display.set_mode(window_size)
    pygame.display.set_caption("Mines Locations")
    scr.fill(consts.BLACK_SCREEN)
    for x in range(0, consts.WINDOW_WIDTH, consts.LENGTH):
        for y in range(0, consts.WINDOW_HEIGHT, consts.LENGTH):
            rect = pygame.Rect(x, y, consts.LENGTH, consts.LENGTH)
            pygame.draw.rect(scr, consts.GREEN_GRID, rect, 1)
    for mine in mines_list:
        cord_y = mine[0] * 20
        cord_x = mine[1] * 20
        draw_mine(cord_x, cord_y)
    Soldier.create_soldier(consts.MINE_SCREEN_SOLDIER, left_corner_x, left_corner_y)
    time.sleep(1)


def draw_mine(cord_x, cord_y):
    mine = pygame.image.load(consts.MINE_IMAGE)
    mine_size = pygame.transform.scale(mine, (
        consts.MINE_WIDTH, consts.MINE_HEIGHT))
    screen.blit(mine_size, (cord_x, cord_y))
    pygame.display.update()


def draw_flag(left_corner_x, left_corner_y):
    flag = pygame.image.load(consts.FLAG_IMAGE)
    flag_size = pygame.transform.scale(flag, (
        consts.FLAG_WIDTH, consts.FLAG_HEIGHT))
    screen.blit(flag_size, (left_corner_x, left_corner_y))
    pygame.display.update()


def draw_lose_message():
    draw_message(consts.LOSE_MESSAGE, consts.LOSE_FONT_SIZE,
                 consts.LOSE_COLOR, consts.LOSE_LOCATION)


def draw_win_message():
    draw_message(consts.WIN_MESSAGE, consts.WIN_FONT_SIZE,
                 consts.WIN_COLOR, consts.WIN_LOCATION)


def draw_message(message, font_size, color, location):
    font = pygame.font.SysFont(consts.FONT_NAME, font_size)
    text_img = font.render(message, True, color)
    screen.blit(text_img, location)
    pygame.display.update()
    time.sleep(3)
    pygame.quit()
