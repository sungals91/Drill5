from pico2d import *

open_canvas()
background = load_image('TUK_GROUND.png')
character_idle = load_image('Idle.png')
character_walk = load_image('Walk.png')

while True:
    clear_canvas()
    background.draw(400, 300)
    character_idle.draw(400, 300)
    update_canvas()

close_canvas()