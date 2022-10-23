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
            row.append({"content": "E", "left_cord_x": j * consts.LENGTH, "left_cord_y": i * consts.LENGTH})
        mine_flag_grid.append(row)


def put_flag_places():
    for row in range(21, 24):
        for col in range(46, 50):
            mine_flag_grid[row][col]["content"] = "F"
            flag, flag_size = Screen.draw_flag()
            Screen.screen.blit(flag_size, (row * consts.LENGTH, col * consts.LENGTH))
            pygame.display.update()


def put_mine_in_field():
    num_mines = 0
    while num_mines < 20:
        row_random = random.randint(0, consts.SQUARE_GRID_ROWS - 3)
        col_random = random.randint(0, consts.SQUARE_GRID_COLS - 3)
        cord_y = int(row_random * 20)
        cord_x = int(col_random * 20)
        if mine_flag_grid[row_random][col_random]["content"] == "E":
            if mine_flag_grid[row_random][col_random]["content"] != "M":
                mine_flag_grid[row_random][col_random]["content"] = "M"
                num_mines += 1
        mine, mine_size = Screen.draw_mine()
        Screen.screen.blit(mine_size, (cord_x, cord_y))
        pygame.display.update()


def check_touch_mine(list_index_sol_legs):
    for part in list_index_sol_legs:
        if mine_flag_grid[part[0]][part[1]]["content"] == "M":
            return True


def check_touch_flag(list_index_sol_legs):
    for row in range(23, 25):
        for col in range(46, 50):
            if list_index_sol_legs[1] == [row, col]:
                return True
