import game_framework
from pico2d import *
import game_world
from boy import Boy
from grass import Grass

import title_mode

def handle_events():
    global boy

    event_list = get_events()
    for event in event_list:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_p:
            import stop_mode
            game_framework.push_mode(stop_mode)
        elif event.type == SDL_KEYDOWN and event.key == SDLK_i:
            import item_mode
            game_framework.push_mode(item_mode)
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.change_mode(title_mode)
        else:
            boy.handle_event(event)



def init():
    global boy

    boy = Boy()
    game_world.add_oject(boy)

    grass = Grass()
    game_world.add_oject(grass, 0)

def update():
    game_world.update()

def render():
    clear_canvas()
    game_world.render()
    update_canvas()

def finish():
    game_world.clear()


def pause():
    pass


def resume():
    pass
