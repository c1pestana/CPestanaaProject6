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
    window.firstcar = arcade.create_rectangle(25, 125, 50, 50, arcade.color.PURPLE)
    window.secondcar = arcade.create_rectangle(775, 175, 50, 50, arcade.color.PURPLE)
    window.thirdcar = arcade.create_rectangle(25, 250, 50, 50, arcade.color.PURPLE)
    window.fourthcar = arcade.create_rectangle(775, 325, 50, 50, arcade.color.PURPLE)

    window.firstlog = arcade.create_rectangle(25, 500, 50, 50, arcade.color.DARK_BROWN)
    window.secondlog = arcade.create_rectangle(775, 575, 50, 50, arcade.color.DARK_BROWN)
    window.thirdlog = arcade.create_rectangle(25, 625, 50, 50, arcade.color.DARK_BROWN)
    window.fourthlog = arcade.create_rectangle(775, 700, 50, 50, arcade.color.DARK_BROWN)
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


def update(window, delta_time: float):
    window.firstlog.change_x = +2
    window.secondlog.change_x = -2
    window.thirdlog.change_x = +4
    window.fourthlog.change_x = -3
    window.firstcar.change_x = +2
    window.secondcar.change_x = -2
    window.thirdcar.change_x = +4
    window.fourthcar.change_x_x = -3
    window.firstlog.center_x += window.firstcar.change_x()
    window.secondlog.center_x += window.secondcar.change_x()
    window.thirdlog.center_x += window.thirdcar.change_x()
    window.fourthlog.center_x += window.fourthcar.change_x()
    window.firstcar.center_x += window.firstlog.change_x()
    window.secondcar.center_x += window.secondlog.change_x()
    window.thirdcar.center_x += window.thirdlog.change_x()
    window.fourthcar.center_x += window.fourthlog.change_x()

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