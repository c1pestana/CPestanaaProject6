import arcade


class Comp151Window(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height,title)

    def setup(self):
        """ Set up the game here. Call this function to restart the game. """
        pass
    #
    # def update(self, delta_time: float):
    #     self.firstlog.change_x = +2
    #     self.secondlog.change_x = -2
    #     self.thirdlog.change_x = +4
    #     self.fourthlog.change_x = -3
    #     self.firstcar.change_x = +2
    #     self.secondcar.change_x = -2
    #     self.thirdcar.change_x = +4
    #     self.fourthcar.change_x = -3
    #     self.firstlog.center_x += self.firstcar.change()
    #     self.secondlog.center_x += self.secondcar.change()
    #     self.thirdlog.center_x += self.thirdcar.change()
    #     self.fourthlog.center_x += self.fourthcar.change()
    #     self.firstcar.center_x += self.firstlog.change()
    #     self.secondcar.center_x += self.secondlog.change()
    #     self.thirdcar.center_x += self.thirdlog.change()
    #     self.fourthcar.center_x += self.fourthlog.change()

    def on_draw(self):
        """ Render the screen. """
        # Clear the screen
        arcade.start_render()

    def on_mouse_press(self, x, y, button, key_modifiers):
        """ Called when the user presses a mouse button. """
        pass

    def on_mouse_release(self, x: float, y: float, button: int,
                         modifiers: int):
        """ Called when the user presses a mouse button. """
        pass

    def on_mouse_motion(self, x: float, y: float, dx: float, dy: float):
        """ User moves mouse """
        pass

    def on_key_press(self, symbol: int, modifiers: int):
        pass

    def on_key_release(self, symbol: int, modifiers: int):
        pass