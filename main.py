import Screen
import pygame
import Soldier
import consts
import MineField

state = {
    "welcome statement": "Welcome to the Flag Game. \n Have Fun!",
    "is_window_open": True,
    "state": consts.RUNNING_STATE,
    # player place is changing during the game but this is his first place
    "player_place": (0, 0),
    # "flag place": do we need? its consts anyway
    "mine_places": consts.MINE_IMAGE,
    "grass_places": consts.GRASS_IMAGE,
    # when you press an arrow in the key_board up\down\right\left\enter it will change
    "key_input": None,
    "is_touch_flag": True,
    "is_touch_mine": True
}


def main():
    pygame.init()
    Screen.create()
    if state["is_window_open"]:
        Screen.draw_game(state)
        while state["is_window_open"]:
            handle_user_events()
        # last row in the while#
        # Screen.draw_game(state)


def handle_user_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            state["is_window_open"] = False
        elif state["state"] != consts.RUNNING_STATE:
            continue


if __name__ == '__main__':
    main()
