from pico2d import *
import game_framework
import game_world
from boy import Boy
from grass import Grass
import title_mode
import pause_mode

item_select_image = None


def handle_events():
    event_list = get_events()
    for event in event_list:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.change_mode(title_mode)
            return
        elif event.type == SDL_KEYDOWN and event.key == SDLK_p:
            game_framework.push_mode(pause_mode)
            return
        else:
            boy.handle_event(event)



def init():
    global boy, item_select_image

    item_select_image = load_image('item_select.png')

    boy = Boy()
    game_world.add_oject(boy)

    grass = Grass()
    game_world.add_oject(grass, 0)



def update():
    game_world.update()


def render():
    clear_canvas()
    game_world.render()
    item_select_image.draw(150, 485)
    update_canvas()

def finish():
    global boy, item_select_image
    game_world.clear()
    boy = None
    del item_select_image
    item_select_image = None


def pause():
    boy.pressed_keys.clear()
    if boy.state == 'RUN':
        boy.dir = 0
        boy.stop_run()


def resume():
    pass


