from pico2d import *
import game_world
import game_framework
from boy import Boy
from grass import Grass
from ball import Ball
from zombie import Zombie
import random

boy = None


def handle_events():


    event_list = get_events()
    for event in event_list:
        if event.type == SDL_QUIT:
            game_framework.quit()
            return
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()
        else:
            boy.handle_event(event)


def init():
    global boy
    boy = Boy()

    global grass
    grass = Grass()

    #####
    global balls
    balls = [Ball(random.randint(100, 1700), 60, 0) for _ in range(30)]

    game_world.add_oject(boy)
    game_world.add_oject(grass, 0)
    game_world.add_objects(balls, 1)

    # 소년과 볼 사이의 충돌 페어를 등록
    game_world.add_collision_pair('boy:ball', boy, None)
    game_world.add_collision_pair('grass:ball', grass, None)
    for ball in balls:
        game_world.add_collision_pair('boy:ball', None, ball)
        game_world.add_collision_pair('grass:ball', None, ball)

    zombies = [Zombie() for _ in range(4)]
    game_world.add_objects(zombies, 1)

    


def pause():
    boy.pause()


def resume():
    pass


def finish():
    global boy
    game_world.clear()
    boy = None


#####
def update():
    game_world.update()

    ## 볼과 소년의 충돌 검사
    #for ball in balls.copy(): # ball'라는 카피 리스트에서 탐색. remove 오류 막기 위한 코드. 제거는 ball에서 함 balls.copy() = balls[:] 
    #    if game_world.collide(boy, ball):
    #        print('COLLISION boy : ball\n\n')
    #        boy.ball_count += 1
    #        game_world.remove_object(ball)
    #        balls.remove(ball) # ball이라는 그릇(리스트)에선 지웠지만 balls에는 (메모리상) 남아있음. 그걸 지우는 코드

    game_world.handle_collisions() #####




def render():
    clear_canvas()
    game_world.render()
    update_canvas()









