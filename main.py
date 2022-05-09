##CAITLIN PESTANA
##NO DEATH IF DROWN// NO SOUND// NO SCORE// NO LIVES// NO COMMENTS
##use arrow keys to move frog, try not to die

import types
import arcade
import random
import Comp151Window


def main():
    window = Comp151Window.Comp151Window(800, 800, "Frogger")
    window.background_color = arcade.color.SKY_BLUE
    window.street = arcade.Sprite("railroad.jpg", 1.1)
    window.endpanel = arcade.Sprite("grass (2).jpg", 1.25)
    window.startpanel = arcade.Sprite("brix (2).jpg")
    window.safespot = arcade.Sprite("img.png", .75)
    window.water = arcade.Sprite("water (2).jpeg", 1.1)
    window.frog = arcade.Sprite("frog.png", .75)

    window.firstcar = arcade.Sprite("truck.png", .1, flipped_horizontally=True)
    window.secondcar = arcade.Sprite("truck.png", .1)
    window.thirdcar = arcade.Sprite("truck.png", .1, flipped_horizontally=True)
    window.fourthcar = arcade.Sprite("truck.png", .1)
    window.firstlog = arcade.Sprite("mushroom.png", 1.25)
    window.secondlog = arcade.Sprite("mushroom.png", 1.25)
    window.thirdlog = arcade.Sprite("mushroom.png", 1.25)
    window.fourthlog = arcade.Sprite("mushroom.png", 1.25)

    window.gameover = arcade.Sprite("gameover.png")
    
    window.street.center_y = 210
    window.endpanel.center_y = 825
    window.startpanel.center_y = 10
    window.safespot.center_y = 400
    window.water.center_y = 590

    window.firstcar.center_y = 90
    window.secondcar.center_y = 175
    window.thirdcar.center_y = 255
    window.fourthcar.center_y = 335
    window.firstlog.center_y = 470
    window.secondlog.center_y = 550
    window.thirdlog.center_y = 625
    window.fourthlog.center_y = 700
    window.endpanel.center_x = 400
    window.street.center_x = 400
    window.startpanel.center_x = 400
    window.safespot.center_x = 400
    window.water.center_x = 400
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

    window.lose = False

    window.on_draw = types.MethodType(comp151_draw, window)
    window.on_key_press = types.MethodType(handle_key_press, window)
    window.on_key_release = types.MethodType(handle_key_release, window)

    arcade.run()


def winner_screen(window):
    if 750 < window.frog.center_y < 800:
        window.background_color = arcade.color.LIGHT_CORNFLOWER_BLUE
        arcade.draw_text("YOU WIN!", 400, 750, arcade.color.BLACK, font_size=40)

def loser_screen(window):
        window.background_color = arcade.color.BLACK
        window.gameover.draw()
        window.gameover.center_x = 400
        window.gameover.center_y = 400
        window.street.kill()
        window.endpanel.kill()
        window.startpanel.kill()
        window.safespot.kill()
        window.water.kill()
        window.frog.kill()
        window.firstcar.kill()
        window.secondcar.kill()
        window.thirdcar.kill()
        window.fourthcar.kill()
        window.firstlog.kill()
        window.secondlog.kill()
        window.thirdlog.kill()
        window.fourthlog.kill()
        window.lose = False





def does_collide(sprite1, sprite2):
    return sprite1.collides_with_sprite(sprite2)


def does_collide_with_any_in_list(player, sprite_list):
    # first I'll create an arcade thing to do most of the work for me
    easy_list = arcade.SpriteList()
    easy_list.extend(sprite_list)
    return player.collides_with_list(easy_list)


def car_crashes(window):
    ##CRASH NOISES HERE
    if does_collide(window.frog, window.firstcar):
        loser_screen(window)
    if does_collide(window.frog, window.secondcar):
        loser_screen(window)
    if does_collide(window.frog, window.thirdcar):
        loser_screen(window)
    if does_collide(window.frog, window.fourthcar):
        loser_screen(window)



def stick_to_log(window):

    if 445 < window.frog.center_y < 750:

        if does_collide(window.frog, window.firstlog):
            window.frog.center_x = window.firstlog.center_x

        elif does_collide(window.frog, window.secondlog):
            window.frog.center_x = window.secondlog.center_x

        elif does_collide(window.frog, window.thirdlog):
            window.frog.center_x = window.thirdlog.center_x

        elif does_collide(window.frog, window.fourthlog):
            window.frog.center_x = window.fourthlog.center_x
        else:
            loser_screen(window)








def comp151_draw(window):
    arcade.start_render()
    if not window.lose:
        update_shroom_and_trucks(window)
        update_frog_location(window)
        car_crashes(window)
        stick_to_log(window)
        window.street.draw()
        window.endpanel.draw()
        window.startpanel.draw()

        window.water.draw()
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
        winner_screen(window)
    arcade.finish_render()


def update_shroom_and_trucks(window):
    window.firstlog.change_x = +2
    window.secondlog.change_x = -3
    window.thirdlog.change_x = +1
    window.fourthlog.change_x = -2
    window.firstcar.change_x =6
    window.secondcar.change_x = -9
    window.thirdcar.change_x = +5
    window.fourthcar.change_x = -7
    window.firstlog.center_x += window.firstlog.change_x
    window.secondlog.center_x += window.secondlog.change_x
    window.thirdlog.center_x += window.thirdlog.change_x
    window.fourthlog.center_x += window.fourthlog.change_x
    window.firstcar.center_x += window.firstcar.change_x
    window.secondcar.center_x += window.secondcar.change_x
    window.thirdcar.center_x += window.thirdcar.change_x
    window.fourthcar.center_x += window.fourthcar.change_x
    if window.firstlog.center_x < -36:
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