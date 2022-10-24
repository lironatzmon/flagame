import pygame
import Screen
import consts


def create_soldier(soldier_img, left_corner_x, left_corner_y):
    soldier = pygame.image.load(soldier_img)
    soldier_size = pygame.transform.scale(soldier, (
        consts.SOLDIER_WIDTH, consts.SOLDIER_HEIGHT))
    if left_corner_y < 0 and left_corner_x > 960:
        Screen.screen.blit(soldier_size, (960, 0))
        pygame.display.update()
    elif left_corner_y > 420 and left_corner_x < 0:
        Screen.screen.blit(soldier_size, (0, 420))
        pygame.display.update()
    elif left_corner_y > 420 and left_corner_x > 960:
        Screen.screen.blit(soldier_size, (960, 420))
        pygame.display.update()
    elif left_corner_y < 0 and left_corner_x < 0:
        Screen.screen.blit(soldier_size, (0, 0))
        pygame.display.update()
    elif left_corner_y < 0:
        Screen.screen.blit(soldier_size, (left_corner_x, 0))
        pygame.display.update()
    elif left_corner_y > 420:
        Screen.screen.blit(soldier_size, (left_corner_x, 420))
        pygame.display.update()
    elif left_corner_x < 0:
        Screen.screen.blit(soldier_size, (0, left_corner_y))
        pygame.display.update()
    elif left_corner_x > 960:
        Screen.screen.blit(soldier_size, (960, left_corner_y))
        pygame.display.update()
    else:
        Screen.screen.blit(soldier_size, (left_corner_x, left_corner_y))
        pygame.display.update()


def index_of_soldier(left_corner_x, left_corner_y):
    index_row = int(left_corner_x / 20)
    index_col = int(left_corner_y / 20)
    index_list = []
    for row in range(index_row, index_row + 4):
        for col in range(index_col, index_col + 2):
            index_of_left_corner = [row, col]
            index_list.append(index_of_left_corner)
    return index_list


def index_of_soldier_legs(left_corner_x, left_corner_y):
    index_row = int(left_corner_x / 20)
    index_col = int(left_corner_y / 20)
    index_list = []
    for row in range(index_row + 3, index_row + 4):
        for col in range(index_col, index_col + 2):
            index_of_left_corner = [row, col]
            index_list.append(index_of_left_corner)
    return index_list
