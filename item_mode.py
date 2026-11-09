import game_framework
from pico2d import *
import game_world

import play_mode


update_underlying = True
draw_underlying = False


def init():
    global image
    play_mode.boy.clear_input()\n    play_mode.boy.input_locked = True
    image = load_image('item_select.png')


def finish():
    global image
    del image


def update():
    pass


def render():
    clear_canvas()
    game_world.render()
    image.draw(400, 300)
    update_canvas()


def select_item(ball_type):
    play_mode.boy.ball_type = ball_type
    game_framework.pop_mode()

def handle_events():
    for event in get_events():
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_i or event.key == SDLK_ESCAPE:
                game_framework.pop_mode()
            elif event.key == SDLK_0:
                play_mode.boy.ball_type = 0
                game_framework.pop_mode()
            elif event.key == SDLK_1:
                play_mode.boy.ball_type = 1
                game_framework.pop_mode()
            elif event.key == SDLK_2:
                play_mode.boy.ball_type = 2
                game_framework.pop_mode()


