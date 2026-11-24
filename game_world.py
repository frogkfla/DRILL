world = [[], [], []]  # 0: 배경, 1: 오브젝트, 2: UI



def add_oject(o, depth=1):
    world[depth].append(o)

def add_objects(ol, depth=1):
    world[depth] += ol

def remove_object(o):
    for layer in world:
        if o in layer:
            layer.remove(o)
            remove_collision_object(o) ### 페어에서 충돌 일어난 걸 지움
            return
    raise ValueError('Cannot delete non existing object')



def update():
    for layer in world:
        for o in layer[:]:
            o.update()

def render():
    for layer in world:
        for o in layer[:]:
            o.draw()




def clear():
    for layer in world:
        layer.clear()
    collision_pairs.clear()


#####
# 충돌 검사 함수 a, b
def collide(a, b):
    # a, b의 충돌 영역을 계산하여 바운딩 박스 리턴
    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb()

    if left_a > right_b: return False
    if right_a < left_b: return False
    if top_a < bottom_b: return False
    if bottom_a > top_b: return False

    return True


collision_pairs = {} # object a,b의 충돌 페어를 등록하는 딕셔너리

#####
def add_collision_pair(group, a, b):
    if group not in collision_pairs:
        collision_pairs[group] = [[], []]
    if a :
        collision_pairs[group][0].append(a)
    if b :
        collision_pairs[group][1].append(b)



# 충돌 페어로 등록된 오브젝트들에 대해 충돌을 검사하고, 충돌 시 콜백 함수를 호출
def handle_collisions():
    for group, pairs in collision_pairs.items(): #items : 딕셔너리에서 키와 값을 구분하여 키->group 값->pairs로 보내줌
        for a in pairs[0]:
            for b in pairs[1]:
                if collide(a, b):
                    a.handle_collision(group, b)
                    b.handle_collision(group, a)


#####
def remove_collision_object(o):
    for pairs in collision_pairs.values():
        if o in pairs[0]:
            pairs[0].remove(o)
        if o in pairs[1]:
            pairs[1].remove(o)
