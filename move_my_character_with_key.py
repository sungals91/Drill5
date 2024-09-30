from pico2d import *

open_canvas()
background = load_image('TUK_GROUND.png')
character_idle = load_image('Idle.png')
character_walk = load_image('Walk.png')

running = True
frame = 0
dir_x = 0
x = 800 // 2

def handle_events():
    global running, dir_x

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                dir_x += 1
            elif event.key == SDLK_LEFT:
                dir_x -= 1
            elif event.key == SDLK_ESCAPE:
                running = False
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                dir_x -= 1
            elif event.key == SDLK_LEFT:
                dir_x += 1
    pass

while running:
    clear_canvas()
    background.draw(400, 300)
    character_idle.clip_draw(frame * 128, 0, 128, 128, x, 300)
    update_canvas()
    handle_events()
    frame = (frame + 1) % 6
    x += dir_x * 10
    delay(0.05)


close_canvas()