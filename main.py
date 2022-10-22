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
    "mine_places": None,
    "grass_places": consts.GRASS_IMAGE,
    "enter_key": True,
    "right_button": True,
    "left_button": True,
    "up_button": True,
    "down_button": True,
}


def main():
    pygame.init()
    Screen.create()
    if state["is_window_open"]:
        Screen.draw_game(state)
    # while state["is_window_open"]:
    #     #handle_user_events()
    #     # last row in the while#
    #     Screen.draw_game(state)



def handle_user_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            state["is_window_open"] = False
        elif state["state"] != consts.RUNNING_STATE:
            continue


if __name__ == '__main__':
    main()
