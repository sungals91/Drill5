from pico2d import *

open_canvas()
background = load_image('TUK_GROUND.png')
character_idle = load_image('Idle.png')
character_walk = load_image('Walk.png')

running = True
frame = 0

def handle_events():
    global running
    pass

while running:
    clear_canvas()
    background.draw(400, 300)
    character_idle.clip_draw(frame * 128, 0, 128, 128, 400, 300)
    update_canvas()
    frame = (frame + 1) % 6
    delay(0.05)


close_canvas()