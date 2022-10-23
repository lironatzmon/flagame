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
