import glfw

class KeyHandler:

    def __init__(self, window) -> None:
        self.pressed = {}

        def key_callback(win, key, scancode, action, mods):
            if action == glfw.PRESS:
                self.pressed[key] = True
            if action == glfw.RELEASE:
                self.pressed[key] = False

        glfw.set_key_callback(window, key_callback)

    def is_pressed(self, key):
        return self.pressed.get(key, False)