import Screen
import pygame
import Soldier
import consts
import MineField

state = {
    "welcome statement": "Welcome to the Flag Game. \n Have Fun!",
    "is_window_open": True,
    "state": consts.RUNNING_STATE,
    "player_place_x": 0,
    "player_place_y": 0,
    "main_matrix": MineField.create_main_matrix(),
    "flag_place_x": consts.WINDOW_WIDTH - consts.FLAG_WIDTH,
    "flag_place_y": consts.WINDOW_HEIGHT - consts.FLAG_HEIGHT,
    "mine_places": consts.MINE_IMAGE,
    "grass_places": Screen.put_grass_in_field(),
    "key_input": False,

}

sol_pic = "soldier.png"


def main():
    pygame.init()
    Screen.create()
    Screen.draw_game(state)
    while state["is_window_open"]:

        handle_user_events()

        if state["key_input"]:
            state["key_input"] = False
            state["player_place_x"], state["player_place_y"] = press_check(state["player_place_x"], state["player_place_y"])
            Screen.draw_game(state)

        list_index_sol_body = Soldier.index_of_soldier(state["player_place_x"], state["player_place_y"]),
        list_index_sol_legs = Soldier.index_of_soldier_legs(state["player_place_x"], state["player_place_y"])

        if MineField.check_touch_mine(list_index_sol_legs):
            state["state"] = consts.LOSE_STATE
            lose_message()
        if MineField.check_touch_flag(list_index_sol_body):
            state["state"] = consts.WIN_STATE
            win_message()


def handle_user_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            state["is_window_open"] = False
        elif state["state"] != consts.RUNNING_STATE:
            continue
        if event.type == pygame.KEYDOWN:
            state["key_input"] = True


def press_check(cord_x, cord_y):
    key_input = pygame.key.get_pressed()
    step = 20
    if key_input[pygame.K_LEFT]:
        cord_x -= step
    if key_input[pygame.K_RIGHT]:
        cord_x += step
    if key_input[pygame.K_UP]:
        cord_y -= step
    if key_input[pygame.K_DOWN]:
        cord_y += step
    if key_input[pygame.K_RETURN]:
        Screen.create_mine_screen()
    return cord_x, cord_y


def lose_message():
    Screen.draw_lose_message()


def win_message():
    Screen.draw_win_message()


if __name__ == '__main__':
    main()
