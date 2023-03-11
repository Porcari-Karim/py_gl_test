from .base import BaseWindow
import glfw

class GlfwWindow(BaseWindow):

    def __init__(self, width:int, height:int, title:int):
        self.height = height
        self.width = width
        self.window = glfw.create_window(width, height, title, None, None)
        if not self.window:
            glfw.terminate()
            return
    
    def present(self):
        glfw.swap_buffers(self.window)

    def poll_events(self):
        glfw.poll_events()

    def should_close(self)->bool:
        return glfw.window_should_close(self.window)

    def use_context(self):
        glfw.make_context_current(self.window)

        