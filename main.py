import types

import arcade
import random

import Comp151Window


def main():
    window = Comp151Window.Comp151Window(800, 800, "Moving demo")
    window.background_color = arcade.color.SKY_BLUE
    window.street = arcade.create_rectangle(400, 200, window.width, 350, arcade.color.CHARCOAL)
    window.endpanel = arcade.create_rectangle(400, 775, window.width, 50, arcade.color.FOREST_GREEN)
    window.startpanel = arcade.create_rectangle(400, 25, window.width, 50, arcade.color.FOREST_GREEN)
    window.safespot = arcade.create_rectangle(400, 400, window.width, 50, arcade.color.BLACK)
    window.frog = arcade.Sprite("frog.png")
    window.firstcar = arcade.Sprite("mushroom.png")
    window.secondcar = arcade.Sprite("mushroom.png")
    window.thirdcar = arcade.Sprite("mushroom.png")
    window.fourthcar = arcade.Sprite("mushroom.png")
    window.firstlog = arcade.Sprite("mushroom.png")
    window.secondlog = arcade.Sprite("mushroom.png")
    window.thirdlog = arcade.Sprite("mushroom.png")
    window.fourthlog = arcade.Sprite("mushroom.png")
    window.firstcar.center_y = 50
    window.secondcar.center_y = 100
    window.thirdcar.center_y = 150
    window.fourthcar.center_y = 200
    window.firstlog.center_y = 300
    window.secondlog.center_y = 350
    window.thirdlog.center_y = 400
    window.fourthlog.center_y = 450
    
    window.firstcar.center_x = 0
    window.secondcar.center_x = 0
    window.thirdcar.center_x = 0
    window.fourthcar.center_x = 0
    window.firstlog.center_x = 0
    window.secondlog.center_x = 0
    window.thirdlog.center_x = 0
    window.fourthlog.center_x = 0
    
    window.frog.center_x = 400
    window.frog.center_y = 25
    window.frog_dx = 0
    window.frog_dy = 0
    window.on_draw = types.MethodType(comp151_draw, window)
    window.on_key_press = types.MethodType(handle_key_press, window)
    window.on_key_release = types.MethodType(handle_key_release, window)
    arcade.run()



def comp151_draw(window):
    arcade.start_render()
    update(window)
    update_frog_location(window)
    window.street.draw()
    window.endpanel.draw()
    window.startpanel.draw()
    window.safespot.draw()
    window.firstcar.draw()
    window.secondcar.draw()
    window.thirdcar.draw()
    window.fourthcar.draw()
    window.firstlog.draw()
    window.secondlog.draw()
    window.thirdlog.draw()
    window.fourthlog.draw()
    window.frog.draw()
    arcade.finish_render()


def update(window):
    window.firstlog.change_x = +2
    window.secondlog.change_x = -2
    window.thirdlog.change_x = +4
    window.fourthlog.change_x = -3
    window.firstcar.change_x = +2
    window.secondcar.change_x = -2
    window.thirdcar.change_x = +4
    window.fourthcar.change_x = -3
    window.firstlog.center_x += window.firstcar.change_x
    window.secondlog.center_x += window.secondcar.change_x
    window.thirdlog.center_x += window.thirdcar.change_x
    window.fourthlog.center_x += window.fourthcar.change_x
    window.firstcar.center_x += window.firstlog.change_x
    window.secondcar.center_x += window.secondlog.change_x
    window.thirdcar.center_x += window.thirdlog.change_x
    window.fourthcar.center_x += window.fourthlog.change_x

def update_frog_location(window):
    if window.frog_dx != 0:
        window.frog.center_x += window.frog_dx
    if window.frog_dy !=0:
        window.frog.center_y += window.frog_dy
    if window.frog.center_x <-36:
        window.frog.center_x = 836
    if window.frog.center_x > 836:
        window.frog.center_x = -36

def handle_key_press(window, key, mod):
    if key == arcade.key.LEFT:
        window.frog_dx= -3
    elif key == arcade.key.RIGHT:
        window.frog_dx =3
    if key == arcade.key.UP:
        window.frog_dy = 3
    elif key == arcade.key.DOWN:
        window.frog_dy = -3

def handle_key_release(window, key, mod):
    if key == arcade.key.LEFT or key == arcade.key.RIGHT:
        window.frog_dx =0
    if key == arcade.key.UP or key == arcade.key.DOWN:
        window.frog_dy =0

main()