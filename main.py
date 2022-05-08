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

    window.firstcar = arcade.Sprite("truck.png", .1, flipped_horizontally=True)
    window.secondcar = arcade.Sprite("truck.png", .1)
    window.thirdcar = arcade.Sprite("truck.png", .1, flipped_horizontally=True)
    window.fourthcar = arcade.Sprite("truck.png", .1)
    window.firstlog = arcade.Sprite("mushroom.png")
    window.secondlog = arcade.Sprite("mushroom.png")
    window.thirdlog = arcade.Sprite("mushroom.png")
    window.fourthlog = arcade.Sprite("mushroom.png")
    window.firstcar.center_y = 100
    window.secondcar.center_y = 175
    window.thirdcar.center_y = 250
    window.fourthcar.center_y = 325
    window.firstlog.center_y = 475
    window.secondlog.center_y = 550
    window.thirdlog.center_y = 625
    window.fourthlog.center_y = 700
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


def loser(window):
    window.background_color = arcade.color.BLACK
    arcade.draw_text("GAME OVER", 400, 400, arcade.color.MAGENTA, font_size=50)


def does_collide(sprite1, sprite2):
    return sprite1.collides_with_sprite(sprite2)


def car_crashes(window):
    ##CRASH NOISES HERE
    if does_collide(window.frog, window.firstcar):
        window.display_text = "OUCH"
    if does_collide(window.frog, window.secondcar):
        window.display_text = "OUCH"
    if does_collide(window.frog, window.thirdcar):
        window.display_text = "OUCH"
    if does_collide(window.frog, window.fourthcar):
        window.display_text = "OUCH"
    arcade.draw_text(window.display_text, 50, 750, arcade.color.BLACK, font_size=20)
    loser(window)

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
    window.firstlog.change_x = +7
    window.secondlog.change_x = -5
    window.thirdlog.change_x = +5
    window.fourthlog.change_x = -7
    window.firstcar.change_x = +4
    window.secondcar.change_x = -6
    window.thirdcar.change_x = +6
    window.fourthcar.change_x = -4
    window.firstlog.center_x += window.firstcar.change_x
    window.secondlog.center_x += window.secondcar.change_x
    window.thirdlog.center_x += window.thirdcar.change_x
    window.fourthlog.center_x += window.fourthcar.change_x
    window.firstcar.center_x += window.firstlog.change_x
    window.secondcar.center_x += window.secondlog.change_x
    window.thirdcar.center_x += window.thirdlog.change_x
    window.fourthcar.center_x += window.fourthlog.change_x
    if window.firstlog.center_x <-36:
        window.firstlog.center_x = 836
    if window.firstlog.center_x > 836:
        window.firstlog.center_x = -36
    if window.secondlog.center_x < -36:
        window.secondlog.center_x = 836
    if window.secondlog.center_x > 836:
        window.secondlog.center_x = -36
    if window.thirdlog.center_x < -36:
        window.thirdlog.center_x = 836
    if window.thirdlog.center_x > 836:
        window.thirdlog.center_x = -36
    if window.fourthlog.center_x < -36:
        window.fourthlog.center_x = 836
    if window.fourthlog.center_x > 836:
        window.fourthlog.center_x = -36
    if window.firstcar.center_x < -36:
        window.firstcar.center_x = 836
    if window.firstcar.center_x > 836:
        window.firstcar.center_x = -36
    if window.secondcar.center_x < -36:
        window.secondcar.center_x = 836
    if window.secondcar.center_x > 836:
        window.secondcar.center_x = -36
    if window.thirdcar.center_x < -36:
        window.thirdcar.center_x = 836
    if window.thirdcar.center_x > 836:
        window.thirdcar.center_x = -36
    if window.fourthcar.center_x < -36:
        window.fourthcar.center_x = 836
    if window.fourthcar.center_x > 836:
        window.fourthcar.center_x = -36


def update_frog_location(window):
    if window.frog_dx != 0:
        window.frog.center_x += window.frog_dx
    if window.frog_dy != 0:
        window.frog.center_y += window.frog_dy
    if window.frog.center_x < -36:
        window.frog.center_x = 836
    if window.frog.center_x > 836:
        window.frog.center_x = -36

def handle_key_press(window, key, mod):
    if key == arcade.key.LEFT:
        window.frog_dx = -3
    elif key == arcade.key.RIGHT:
        window.frog_dx = 3
    if key == arcade.key.UP:
        window.frog_dy = 3
    elif key == arcade.key.DOWN:
        window.frog_dy = -3

def handle_key_release(window, key, mod):
    if key == arcade.key.LEFT or key == arcade.key.RIGHT:
        window.frog_dx = 0
    if key == arcade.key.UP or key == arcade.key.DOWN:
        window.frog_dy = 0


main()
