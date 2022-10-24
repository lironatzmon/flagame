import pygame
import consts
import random
import Screen
import Soldier

mine_flag_grid = []


def create_main_matrix():
    global mine_flag_grid
    for i in range(consts.SQUARE_GRID_ROWS):
        row = []
        for j in range(consts.SQUARE_GRID_COLS):
            row.append("E")
        mine_flag_grid.append(row)

    put_flag_places()
    put_mine_in_field()


def put_flag_places():
    for row in range(21, 24):
        for col in range(46, 50):
            mine_flag_grid[row][col] = "F"
            # flag, flag_size = Screen.draw_flag()
            # Screen.screen.blit(flag_size, (row * consts.LENGTH, col * consts.LENGTH))
            # pygame.display.update()


def put_mine_in_field():
    list_places_mines = []
    num_mines = 0
    while num_mines < 20:
        row_random = random.randint(0, consts.SQUARE_GRID_ROWS - 3)
        col_random = random.randint(0, consts.SQUARE_GRID_COLS - 3)
        if mine_flag_grid[row_random][col_random] == "E":
            if mine_flag_grid[row_random][col_random] != "M":
                mine_flag_grid[row_random][col_random] = "M"
                list_places_mines.append([row_random, col_random])
                num_mines += 1
    return list_places_mines


def check_touch_mine(list_index_sol_legs):
    for part in list_index_sol_legs:
        if mine_flag_grid[part[0]][part[1]] == "M":
            return True


def check_touch_flag(list_index_sol_body):
    if mine_flag_grid[list_index_sol_body[0][0]][list_index_sol_body[0][1]] == "F" or \
            mine_flag_grid[list_index_sol_body[1][0]][list_index_sol_body[1][1]] == "F" or \
            mine_flag_grid[list_index_sol_body[2][0]][list_index_sol_body[2][1]] == "F" or \
            mine_flag_grid[list_index_sol_body[3][0]][list_index_sol_body[3][1]] == "F":
        return True

# def check_touch_flag(list_index_sol_legs):
#     for row in range(23, 25):
#         for col in range(46, 50):
#             if list_index_sol_legs[1] == [row, col]:
#                 return True
