import os

from pico2d import *
import game_framework
import game_world

font = None


def init():
    global font
    font_path = os.path.join(os.path.dirname(__file__), '..', 'LEC16_Time', 'ENCR10B.TTF')
    font = load_font(font_path, 36)


def finish():
    global font
    del font


def handle_events():
    for event in get_events():
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_p:
            game_framework.pop_mode()
            return


def update():
    pass


def render():
    clear_canvas()
    game_world.render()
    font.draw(401, 501, 'PAUSED  |  P: RESUME', (0, 0, 0))
    font.draw(400, 500, 'PAUSED  |  P: RESUME', (255, 255, 255))
    update_canvas()