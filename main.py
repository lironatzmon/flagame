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
    "player_place_x": 0,
    "player_place_y": 0,
    "flag_place_x": consts.WINDOW_WIDTH - consts.FLAG_WIDTH,
    "flag_place_y": consts.WINDOW_HEIGHT - consts.FLAG_HEIGHT,
    "mine_places": consts.MINE_IMAGE,
    "key_input": False,
    "enter_key": False,
    "is_touch_flag": True,
    "is_touch_mine": True
}


def main():
    pygame.init()
    Screen.create()

    # if state["is_window_open"]:
    Screen.draw_game(state)
    while state["is_window_open"]:

        handle_user_events()

        if state["key_input"]:

            state["player_place_x"], state["player_place_y"] = move(state["player_place_x"], state["player_place_y"])

        if state["enter_key"]:
            Screen.draw_grid()



        # last row in the while
        Screen.draw_game(state)


def handle_user_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            state["is_window_open"] = False
        elif state["state"] != consts.RUNNING_STATE:
            continue
        elif event.type == pygame.KEYDOWN:
            state["key_input"] = True
        key_input = pygame.key.get_pressed()
        if key_input[pygame.K_KP_ENTER]:
            state["enter_key"] = True


def move(cord_x, cord_y):
    key_input = pygame.key.get_pressed()
    state["key_input"] = True
    step = 20
    if key_input[pygame.K_LEFT]:
        cord_x -= step
    if key_input[pygame.K_RIGHT]:
        cord_x += step
    if key_input[pygame.K_UP]:
        cord_y -= step
    if key_input[pygame.K_DOWN]:
        cord_y += step
    return cord_x, cord_y

# def press_enter_in_key_board():
#     key_input = pygame.key.get_pressed()
#     if key_input[pygame.K_KP_ENTER]:



if __name__ == '__main__':
    main()
