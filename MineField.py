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
    print(mine_flag_grid)


def put_flag_places():
    for row in range(21, 24):
        for col in range(46, 50):
            mine_flag_grid[row][col] = "F"


def put_mine_in_field():
    list_places_mines = []
    for i in range(20):
        row_random = random.randint(0, consts.SQUARE_GRID_ROWS - 3)
        col_random = random.randint(0, consts.SQUARE_GRID_COLS - 3)
        # row_random = i
        # col_random = i
        for j in range(0, 3):
            mine_flag_grid[row_random][col_random + j] = "M"
        # cord_x = int(row_random * 20)
        # cord_y = int(col_random * 20)
        # cords = [cord_x, cord_y]
        index = [row_random, col_random]
        list_places_mines.append(index)
    return list_places_mines


# def check_touch_mine(list_index_sol_legs):
#     for leg in list_index_sol_legs:
#         if mine_flag_grid[leg[0]][leg[1]] == "M":
#             return True
#     return False
def check_touch_mine(list_index_sol_legs, mine_places):
    for leg in list_index_sol_legs:
        if leg in mine_places:
            return True
    return False


def check_touch_flag(list_index_sol_body):
    if mine_flag_grid[list_index_sol_body[0][0]][list_index_sol_body[0][1]] == "F" or \
            mine_flag_grid[list_index_sol_body[1][0]][list_index_sol_body[1][1]] == "F" or \
            mine_flag_grid[list_index_sol_body[2][0]][list_index_sol_body[2][1]] == "F" or \
            mine_flag_grid[list_index_sol_body[3][0]][list_index_sol_body[3][1]] == "F":
        print("true")
        return True
    return False

# def check_touch_flag(list_index_sol_legs):
#     for row in range(23, 25):
#         for col in range(46, 50):
#             if list_index_sol_legs[1] == [row, col]:
#                 return True
