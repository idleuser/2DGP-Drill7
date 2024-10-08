import random

from pico2d import *
import random

# Game object class here
class Grass:
    def __init__(self):
        # 생성자를 이용해서 객체의 초기 상태 정의
        self.image = load_image('grass.png')
    def update(self):
        pass
    def draw(self):
        self.image.draw(400,30)

class Boy:
    def __init__(self):
        self.x, self.y = random.randint(100, 700), 90
        self.frame = random.randint(0,7)
        self.image = load_image('run_animation.png')
    def update(self):
        self.frame = (self.frame + 1) % 8
        self.x += 5
    def draw(self):
        self.image.clip_draw(self.frame*100, 0, 100, 100, self.x, self.y)

class Ball:
    def __init__(self):
        self.x, self.y = random.randint(100,700), 599
        self.image_small = load_image('ball21x21.png')
        self.image_big = load_image('ball41x41.png')
        self.size = random.randint(0,1)
        self.speed = random.randint(3, 20)
    def update(self):
        if self.y <= 62 and self.size == 0:
            self.y = 62
        elif self.y <= 74 and self.size == 1:
            self.y = 74
        else:
            self.y -= self.speed
    def draw(self):
        if self.size == 0:
            self.image_small.draw(self.x, self.y)
        else:
            self.image_big.draw(self.x, self.y)

def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

def reset_world(): # 초기화하는 함수
    global running
    global grass
    global team
    global balls
    global world

    running = True
    world = []
    grass = Grass() # Grass클래스로 grass 객체 생성
    world.append(grass)
    team = [Boy() for i in range(11)]
    world += team
    balls = [Ball() for i in range(21)]
    world += balls


def update_world() :
    for i in world:
        i.update()

def render_world():
    clear_canvas()

    for i in world:
        i.draw()

    update_canvas()

open_canvas()

# initialization code
reset_world()
# game main loop code
while running:
    handle_events()
    update_world()
    render_world()
    delay(0.05)
# finalization code

close_canvas()
