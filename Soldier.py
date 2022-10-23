import pygame
import Screen
import consts


def soldier(left_corner_x, left_corner_y):
    soldier = pygame.image.load(consts.SOLDIER_IMAGE)
    soldier_size = pygame.transform.scale(soldier, (
        consts.SOLDIER_WIDTH, consts.SOLDIER_HEIGHT))
    Screen.screen.blit(soldier_size, (left_corner_x, left_corner_y))
    pygame.display.update()
    return soldier, soldier_size


def index_of_soldier(left_corner_x, left_corner_y):
    index_row = left_corner_x / 20
    index_col = left_corner_y / 20
    index_list = []
    for row in range(index_row, index_row + 4):
        for col in range(index_col, index_col + 2):
            index_of_left_corner = [row, col]
            index_list.append(index_of_left_corner)
    return index_list


def index_of_soldier_legs(left_corner_x, left_corner_y):
    index_row = left_corner_x / 20
    index_col = left_corner_y / 20
    index_list = []
    for row in range(index_row + 3, index_row + 2):
        for col in range(index_col, index_col + 2):
            index_of_left_corner = [row, col]
            index_list.append(index_of_left_corner)
    return index_list
